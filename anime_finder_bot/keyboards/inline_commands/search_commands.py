import aiohttp
from fake_useragent import UserAgent
from bs4 import BeautifulSoup

from requests_html import AsyncHTMLSession

''' This func return news from \"news\" button'''


async def get_news():
    ua = UserAgent()

    async with aiohttp.ClientSession() as session:
        headers = {
            'user-agent': ua.random
        }
        async with session.get('https://anitube.in.ua/news/', headers=headers) as response:
            soup = BeautifulSoup(await response.text(), 'html.parser')
            news_boxes = soup.findAll('img')
            news_desc = soup.findAll('div', id='news-id-8291')

            dict_of_news = {
                'img': [],
                'desc': [],
                'link': [],
            }

            for desc in news_desc:
                dict_of_news['desc'].append(desc.text.split('(Детальніше)'))
                dict_of_news['link'].append(desc.findNext('a').get('href'))

            for news in news_boxes:
                text = news.get('src')
                if 'posts' in text:
                    link = 'anitube.in.ua' + text
                    dict_of_news['img'].append(link)

            return dict_of_news


''' This func return list of video card in loop'''


async def get_video_from_site(some_anime):
    ua = UserAgent()

    async with aiohttp.ClientSession() as session:
        headers = {
            'user-agent': ua.random
        }
        datas = {
            'do': 'search',
            'subaction': 'search',
            'story': f'{str(some_anime)}'
        }
        dict_of_videos_info = {
            'name': [],
            'img': [],
            'desc': [],
            'link': []
        }
        print(str(some_anime))
        async with session.post(url='https://anitube.in.ua/', data=datas, headers=headers) as response:
            # async with aiofiles.open("D:\\apps\\file1.html", "r", encoding="UTF-8") as file:
            soup = BeautifulSoup(await response.text(), 'html.parser')
            anime_pages = soup.findAll('div', class_='story_c')

            for page in anime_pages:
                # print(page)

                img_links = page.findAll('img')

                ''' img of page '''

                for src in img_links:
                    print(src)
                    if 'full-news-poster' in src.get('src'):
                        dict_of_videos_info['img'].append('https://anitube.in.ua/' + src.get('src').strip())
                    else:
                        pass

                '''name of page '''

                name_of_page = page.findNext('h2').find('a').text.strip()
                dict_of_videos_info['name'].append(name_of_page)

                '''description of page'''

                desc_of_page = page.findNext('div', class_='story_c_text').text.strip()
                dict_of_videos_info['desc'].append(desc_of_page)

                ''' link to video page '''

                link_page = page.findNext('a').get('href')
                dict_of_videos_info['link'].append(link_page)

        return dict_of_videos_info


''' This func return anime video players '''


async def get_anime_players(session: AsyncHTMLSession, url: str):
    list_of_players = []
    r = await session.get(url=url)
    await r.html.arender()

    result = r.html.find('.RlItem1')
    [list_of_players.append(i.text) for i in result]
    await session.close()

    return list_of_players


''' func return anime series according to player'''


async def get_anime_series(session: AsyncHTMLSession, url: str, script: str):
    r = await session.get(url=url)
    dict_of_series = []

    await r.html.arender(scrolldown=True, script=script)

    series = r.html.xpath('//option[@class="RlItem"]')
    [dict_of_series.append(ser.text) for ser in series]

    await session.close()

    return dict_of_series

