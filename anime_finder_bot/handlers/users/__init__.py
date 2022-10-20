from .bot_start import dp
from keyboards.inline_commands.search_commands import get_news
from .news import dp
from .search import dp
from .library import dp


from .error import dp

__all__ = ['dp', 'get_news']