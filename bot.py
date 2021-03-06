import time
import discord
import aiohttp
import asyncio
from discord.utils import get
from discord.ext import commands
from scripts.parsers import parse
from scripts.db_manager import SearchRequestsDbManager, ItemsShowedDbManager
from scripts.config import TOKEN, GUILD_ID, CHANEL_NAME, RESULTS_CATEGORY_NAME, SHOPIFY_FILTRED, SHOPIFY_UNFILTRED

loop = asyncio.get_event_loop()
bot = commands.Bot(command_prefix='$')

PARSER_STARTED = False

bot.loop.create_task(parse(bot))

loop.run_until_complete(ItemsShowedDbManager.clear(loop))


@bot.command(name='add-to-search')
@commands.has_role('admin')
async def add_search_request(ctx, request=None):
    channel = ctx.message.channel
    request = ctx.message.content[15:]
    guild = ctx.message.guild
    chanel_categories = guild.categories
    category = get(chanel_categories, name=RESULTS_CATEGORY_NAME)

    if request is None:
        await channel.send('''❌ Необходимо указать сам запрос в коменде: *$add-to-search **запрос***''')
        return
    elif len(request) < 2:
        await channel.send('''❌ Длинна запроса не должна быть короче 2-х символов.''')
        return
    elif await SearchRequestsDbManager.get_by_name_and_type(request, 'common', loop) is not None:
        await channel.send('''❌ Такой запрос уже есть''')
        return

    new_channel_name = '👟-' + request.replace(' ', '-')
    new_channel = await guild.create_text_channel(new_channel_name, category=category)
    await SearchRequestsDbManager.add(request, new_channel.id, 'common', loop)
    await channel.send(f'Запрос **{request}** добавлен')


@bot.command(name='filtered-add-to-search')
@commands.has_role('admin')
async def add_search_request(ctx, request=None):
    request = ctx.message.content[24:]
    channel = ctx.message.channel

    if request is None:
        await channel.send('''❌ Необходимо указать сам запрос в коменде: *$add-to-search **запрос***''')
        return
    elif len(request) < 2:
        await channel.send('''❌ Длинна запроса не должна быть короче 2-х символов.''')
        return
    elif await SearchRequestsDbManager.get_by_name_and_type(request, 'shopify-filtered', loop) is not None:
        await channel.send('''❌ Такой запрос уже есть''')
        return

    await SearchRequestsDbManager.add(request, SHOPIFY_FILTRED, 'shopify-filtered', loop)
    await channel.send(f'Запрос **{request}** добавлен')


@bot.command(name='show-requests')
@commands.has_role('admin')
async def show_requests(ctx, request=None):
    channel = ctx.message.channel
    requests = await SearchRequestsDbManager.get_all(loop)
    if len(requests) == 0:
        text = 'Список запросов пуст.'
    else:
        text = '''**Поисковые запросы**'''
        for r in requests:
            if r.type == 'shopify-filtered':
                text += f'''
**{r.id}** - {r.request} (shopify-filtered)'''
            else:
                text += f'''
**{r.id}** - {r.request}'''

    await channel.send(text)


@bot.command(name='clear-base')
@commands.has_role('admin')
async def show_requests(ctx, request=None):
    channel = ctx.message.channel
    count = await ItemsShowedDbManager.count(loop)

    await ItemsShowedDbManager.clear(loop)

    text = f'База очщена, было удалено **{count}** результата поиска'

    await channel.send(text)


@bot.command(name='delete')
@commands.has_role('admin')
async def delete(ctx, request_id=None):
    channel = ctx.message.channel
    print(channel.id)
    if request_id is None:
        await channel.send('''Необходимо указать id запроса в коменде: *$adelete **id***''')
        return
    try:
        request_id = int(request_id)
    except ValueError:
        await channel.send('''❌ Не корректный формат id''')
        return

    request = await SearchRequestsDbManager.get_by_id(request_id, loop)

    if request is None:
        await channel.send(f'''Запроса с номером **{request_id}** не существует''')
        return

    await SearchRequestsDbManager.delete(request_id, loop)
    await channel.send(f'''Запрос **{request.request}** удален''')


'''
@bot.event
async def on_command_error(ctx, error):
    channel = ctx.message.channel
    if isinstance(error, commands.NoPrivateMessage):
        await channel.send('Эту команду нельзя использовать в личных сообщениях.')
    elif isinstance(error, commands.DisabledCommand):
        await channel.send('Сожалею. Эта команда отключена и не может быть использована.')
    elif isinstance(error, commands.CheckFailure):
        await channel.send('Сожалею. У вас нет разрешения на использование этой команды.')
    elif isinstance(error, commands.CommandNotFound):
        await channel.send("Я не знаю эту команду")
'''
bot.run(TOKEN)
