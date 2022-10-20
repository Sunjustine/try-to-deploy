from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import aiohttp
import asyncio


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
            print(dict_of_videos_info)
loop = asyncio.get_event_loop()
loop.run_until_complete(get_video_from_site("поклик"))