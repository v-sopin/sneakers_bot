import time
import json
import asyncio
import aiohttp
from bs4 import BeautifulSoup
from scripts.db_manager import SearchRequestsDbManager, ItemsShowedDbManager
from scripts.models import SearchRequest
import scripts.text_parsers as tp
from scripts.config import DEVELOPER_ID

loop = asyncio.get_event_loop()


async def parse(bot):
    await bot.wait_until_ready()
    user = bot.get_user(DEVELOPER_ID)
    if user.dm_channel is None:
        await user.create_dm()

    while True:
        search_requests = await SearchRequestsDbManager.get_all(loop)

        cur = time.time()
        '''
        #  0

        try:
            await hypedc_com(bot, search_requests)
        except Exception:
            print('Exception: hypedc_com')
            await user.send('Exception: hypedc_com')
        try:
            await subtypestore_com(bot, search_requests)
            raise Exception
        except Exception:
            print('Exception: subtypestore_com')
            await user.send('Exception: subtypestore_com')
        try:
            await lockwood_avenue_com(bot, search_requests)
        except Exception:
            print('Exception: lockwood_avenue_com')
            await user.send('Exception: lockwood_avenue_com')
        try:
            await footshop_eu(bot, search_requests)
        except Exception:
            print('Exception: footshop_eu')
            await user.send('Exception: footshop_eu')
        try:
            await footshop_com(bot, search_requests)
        except Exception:
            print('Exception: footshop_com')
            await user.send('Exception: footshop_com')
        try:
            await rezetstore_dk(bot, search_requests)
        except Exception:
            print('Exception: rezetstore_dk')
            await user.send('Exception: rezetstore_dk')
        try:
            await stormfashion_dk(bot, search_requests)
        except Exception:
            print('Exception: stormfashion_dk')
            await user.send('Exception: stormfashion_dk')
        try:
            await stoy_com(bot, search_requests)
        except Exception:
            print('Exception: stoy_com')
            await user.send('Exception: stoy_com')
        try:
            await dev_thegoodlifespace_com(bot, search_requests)
        except Exception:
            print('Exception: dev_thegoodlifespace_com')
            await user.send('Exception: dev_thegoodlifespace_com')
        try:
            await basket4ballers_com(bot, search_requests)
        except Exception:
            print('Exception: basket4ballers_com')
            await user.send('Exception: basket4ballers_com')

        #  10

        try:
            await bouncewear_com(bot, search_requests)
        except Exception:
            print('Exception: bouncewear_com')
            await user.send('Exception: bouncewear_com')
        try:
            await chezvibe_com(bot, search_requests)
        except Exception:
            print('Exception: chezvibe_com')
            await user.send('Exception: chezvibe_com')
        try:
            await galerieslafayette_com(bot, search_requests)
        except Exception:
            print('Exception: galerieslafayette_com')
            await user.send('Exception: galerieslafayette_com')
        try:
            await hubbastille_com(bot, search_requests)
        except Exception:
            print('Exception: hubbastille_com')
            await user.send('Exception: hubbastille_com')
        try:
            await impact_premium_com(bot, search_requests)
        except Exception:
            print('Exception: impact_premium_com')
            await user.send('Exception: impact_premium_com')
        try:
            await lerayonfrais_fr(bot, search_requests)
        except Exception:
            print('Exception: lerayonfrais_fr')
            await user.send('Exception: lerayonfrais_fr')
        try:
            await opiumparis_com(bot, search_requests)
        except Exception:
            print('Exception: opiumparis_com')
            await user.send('Exception: opiumparis_com')
        #  http://oquimstore.com/
        try:
            await shinzo_paris(bot, search_requests)
        except Exception:
            print('Exception: shinzo_paris')
            await user.send('Exception: shinzo_paris')
        
        #  20
        try:
            await shoezgallery_com(bot, search_requests)
        except Exception:
            print('Exception: shoezgallery_com')
            await user.send('Exception: shoezgallery_com')
        try:
            await snkrs_com(bot, search_requests)
        except Exception:
            print('Exception: snkrs_com')
            await user.send('Exception: snkrs_com')
        try:
            await thenextdoor_fr(bot, search_requests)
        except Exception:
            print('Exception: thenextdoor_fr')
            await user.send('Exception: thenextdoor_fr')
        try:
            await the_broken_arm_com(bot, search_requests)
        except Exception:
            print('Exception: the_broken_arm_com')
            await user.send('Exception: the_broken_arm_com')
        try:
            await zalando_fr(bot, search_requests)
        except Exception:
            print('Exception: zalando_fr')
            await user.send('Exception: zalando_fr')
        try:
            await einhalb_com(bot, search_requests)
        except Exception:
            print('Exception: einhalb_com')
            await user.send('Exception: einhalb_com')
        try:
            await asphaltgold_com(bot, search_requests)
        except Exception:
            print('Exception: asphaltgold_com')
            await user.send('Exception: asphaltgold_com')
        try:
            await allikestore_com(bot, search_requests)
        except Exception:
            print('Exception: allikestore_com')
            await user.send('Exception: allikestore_com')
        try:
            await kickz_com(bot, search_requests)
        except Exception:
            print('Exception: kickz_com')
            await user.send('Exception: kickz_com')
        try:
            await kickzpremium_com(bot, search_requests)
        except Exception:
            print('Exception: kickzpremium_com')
            await user.send('Exception: kickzpremium_com')
        
        #  30

        try:
            await rimowa_com(bot, search_requests)
        except Exception:
            print('Exception: rimowa_com')
            await user.send('Exception: rimowa_com')
        # http://thegoodwillout.com/
        try:
            await suppastore_com(bot, search_requests)
        except Exception:
            print('Exception: suppastore_com')
            await user.send('Exception: suppastore_com')
        try:
            await vooberlin_com(bot, search_requests)
        except Exception:
            print('Exception: vooberlin_com')
            await user.send('Exception: vooberlin_com')
        try:
            await zupport_de(bot, search_requests)
        except Exception:
            print('Exception: zupport_de')
            await user.send('Exception: zupport_de')
        try:
            await aw_lab_com(bot, search_requests)
        except Exception:
            print('Exception: aw_lab_com')
            await user.send('Exception: aw_lab_com')
        try:
            await back_door_it(bot, search_requests)
        except Exception:
            print('Exception: back_door_it')
            await user.send('Exception: back_door_it')

        try:
            await blackboxstore_com(bot, search_requests)
        except Exception:
            print('Exception: blackboxstore_com')
            await user.send('Exception: blackboxstore_com')

        # https://www.excelsiormilano.com/
        try:
            await footdistrict_com(bot, search_requests)
        except Exception:
            print('Exception: footdistrict_com')
            await user.send('Exception: footdistrict_com')
            
        #  40
        
        try:
            await it_oneblockdown_it(bot, search_requests)
        except Exception:
            print('Exception: it_oneblockdown_it')
            await user.send('Exception: it_oneblockdown_it')
        try:
            await sivasdescalzo_com(bot, search_requests)
        except Exception:
            print('Exception: sivasdescalzo_com')
            await user.send('Exception: sivasdescalzo_com')
        try:
            await sivasdescalzo_com(bot, search_requests)
        except Exception:
            print('Exception: shop_havenshop_com')
            await user.send('Exception: shop_havenshop_com')
        try:
            await aimeleondore_com(bot, search_requests)
        except Exception:
            print('Exception: aimeleondore_com')
            await user.send('Exception: aimeleondore_com')
        try:
            await lustmexico_com(bot, search_requests)
        except Exception:
            print('Exception: lustmexico_com')
            await user.send('Exception: lustmexico_com')
        try:
            await onenessboutique_com(bot, search_requests)
        except Exception:
            print('Exception: onenessboutique_com')
            await user.send('Exception: onenessboutique_com')
        try:
            await onenessboutique_com(bot, search_requests)
        except Exception:
            print('Exception: onenessboutique_com')
            await user.send('Exception: onenessboutique_com')
        try:
            await shop_exclucitylife_com(bot, search_requests)
        except Exception:
            print('Exception: shop_exclucitylife_com')
            await user.send('Exception: shop_exclucitylife_com')
        try:
            await saintalfred_com(bot, search_requests)
        except Exception:
            print('Exception: saintalfred_com')
            await user.send('Exception: saintalfred_com')
        try:
            await undefeated_com(bot, search_requests)
        except Exception:
            print('Exception: undefeated_com')
            await user.send('Exception: undefeated_com')
        
        #  50
        
        try:
            await kith_com(bot, search_requests)
        except Exception:
            print('Exception: kith_com')
            await user.send('Exception: kith_com')
        try:
            await deadstock_ca(bot, search_requests)
        except Exception:
            print('Exception: deadstock_ca')
            await user.send('Exception: deadstock_ca')
        try:
            await bluetilelounge_ca(bot, search_requests)
        except Exception:
            print('Exception: bluetilelounge_ca')
            await user.send('Exception: bluetilelounge_ca')
        try:
            await hanon_shop_com(bot, search_requests)
        except Exception:
            print('Exception: hanon_shop_com')
            await user.send('Exception: hanon_shop_com')
        try:
            await hannibalstore_it(bot, search_requests)
        except Exception:
            print('Exception: hannibalstore_it')
            await user.send('Exception: hannibalstore_it')
        '''
        #try:
        await brandshop_ru(bot, search_requests)
        #except Exception:
         #   print('Exception: brandshop_ru')
          #  await user.send('Exception: brandshop_ru')
        '''
        try:
            await sneakerhead_ru(bot, search_requests)
        except Exception:
            print('Exception: sneakerhead_ru')
            await user.send('Exception: sneakerhead_ru')
        try:
            await slamjam_com(bot, search_requests)
        except Exception:
            print('Exception: slamjam_com')
            await user.send('Exception: slamjam_com')
        try:
            await tres_bien_com(bot, search_requests)
        except Exception:
            print('Exception: tres_bien_com')
            await user.send('Exception: tres_bien_com')
        try:
            await urbanjunglestore_com(bot, search_requests)
        except Exception:
            print('Exception: urbanjunglestore_com')
            await user.send('Exception: urbanjunglestore_com')
        '''
        #  60
        print('Result: ', time.time() - cur)


def compare(request, search_result):
    request = request.lower()
    search_result = search_result.lower()
    search_result = search_result.replace(' ', '')
    search_result = search_result.replace('-', '')
    search_result = search_result.replace('\n', '')
    keywords = request.split(' ')

    access = True
    for k in keywords:
        if k not in search_result:
            access = False

    return access


async def get_html(url):
    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session:
        async with session.request('get', url) as responce:
            return await responce.content.read()


async def hypedc_com(bot, search_requests):
    html = await get_html('https://www.hypedc.com/new-arrivals?dir=desc&order=news_from_date')
    bs = BeautifulSoup(html, 'lxml')
    items = bs.find_all('product-block', {'class': 'item'}, limit=10)
    print(len(items))

    if len(items) > 10:
        items = items[:10]

    for sr in search_requests:
        for item in items:
            brand_name = item.findChildren('span', {'class': 'brand-name'})
            product_name = item.findChildren('h5', {'class': 'product-name h4'})
            item_name = brand_name[0].text + ' ' + product_name[0].text

            if not compare(sr.request, item_name):
                continue

            item_url_el = item.findChildren('a')[0]
            item_url = item_url_el['href']

            if await ItemsShowedDbManager.exist(item_url, sr.id, loop):
                continue

            item_info = json.loads(item_url_el['data-product'])
            item_sizes = json.loads(item_url_el['data-sizechart'])

            text = tp.hypedc_com_text(item_info, item_sizes, item_url)

            await ItemsShowedDbManager.add(item_name, item_url, sr.id, loop)

            channel_id = int(sr.channel_id)
            await bot.get_channel(channel_id).send(text)
            print(item_url)


async def subtypestore_com(bot, search_requests):
    html = await get_html('https://www.subtypestore.com/categories/latest-sneaker-releases?sort=dateDesc&pages=5')
    bs = BeautifulSoup(html, 'lxml')
    items = bs.find_all('a', {'class': 'link block relative w-full h-full overflow-hidden'}, limit=10)
    print(len(items))

    if len(items) > 10:
        items = items[:10]

    for sr in search_requests:
        for item in items:
            item_name = item.findChildren('h3', {'class': 'mb-2 font-bold'})[0].text

            if not compare(sr.request, item_name):
                continue

            item_url = 'https://www.subtypestore.com' + item['href']

            if await ItemsShowedDbManager.exist(item_url, sr.id, loop):
                continue

            product_page = await get_html(item_url)
            bs = BeautifulSoup(product_page, 'lxml')

            price = bs.find('p', {'class': 'mt-8 text-center cols:text-left'})
            item_sizes = bs.find_all(lambda tag: tag.name == 'span' and tag.has_attr('data-v-3a6c81cc') and not tag.has_attr('class'))

            text = tp.subtypestore_com_text(item_url, item_name, item_sizes, price.text)

            await ItemsShowedDbManager.add(item_name, item_url, sr.id, loop)

            channel_id = int(sr.channel_id)
            await bot.get_channel(channel_id).send(text)
            print(item_url)


async def lockwood_avenue_com(bot, search_requests):
    html = await get_html(
        'https://www.lockwood-avenue.com/en/latest/?mode=grid&limit=100&sort=default&max=700&min=0&sort=newest&brand=0')
    bs = BeautifulSoup(html, 'lxml')
    items = bs.find_all('div', {'class': 'center info'}, limit=10)
    print(len(items))

    for sr in search_requests:
        for item in items:
            item_info = item.findChildren('a')[0]
            item_name = item_info['title']

            if not compare(sr.request, item_name):
                continue

            item_url = item_info['href']

            if await ItemsShowedDbManager.exist(item_url, sr.id, loop):
                continue

            price = item.findChildren('p')[0].text

            product_page = await get_html(item_url)
            bs = BeautifulSoup(product_page, 'lxml')

            sizes = bs.find_all('a', {'title': 'In stock'})

            text = tp.lockwood_avenue_com_text(item_url, item_name, sizes, price)

            await ItemsShowedDbManager.add(item_name, item_url, sr.id, loop)

            channel_id = int(sr.channel_id)
            await bot.get_channel(channel_id).send(text)
            print(item_url)


async def footshop_eu(bot, search_requests):
    html = await get_html('https://www.footshop.eu/en/1551-latest/categories-mens_shoes/gender-male/location-available_online/orderby-activated_at/orderway-desc')
    bs = BeautifulSoup(html, 'lxml')
    items = bs.find_all('a', {'class': 'Product_text_2vcbK'}, limit=10)
    print(len(items))

    for sr in search_requests:
        for item in items:
            item_url = item['href']
            item_name = item.findChildren('h4', {'class': 'Product_name_3eWGG'})[0].text
            item_price = item.findChildren('strong', {'itemprop': 'price'})[0]
            item_price = item_price['content'] + ' €'

            if not compare(sr.request, item_name):
                continue

            if await ItemsShowedDbManager.exist(item_url, sr.id, loop):
                continue

            text = tp.common_text(item_url, item_name, item_price)

            await ItemsShowedDbManager.add(item_name, item_url, sr.id, loop)

            channel_id = int(sr.channel_id)
            await bot.get_channel(channel_id).send(text)
            print(item_url)


async def footshop_com(bot, search_requests):
    html = await get_html('https://www.footshop.com/en/1551-latest/categories-mens_shoes/gender-male/location-available_online/orderby-activated_at/orderway-desc')
    bs = BeautifulSoup(html, 'lxml')
    items = bs.find_all('a', {'class': 'Product_text_2vcbK'}, limit=10)
    print(len(items))

    for sr in search_requests:
        for item in items:
            item_url = item['href']
            item_name = item.findChildren('h4', {'class': 'Product_name_3eWGG'})[0].text
            item_price = item.findChildren('strong', {'itemprop': 'price'})[0]
            item_price = item_price['content'] + ' €'

            if not compare(sr.request, item_name):
                continue

            if await ItemsShowedDbManager.exist(item_url, sr.id, loop):
                continue

            text = tp.common_text(item_url, item_name, item_price)

            await ItemsShowedDbManager.add(item_name, item_url, sr.id, loop)

            channel_id = int(sr.channel_id)
            await bot.get_channel(channel_id).send(text)
            print(text)
            print(item_url)


#  FAIL
async def norsestore_com(bot, search_requests):
    html = await get_html('https://www.norsestore.com/section/mens#category%5B%5D=boots&category%5B%5D=sandals&category%5B%5D=casual_shoes&category%5B%5D=shoes&category%5B%5D=sneakers')
    bs = BeautifulSoup(html, 'lxml')
    print(html)
    items = bs.find_all('span', {'class': 'list-commodity-container'})
    print(len(items))


#  FAIL
async def nakedcph_com(bot, search_requests):
    html = await get_html('https://www.nakedcph.com/en/6/new-arrivals')
    bs = BeautifulSoup(html, 'lxml')
    print(html)
    items = bs.find_all('div', {'class': 'col-6 col-md-3 mb-5'})
    print(len(items))


async def rezetstore_dk(bot, search_requests):
    html = await get_html('https://rezetstore.dk/en/sneakers')
    bs = BeautifulSoup(html, 'lxml')
    items = bs.find_all('a', {'class': 'ProductTeaser__link'}, limit=10)
    print(len(items))

    for sr in search_requests:
        for item in items:
            item_url = 'https://rezetstore.dk' + item['href']
            brand = item.findChildren('p', {'class': 'ProductTeaser__brand'})[0].text
            name = item.findChildren('h3', {'class': 'ProductTeaser__title HeadingProxy HeadingProxy--h3'})[0].text
            item_name = brand + name
            item_price = item.findChildren('div', {'class': 'ProductPricesRegular'})
            if len(item_price) == 0:
                item_price = item.findChildren('p', {'class': 'ProductPriceItem ProductPriceItem--product ProductPriceItem--campaign'})
            item_price = item_price[0].text
            item_sizes = item.findChildren('span', {'class': 'ProductTeaserSizes__list-item'})

            if not compare(sr.request, item_name):
                continue

            if await ItemsShowedDbManager.exist(item_url, sr.id, loop):
                continue

            text = tp.rezetstore_dk_text(item_url, item_name, item_sizes, item_price)

            await ItemsShowedDbManager.add(item_name, item_url, sr.id, loop)

            channel_id = int(sr.channel_id)
            await bot.get_channel(channel_id).send(text)


async def stormfashion_dk(bot, search_requests):
    html = await get_html('https://stormfashion.dk/new')
    bs = BeautifulSoup(html, 'lxml')
    items = bs.find_all('li', {'class': 'storm-item'}, limit=10)
    print(len(items))

    for sr in search_requests:
        for item in items:
            item_url = 'https://stormfashion.dk/' + item.findChildren('a')[0]['href']
            item_name = item_url.split('/')[-1]
            item_name = item_name.split('-')
            item_name = item_name[-1:] + item_name[:-1]
            text = ''
            for i in item_name:
                text += i
            item_lower_case = text

            if not compare(sr.request, item_lower_case):
                continue

            if await ItemsShowedDbManager.exist(item_url, sr.id, loop):
                continue

            product_page = await get_html(item_url)

            bs = BeautifulSoup(product_page, 'lxml')

            item_name = bs.find('h1', {'itemprop': 'name'}).text
            price = bs.find('span', {'itemprop': 'price'}).text

            text = tp.stormfashion_dk_text(item_url, item_name, price)

            await ItemsShowedDbManager.add(item_name, item_url, sr.id, loop)

            channel_id = int(sr.channel_id)
            await bot.get_channel(channel_id).send(text)
            print(item_url)


async def stoy_com(bot, search_requests):
    html = await get_html('https://stoy.com/en/men/footwear')
    bs = BeautifulSoup(html, 'lxml')
    items = bs.find_all('div', {'class': 'item product-item product'}, limit=10)
    print(len(items))

    for sr in search_requests:
        for item in items:
            item_url = item.findChildren('a')[0]['href']
            brand = item.findChildren('div', {'class': 'brand'})[0].text
            name = item.findChildren('div', {'class': 'name'})[0].text
            item_name = brand + name
            item_price = item.findChildren('span', {'class': 'price'})[0].text

            if not compare(sr.request, item_name):
                continue

            if await ItemsShowedDbManager.exist(item_url, sr.id, loop):
                continue

            text = tp.common_text(item_url, item_name, item_price)

            await ItemsShowedDbManager.add(item_name, item_url, sr.id, loop)

            channel_id = int(sr.channel_id)
            await bot.get_channel(channel_id).send(text)
            print(item_url)


async def dev_thegoodlifespace_com(bot, search_requests):
    html = await get_html('http://dev.thegoodlifespace.com/latest-arrivals/all-latest/footwear-men.html')
    bs = BeautifulSoup(html, 'lxml')
    items = bs.find_all('div', {'class': 'product details product-item-details'}, limit=10)
    print(len(items))

    for sr in search_requests:
        for item in items:
            item_url = item.findChildren('a', {'class': 'product-item-link'})[0]['href']
            brand = item.findChildren('p')[0].text
            name = item.findChildren('a', {'class': 'product-item-link'})[0].text
            item_name = brand + name
            item_price = item.findChildren('span', {'class': 'price'})
            if len(item_price) == 0:
                item_price = 'Sold out'
            else:
                item_price = item_price[0].text

            if not compare(sr.request, item_name):
                continue

            if await ItemsShowedDbManager.exist(item_url, sr.id, loop):
                continue

            text = tp.common_text(item_url, item_name, item_price)

            await ItemsShowedDbManager.add(item_name, item_url, sr.id, loop)

            channel_id = int(sr.channel_id)
            await bot.get_channel(channel_id).send(text)
            print(item_url)


async def basket4ballers_com(bot, search_requests):
    html = await get_html('https://www.basket4ballers.com/en/152-shoes')
    bs = BeautifulSoup(html, 'lxml')
    items = bs.find_all('a', {'class': 'block-product__link product_img_link'}, limit=10)
    print(len(items))

    for sr in search_requests:
        for item in items:
            item_url = item['href']
            item_name = item.findChildren('h2', {'class': 'block-product__name'})[0].text
            sizes = item.findChildren('li', {'class': 'block-product__attributes-item'})
            item_price = item.findChildren('span', {'class': 'block-product__price'})[0].text
            item_price = item_price[:-4]

            if not compare(sr.request, item_name):
                continue

            if await ItemsShowedDbManager.exist(item_url, sr.id, loop):
                continue

            text = tp.basket4ballers_com(item_url, item_name, sizes, item_price)

            await ItemsShowedDbManager.add(item_name, item_url, sr.id, loop)

            channel_id = int(sr.channel_id)
            await bot.get_channel(channel_id).send(text)
            print(item_url)


async def bouncewear_com(bot, search_requests):
    html = await get_html('https://bouncewear.com/en/category/schoenen')
    bs = BeautifulSoup(html, 'lxml')
    items = bs.find_all('div', {'class': 'product'}, limit=10)
    print(len(items))

    for sr in search_requests:
        for item in items:
            item_url = item.findChildren('a')[0]['href']
            item_name = item.findChildren('p', {'class': 'product__name'})[0].text
            item_price = item.findChildren('p', {'class': 'product__price'})[0].text

            if not compare(sr.request, item_name):
                continue

            if await ItemsShowedDbManager.exist(item_url, sr.id, loop):
                continue

            product_page = await get_html(item_url)
            bs = BeautifulSoup(product_page, 'lxml')

            sizes = bs.find_all('div', {'class': 'multi-select-list-wrapper'})[0]
            sizes = sizes.findChildren('label', {'class': 'checkbox__label'})

            text = tp.bouncewear_com_text(item_url, item_name, sizes, item_price)
            await ItemsShowedDbManager.add(item_name, item_url, sr.id, loop)

            channel_id = int(sr.channel_id)
            await bot.get_channel(channel_id).send(text)
            print(item_url)


#  FAIL
async def caliroots_com(bot, search_requests):
    html = await get_html('https://caliroots.com/latest-products/s/20')
    print(html)
    bs = BeautifulSoup(html, 'lxml')
    items = bs.find_all('li', {'class': 'product c-2'})
    print(len(items))


async def chezvibe_com(bot, search_requests):
    html = await get_html('https://www.chezvibe.com/en/new-products')
    bs = BeautifulSoup(html, 'lxml')
    items = bs.find_all('div', {'class': 'product-container'}, limit=10)
    print(len(items))

    for sr in search_requests:
        for item in items:
            item_url = item.findChildren('a', {'class': 'product_img_link'})[0]['href']
            brand = item.findChildren('h5', {'id': 'manufacturer'})[0].text
            name = item.findChildren('a', {'class': 'product-name'})[0].text
            item_name = brand + name
            item_price = item.findChildren('span', {'class': 'price product-price'})[0].text

            if not compare(sr.request, item_name):
                continue

            if await ItemsShowedDbManager.exist(item_url, sr.id, loop):
                continue

            product_page = await get_html(item_url)
            bs = BeautifulSoup(product_page, 'lxml')

            sizes = bs.find_all('select', {'class': 'form-control attribute_select no-print'})[0]
            sizes = sizes.findChildren()

            text = tp.chezvibe_com_text(item_url, item_name, sizes, item_price)

            await ItemsShowedDbManager.add(item_name, item_url, sr.id, loop)

            channel_id = int(sr.channel_id)
            await bot.get_channel(channel_id).send(text)
            print(item_url)


#  FAIL
async def footlocker_fr(bot, search_requests):
    html = await get_html('https://www.footlocker.fr')
    bs = BeautifulSoup(html, 'lxml')
    items = bs.find_all('button', {'class': 'fl-product-size--item'})
    print(len(items))


async def galerieslafayette_com(bot, search_requests):
    html = await get_html('https://www.galerieslafayette.com/c/nouveautes/ct/homme-chaussures/tri/nouveautes')
    bs = BeautifulSoup(html, 'lxml')
    items = bs.find_all('li', {'class': 'pdt-cell pdt-cell-with-hover js-pdt-cell'}, limit=10)
    print(len(items))

    for sr in search_requests:
        for item in items:
            item_url = 'https://www.galerieslafayette.com/' +  item.findChildren('a', {'class': 'js-pdt-link'})[0]['href']
            brand = item.findChildren('strong', {'class': 'pdt-brand bold-large-title-marque one'})[0].text
            name = item.findChildren('span', {'class': 'pdt-name three'})[0].text
            item_name = brand + ' ' + name

            if not compare(sr.request, item_name):
                continue

            if await ItemsShowedDbManager.exist(item_url, sr.id, loop):
                continue

            product_page = await get_html(item_url)
            bs = BeautifulSoup(product_page, 'lxml')

            item_price = bs.find('span', {'class': 'price__current'}).text
            sizes = bs.find_all('select', {'class': 'sizeBlock__select sizeBlock__select--size'})[0]
            sizes = sizes.findChildren()

            text = tp.galerieslafayette_com_text(item_url, item_name, sizes, item_price)

            await ItemsShowedDbManager.add(item_name, item_url, sr.id, loop)

            channel_id = int(sr.channel_id)
            await bot.get_channel(channel_id).send(text)
            print(item_url)


async def hubbastille_com(bot, search_requests):
    html = await get_html('http://hubbastille.com/en/19-les-nouveautes')
    bs = BeautifulSoup(html, 'lxml')
    items = bs.find_all('div', {'class': 'mix cs-item'}, limit=10)
    print(len(items))

    for sr in search_requests:
        for item in items:
            item_url = item.findChildren('a', {'class': 'product-name'})[0]['href']
            item_price = item.findChildren('span', {'class': 'price product-price'})[0].text
            item_price = item_price.replace('\t', '')
            item_price = item_price.replace('\n', '')
            item_name = item.findChildren('a', {'class': 'product-name'})[0].text
            item_name = item_name.replace('\t', '')
            item_name = item_name.replace('\n', '')

            if not compare(sr.request, item_name):
                continue

            if await ItemsShowedDbManager.exist(item_url, sr.id, loop):
                continue

            product_page = await get_html(item_url)
            bs = BeautifulSoup(product_page, 'lxml')

            sizes = bs.find_all('select', {'class': 'form-control attribute_select no-print'})[0]
            sizes = sizes.findChildren()

            text = tp.galerieslafayette_com_text(item_url, item_name, sizes, item_price)

            await ItemsShowedDbManager.add(item_name, item_url, sr.id, loop)

            channel_id = int(sr.channel_id)
            await bot.get_channel(channel_id).send(text)
            print(item_url)


#  FAIL
async def jdsports_fr(bot, search_requests):
    html = await get_html('https://www.jdsports.fr/homme/chaussures-homme/?facet-new=latest')
    bs = BeautifulSoup(html, 'lxml')
    print(html)
    items = bs.find_all('li', {'class': 'productListItem'})
    print(len(items))


async def impact_premium_com(bot, search_requests):
    html = await get_html('https://www.impact-premium.com/fr/nouveaux-produits?n=60')
    bs = BeautifulSoup(html, 'lxml')
    items = bs.find_all('div', {'class': 'product-container'}, limit=10)
    print(len(items))

    for sr in search_requests:
        for item in items:
            item_url = item.findChildren('a', {'class': 'product_img_link'})[0]['href']
            item_price = item.findChildren('span', {'class': 'price product-price'})[0].text
            item_name = item.findChildren('a', {'class': 'product-name'})[0].text
            item_name = item_name.replace(':', '')

            if not compare(sr.request, item_name):
                continue

            if await ItemsShowedDbManager.exist(item_url, sr.id, loop):
                continue

            product_page = await get_html(item_url)
            bs = BeautifulSoup(product_page, 'lxml')

            sizes = bs.find_all('select', {'class': 'form-control attribute_select no-print'})[0]
            sizes = sizes.findChildren()

            text = tp.galerieslafayette_com_text(item_url, item_name, sizes, item_price)

            await ItemsShowedDbManager.add(item_name, item_url, sr.id, loop)

            channel_id = int(sr.channel_id)
            await bot.get_channel(channel_id).send(text)
            print(item_url)


#  FAIL
async def lebuzzsneakershop_com(bot, search_requests):
    html = await get_html('https://www.lebuzzsneakershop.com/en/collection/footwear.html')
    bs = BeautifulSoup(html, 'lxml')
    print(html)
    items = bs.find_all('li', {'class': 'item product product-item'})
    print(len(items))


async def lerayonfrais_fr(bot, search_requests):
    html = await get_html('https://lerayonfrais.fr/fr/30-nouveaut%C3%A9s')
    bs = BeautifulSoup(html, 'lxml')
    items = bs.find_all('div', {'class': 'listing block'}, limit=10)
    print(len(items))

    for sr in search_requests:
        for item in items:
            url = item.findChildren('a')[0]
            item_url = url['href']
            name = url['title']
            brand = item.findChildren('a', {'class': 'brand'})[0].text

            try:
                item_price = item.findChildren('div', {'class': 'price_no_discount'})[0].text
            except Exception:
                item_price = 'SOLD OUT'

            item_name = brand + ' ' + name

            if not compare(sr.request, item_name):
                continue

            if await ItemsShowedDbManager.exist(item_url, sr.id, loop):
                continue

            product_page = await get_html(item_url)
            bs = BeautifulSoup(product_page, 'lxml')

            sizes = bs.find_all('a', {'title': 'Available'})
            print(len(sizes))

            text = tp.galerieslafayette_com_text(item_url, item_name, sizes, item_price)

            await ItemsShowedDbManager.add(item_name, item_url, sr.id, loop)

            channel_id = int(sr.channel_id)
            await bot.get_channel(channel_id).send(text)
            print(item_url)


#  FAIL
async def milk_store_com(bot, search_requests):
    html = await get_html('https://www.milk-store.com/nouveaux-produits')
    bs = BeautifulSoup(html, 'lxml')
    print(html)
    items = bs.find_all('div', {'class': 'product-container'})
    print(len(items))


async def opiumparis_com(bot, search_requests):
    html = await get_html('https://www.opiumparis.com/en/16-new-arrivals')
    bs = BeautifulSoup(html, 'lxml')
    items = bs.find_all('div', {'class': 'thumbnail-container ta-c'}, limit=10)
    print(len(items))

    for sr in search_requests:
        for item in items:
            item_url = item.findChildren('a', {'class': 'thumbnail product-thumbnail'})[0]['href']
            name = item.findChildren('h1', {'class': 'product-title title-sm mb-xs'})[0].text
            brand = item.findChildren('p', {'class': 'product-manufacturer'})[0].text
            item_price = item.findChildren('div', {'class': 'price'})[0].text
            item_name = brand + ' ' + name
            item_name = item_name.replace('\t', '')
            item_name = item_name.replace('\n', '')
            sizes = item.findChildren('ul', {'class': 'list-sizes'})[0]
            sizes = sizes.findChildren()

            if not compare(sr.request, item_name):
                continue

            if await ItemsShowedDbManager.exist(item_url, sr.id, loop):
                continue

            text = tp.galerieslafayette_com_text(item_url, item_name, sizes, item_price)

            await ItemsShowedDbManager.add(item_name, item_url, sr.id, loop)

            channel_id = int(sr.channel_id)
            await bot.get_channel(channel_id).send(text)
            print(item_url)


async def shinzo_paris(bot, search_requests):
    try:
        html = await get_html('https://www.shinzo.paris/fr/63-nouveautes#/genre-homme')
    except Exception:
        print('shinzo.paris exception')
        return
    bs = BeautifulSoup(html, 'lxml')
    items = bs.find_all('div', {'class': 'product-inner'}, limit=10)
    print(len(items))

    for sr in search_requests:
        for item in items:
            url = item.findChildren('a', {'class': 'link-declinaison-product'})[0]
            item_url = url['href']
            item_name = url['title']
            item_price = item.findChildren('span', {'class': 'price product-price'})[0].text

            if not compare(sr.request, item_name):
                continue

            if await ItemsShowedDbManager.exist(item_url, sr.id, loop):
                continue

            product_page = await get_html(item_url)
            bs = BeautifulSoup(product_page, 'lxml')

            try:
                sizes = bs.find_all('fieldset', {'class': 'attribute_fieldset sizes-fieldset'})[0]
                sizes = sizes.findChildren('ul')[0]
                sizes = sizes.findChildren()
            except IndexError:
                sizes = []

            text = tp.galerieslafayette_com_text(item_url, item_name, sizes, item_price)
            print(text)
            await ItemsShowedDbManager.add(item_name, item_url, sr.id, loop)

            channel_id = int(sr.channel_id)
            await bot.get_channel(channel_id).send(text)
            print(item_url)


async def shoezgallery_com(bot, search_requests):
    html = await get_html('https://www.shoezgallery.com/en/32-latest#')
    bs = BeautifulSoup(html, 'lxml')
    items = bs.find_all('div', {'class': 'product-block'}, limit=10)
    print(len(items))

    for sr in search_requests:
        for item in items:
            item_url = item.findChildren('a', {'class': 'product_img_link'})[0]['href']
            brand = item.findChildren('span', {'itemprop': 'brand'})[0].text
            name = item.findChildren('span', {'itemprop': 'name'})[0].text
            item_name = brand + ' ' + name
            item_price = item.findChildren('span', {'class': 'price product-price'})[0].text
            size = item.findChildren('span', {'class': 'product-combinations position-absolute text-center py-2 w-100'})[0]
            sizes = size.findChildren()

            if not compare(sr.request, item_name):
                continue

            if await ItemsShowedDbManager.exist(item_url, sr.id, loop):
                continue

            text = tp.galerieslafayette_com_text(item_url, item_name, sizes, item_price)

            await ItemsShowedDbManager.add(item_name, item_url, sr.id, loop)

            channel_id = int(sr.channel_id)
            await bot.get_channel(channel_id).send(text)
            print(item_url)


#  FAIL
async def sizeofficial_fr(bot, search_requests):
    html = await get_html('https://www.sizeofficial.fr/homme/chaussures/latest/')
    print(html)
    bs = BeautifulSoup(html, 'lxml')
    items = bs.find_all('li', {'class': 'productListItem'})
    print(len(items))


async def snkrs_com(bot, search_requests):
    html = await get_html('https://www.snkrs.com/en/166-new')
    bs = BeautifulSoup(html, 'lxml')
    items = bs.find_all('div', {'class': 'product-container'}, limit=10)
    print(len(items))

    for sr in search_requests:
        for item in items:
            item_url = item.findChildren('a', {'class': 'product_img_link'})[0]['href']
            brand = item.findChildren('span', {'class': 'manufacturer'})[0].text
            name = item.findChildren('span', {'class': 'product-name'})[0].text
            item_name = brand + ' ' + name
            item_price = item.findChildren('span', {'class': 'price product-price'})[0].text

            if not compare(sr.request, item_name):
                continue

            if await ItemsShowedDbManager.exist(item_url, sr.id, loop):
                continue

            product_page = await get_html(item_url)
            bs = BeautifulSoup(product_page, 'lxml')

            sizes = bs.find_all('span', {'class': 'size_EU'})

            text = tp.galerieslafayette_com_text(item_url, item_name, sizes, item_price)

            await ItemsShowedDbManager.add(item_name, item_url, sr.id, loop)

            channel_id = int(sr.channel_id)
            await bot.get_channel(channel_id).send(text)
            print(item_url)


async def thenextdoor_fr(bot, search_requests):
    html = await get_html('https://thenextdoor.fr/collections/nouveautes/categorie_basket?sort_by=created-descending')
    bs = BeautifulSoup(html, 'lxml')
    items = bs.find_all('div', {'class': 'grid-view-item product-card'}, limit=10)
    print(len(items))

    for sr in search_requests:
        for item in items:
            item_url = 'https://thenextdoor.fr/' + item.findChildren('a', {'class': 'grid-view-item__link grid-view-item__image-container full-width-link'})[0]['href']
            brand = item.findChildren('div', {'class': 'grid-view-item__vendor'})[0].text
            name = item.findChildren('div', {'class': 'h4 grid-view-item__title product-card__title'})[0].text
            item_name = brand + ' ' + name
            item_name = item_name.replace('\n', '')
            item_name = item_name.replace('\t', '')
            item_price = item.findChildren('span', {'class': 'money'})[0].text

            if not compare(sr.request, item_name):
                continue

            if await ItemsShowedDbManager.exist(item_url, sr.id, loop):
                continue

            product_page = await get_html(item_url)
            bs = BeautifulSoup(product_page, 'lxml')

            sizes = bs.find_all('input', {'class': 'single-option-selector single-option-selector-product-template product-form__input'})

            text = tp.thenextdoor_fr_text(item_url, item_name, sizes, item_price)

            await ItemsShowedDbManager.add(item_name, item_url, sr.id, loop)

            channel_id = int(sr.channel_id)
            await bot.get_channel(channel_id).send(text)
            print(item_url)


async def the_broken_arm_com(bot, search_requests):
    html = await get_html('https://www.the-broken-arm.com/en/57-sneakers')
    bs = BeautifulSoup(html, 'lxml')
    items = bs.find_all('div', {'class': 'product-container'}, limit=10)
    print(len(items))

    for sr in search_requests:
        for item in items:
            item_url = item.findChildren('a', {'class': 'product_img_link'})[0]['href']
            item_name = item.findChildren('a', {'class': 'product-name'})[0]['title']

            if not compare(sr.request, item_name):
                continue

            if await ItemsShowedDbManager.exist(item_url, sr.id, loop):
                continue

            product_page = await get_html(item_url)
            bs = BeautifulSoup(product_page, 'lxml')

            item_price = item.findChildren('span', {'itemprop': 'price'})[0].text
            sizes = bs.find_all('select', {'name': 'group_2'})[0]
            sizes = sizes.findChildren()

            text = tp.the_broken_arm_com_tex(item_url, item_name, sizes, item_price)

            await ItemsShowedDbManager.add(item_name, item_url, sr.id, loop)

            channel_id = int(sr.channel_id)
            await bot.get_channel(channel_id).send(text)
            print(item_url)


async def zalando_fr(bot, search_requests):
    html = await get_html('https://www.zalando.fr/baskets-homme/?activation_date=0-7&order=activation_date')
    bs = BeautifulSoup(html, 'lxml')
    items = bs.find_all('div', {'class': 'cat_cardWrap-2UHT7'}, limit=10)
    print(len(items))

    for sr in search_requests:
        for item in items:
            item_url = 'https://www.zalando.fr/' + item.findChildren('a', {'class': 'cat_imageLink-OPGGa'})[0]['href']
            item_price = item.findChildren('div', {'class': 'cat_originalPrice-2Oy4G'})[0].text
            brand = item.findChildren('div', {'class': 'cat_brandName-2XZRz cat_ellipsis-MujnT'})[0].text
            name = item.findChildren('div', {'class': 'cat_articleName--arFp cat_ellipsis-MujnT'})[0].text
            item_name = brand + ' ' + name

            if not compare(sr.request, item_name):
                continue

            if await ItemsShowedDbManager.exist(item_url, sr.id, loop):
                continue

            text = tp.common_text(item_url, item_name, item_price)
            print(text)
            await ItemsShowedDbManager.add(item_name, item_url, sr.id, loop)

            channel_id = int(sr.channel_id)
            await bot.get_channel(channel_id).send(text)
            print(item_url)


async def einhalb_com(bot, search_requests):
    html = await get_html('https://www.43einhalb.com/en/sneaker/page/1/sort/date_new/perpage/36')
    bs = BeautifulSoup(html, 'lxml')
    items = bs.find_all('div', {'class': 'itemWrapper pOverlay'}, limit=10)
    print(len(items))

    for sr in search_requests:
        for item in items:
            item_url = 'https://www.43einhalb.com/' + item.findChildren('a', {'class': 'plink image'})[0]['href']
            item_price = item.findChildren('span', {'class': 'pPrice'})[0].text
            item_price = item_price.replace('\t', '')
            item_price = item_price.replace('\n', '')
            item_price = item_price.replace(' ', '')
            brand = item.findChildren('span', {'class': 'producerName'})[0].text
            name = item.findChildren('span', {'class': 'productName'})[0].text
            item_name = brand + ' ' + name
            sizes = bs.find_all('ul', {'class': 'availableVariants'})[0]
            sizes = sizes.findChildren('a')

            if not compare(sr.request, item_name):
                continue

            if await ItemsShowedDbManager.exist(item_url, sr.id, loop):
                continue

            text = tp.the_broken_arm_com_tex(item_url, item_name, sizes, item_price)

            await ItemsShowedDbManager.add(item_name, item_url, sr.id, loop)

            channel_id = int(sr.channel_id)
            await bot.get_channel(channel_id).send(text)
            print(item_url)


#  FAIL
async def afew_store_com(bot, search_requests):
    html = await get_html('https://www.afew-store.com/en/sneaker/')
    bs = BeautifulSoup(html, 'lxml')
    items = bs.find_all('a', {'class': 'findify-components--cards--product'})
    print(len(items))


async def asphaltgold_com(bot, search_requests):
    html = await get_html('https://www.asphaltgold.com/de/category/men/sneaker/new/')
    bs = BeautifulSoup(html, 'lxml')
    items = bs.find_all('a', {'class': 'product-url'}, limit=10)
    print(len(items))

    for sr in search_requests:
        for item in items:
            item_url = 'https://www.asphaltgold.com/' + item['href']
            brand = item.findChildren('div', {'class': 'product-brand ng-star-inserted'})[0].text
            name = item.findChildren('div', {'class': 'product-name'})[0].text
            item_name = brand + ' ' + name
            item_price = item.findChildren('div', {'class': 'price'})[0].text
            item_price = item_price.replace(' ', '')

            if not compare(sr.request, item_name):
                continue

            if await ItemsShowedDbManager.exist(item_url, sr.id, loop):
                continue

            text = tp.common_text(item_url, item_name, item_price)

            await ItemsShowedDbManager.add(item_name, item_url, sr.id, loop)

            channel_id = int(sr.channel_id)
            await bot.get_channel(channel_id).send(text)
            print(item_url)


async def allikestore_com(bot, search_requests):
    html = await get_html('https://www.allikestore.com/default/sneakers/mens-sneakers.html#page=1')
    bs = BeautifulSoup(html, 'lxml')
    items = bs.find_all('li', {'class': 'item'}, limit=10)
    print(len(items))

    for sr in search_requests:
        for item in items:
            url = item.findChildren('a', {'class': 'product-image'})[0]
            item_url = url['href']
            item_name = url['title']
            item_price = item.findChildren('span', {'class': 'regular-price'})[0].text
            sizes = item.findChildren('div', {'class': 'available-sizes'})[0].text

            if 'Sizes Available' not in sizes:
                sizes = ''

            if not compare(sr.request, item_name):
                continue

            if await ItemsShowedDbManager.exist(item_url, sr.id, loop):
                continue

            text = tp.allikestore_com_text(item_url, item_name, sizes, item_price)

            await ItemsShowedDbManager.add(item_name, item_url, sr.id, loop)

            channel_id = int(sr.channel_id)
            await bot.get_channel(channel_id).send(text)
            print(item_url)


#  FAIL
async def bstn_com(bot, search_requests):
    html = await get_html('https://www.bstn.com/en/new-arrivals/filter/__category_footwear/page/1/sort/date_new')
    bs = BeautifulSoup(html, 'lxml')
    print(html)
    items = bs.find_all('li', {'class': 'item'})
    print(len(items))


async def kickz_com(bot, search_requests):
    html = await get_html('https://www.kickz.com/de/shop/herrenschuhe')
    bs = BeautifulSoup(html, 'lxml')
    items = bs.find_all('div', {'class': 'categoryContent'})[0]
    items = items.findChildren(recursive=False)

    if len(items) > 10:
        items = items[:10]

    print(len(items))

    for sr in search_requests:
        for item in items:
            item_url = item.findChildren('button', {'class': 'btn ref_link'})[0]['href']
            brand = item.findChildren('span', {'class': 'categoryElementHeadlineContent'})[0].text
            name = item.findChildren('div', {'class': 'catalogItemName'})[0].text
            item_name = brand + ' ' + name
            item_price = item.findChildren('span', {'class': 'price'})[0].text
            sizes = item.findChildren('ul', {'class': 'list-group'})[0]
            sizes = sizes.findChildren()

            if not compare(sr.request, item_name):
                continue

            if await ItemsShowedDbManager.exist(item_url, sr.id, loop):
                continue

            text = tp.basket4ballers_com(item_url, item_name, sizes, item_price)

            await ItemsShowedDbManager.add(item_name, item_url, sr.id, loop)

            channel_id = int(sr.channel_id)
            await bot.get_channel(channel_id).send(text)
            print(item_url)


async def kickzpremium_com(bot, search_requests):
    html = await get_html('https://www.kickzpremium.com/de/Maenner/schuhe/c')
    bs = BeautifulSoup(html, 'lxml')
    items = bs.find_all('div', {'class': 'categoryContent'})[0]
    items = items.findChildren(recursive=False)
    print(len(items))

    if len(items) > 10:
        items = items[:10]

    if len(items) > 10:
        items = items[:10]

    for sr in search_requests:
        for item in items:
            item_url = item.findChildren('button', {'class': 'btn ref_link'})[0]['href']
            brand = item.findChildren('span', {'class': 'categoryElementHeadlineContent'})[0].text
            name = item.findChildren('div', {'class': 'catalogItemName'})[0].text
            item_name = brand + ' ' + name
            item_price = item.findChildren('span', {'class': 'price'})[0].text
            sizes = item.findChildren('ul', {'class': 'list-group'})[0]
            sizes = sizes.findChildren()

            if not compare(sr.request, item_name):
                continue

            if await ItemsShowedDbManager.exist(item_url, sr.id, loop):
                continue

            text = tp.basket4ballers_com(item_url, item_name, sizes, item_price)

            await ItemsShowedDbManager.add(item_name, item_url, sr.id, loop)

            channel_id = int(sr.channel_id)
            await bot.get_channel(channel_id).send(text)
            print(item_url)


#  FAIL
async def overkillshop_com(bot, search_requests):
    html = await get_html('https://www.overkillshop.com/en/sneaker/men.html')
    print(html)
    bs = BeautifulSoup(html, 'lxml')
    items = bs.find_all('div', {'class': 'thumbnail'})
    print(len(items))


async def rimowa_com(bot, search_requests):
    html = await get_html('https://www.rimowa.com/de/en/new-colors/')
    bs = BeautifulSoup(html, 'lxml')
    items = bs.find_all('li', {'class': 'grid-tile'}, limit=10)
    print(len(items))

    for sr in search_requests:
        for item in items:
            item_url = item.findChildren('a', {'class': 'product-link js-product-tile-link'})[0]['href']
            item_name = item.findChildren('div', {'class': 'product-name'})[0].text
            item_name = item_name.replace('\n', '')
            item_price = item.findChildren('div', {'class': 'product-pricing'})[0].text
            item_price = item_price.replace('\n', '')

            if not compare(sr.request, item_name):
                continue

            if await ItemsShowedDbManager.exist(item_url, sr.id, loop):
                continue

            text = tp.common_text(item_url, item_name, item_price)

            await ItemsShowedDbManager.add(item_name, item_url, sr.id, loop)

            channel_id = int(sr.channel_id)
            await bot.get_channel(channel_id).send(text)
            print(item_url)


#  FAIL
async def solebox_com(bot, search_requests):
    html = await get_html('https://www.solebox.com/Footwear/?filter=f99:oNew')
    print(html)
    bs = BeautifulSoup(html, 'lxml')
    items = bs.find_all('li', {'class': 'productData'})
    print(len(items))


#  FAIL
async def sotostore_com(bot, search_requests):
    html = await get_html('https://www.sotostore.com/en/2/latest-products?p=337&orderBy=Published')
    print(html)
    bs = BeautifulSoup(html, 'lxml')
    items = bs.find_all('div', {'class': 'card'})
    print(len(items))


async def suppastore_com(bot, search_requests):
    html = await get_html('https://www.suppastore.com/en/latest')
    bs = BeautifulSoup(html, 'lxml')
    items = bs.find_all('div', {'class': 'product-item-info'}, limit=10)
    print(len(items))

    for sr in search_requests:
        for item in items:
            item_url = item.findChildren('a', {'class': 'product photo product-item-photo'})[0]['href']
            brand = item.findChildren('div', {'class': 'manufacturer'})[0].text
            name = item.findChildren('a', {'class': 'product-item-link'})[0].text
            item_name = brand + ' ' + name
            item_name = item_name.replace('\n', '')
            item_price = item.findChildren('span', {'class': 'price-wrapper'})[0]['data-price-amount'] + ' €'

            if not compare(sr.request, item_name):
                continue

            if await ItemsShowedDbManager.exist(item_url, sr.id, loop):
                continue

            text = tp.common_text(item_url, item_name, item_price)

            await ItemsShowedDbManager.add(item_name, item_url, sr.id, loop)

            channel_id = int(sr.channel_id)
            await bot.get_channel(channel_id).send(text)
            print(item_url)


async def vooberlin_com(bot, search_requests):
    html = await get_html('https://www.vooberlin.com/sneakers/new-releases/')
    bs = BeautifulSoup(html, 'lxml')
    items = bs.find_all('div', {'class': 'product--box box--minimal'}, limit=10)
    print(len(items))

    for sr in search_requests:
        for item in items:
            url = item.findChildren('a', {'class': 'product--title'})[0]
            item_url = url['href']
            brand = item.findChildren('span', {'class': 'w_suppliername'})[0].text
            name = url['title']
            item_name = brand + ' ' + name
            item_name = item_name.replace('\n', '')

            try:
                item_price = item.findChildren('div', {'class': 'product--price'})[0].text
                item_price = item_price.replace('\n', '')
            except Exception:
                item_price = ''

            if not compare(sr.request, item_name):
                continue

            if await ItemsShowedDbManager.exist(item_url, sr.id, loop):
                continue

            text = tp.common_text(item_url, item_name, item_price)

            await ItemsShowedDbManager.add(item_name, item_url, sr.id, loop)

            channel_id = int(sr.channel_id)
            await bot.get_channel(channel_id).send(text)
            print(item_url)


async def zupport_de(bot, search_requests):
    html = await get_html('https://zupport.de/skateshoes?p=1')
    bs = BeautifulSoup(html, 'lxml')
    items = bs.find_all('div', {'class': 'product--info'}, limit=10)
    print(len(items))

    for sr in search_requests:
        for item in items:
            url = item.findChildren('a', {'class': 'product--image'})[0]
            item_url = url['href']
            item_name = url['title']
            item_price = item.findChildren('div', {'class': 'product--price'})[0].text
            item_price = item_price.replace('\n', '')
            item_price = item_price.replace(' ', '')
            item_price = item_price.replace('*', '')

            if not compare(sr.request, item_name):
                continue

            if await ItemsShowedDbManager.exist(item_url, sr.id, loop):
                continue

            product_page = await get_html(item_url)
            bs = BeautifulSoup(product_page, 'lxml')

            sizes = bs.find_all('label', {'class': 'option--label'})

            text = tp.the_broken_arm_com_tex(item_url, item_name, sizes, item_price)

            await ItemsShowedDbManager.add(item_name, item_url, sr.id, loop)

            channel_id = int(sr.channel_id)
            await bot.get_channel(channel_id).send(text)
            print(item_url)


async def aw_lab_com(bot, search_requests):
    html = await get_html('https://www.aw-lab.com/shop/uomo/scarpe')
    bs = BeautifulSoup(html, 'lxml')
    items = bs.find_all('div', {'class': 'product-data-container'}, limit=10)
    print(len(items))

    if len(items) > 10:
        items = items[:10]

    for sr in search_requests:
        for item in items:
            item_name = item.findChildren('h2', {'class': 'product-name'})[0].text

            if not compare(sr.request, item_name):
                continue

            item_url = item.findChildren('div', {'class': 'product-detail-link'})[0]
            item_url = item_url.findChildren('a')[0]['href']

            if await ItemsShowedDbManager.exist(item_url, sr.id, loop):
                continue

            item_price = item.findChildren('p', {'class': 'small-price'})[0].text
            item_price = item_price.replace(' ', '')

            text = tp.common_text(item_url, item_name, item_price)

            await ItemsShowedDbManager.add(item_name, item_url, sr.id, loop)

            channel_id = int(sr.channel_id)
            await bot.get_channel(channel_id).send(text)
            print(item_url)


#  FAIL
async def antonioli_eu(bot, search_requests):
    html = await get_html('https://www.antonioli.eu/en/UA/men/t/categories/shoes/sneakers')
    bs = BeautifulSoup(html, 'lxml')
    print(html)
    items = bs.find_all('article', {'class': 'product'})
    print(len(items))


async def back_door_it(bot, search_requests):
    html = await get_html('https://www.back-door.it/product-category/sneakers/#Sneakers')
    bs = BeautifulSoup(html, 'lxml')
    items = bs.find_all('a', {'class': 'product-category product-info'}, limit=10)
    print(len(items))

    if len(items) > 10:
        items = items[:10]

    for sr in search_requests:
        for item in items:
            item_name = item.findChildren('h6', {'itemprop': 'name'})[0].text

            if not compare(sr.request, item_name):
                continue

            item_url = item['href']

            if await ItemsShowedDbManager.exist(item_url, sr.id, loop):
                continue

            item_price = item.findChildren('span', {'class': 'woocommerce-Price-amount amount'})[0].text
            item_price = item_price.replace(' ', '')
            item_price = item_price.replace('\n', '')

            text = tp.common_text(item_url, item_name, item_price)

            await ItemsShowedDbManager.add(item_name, item_url, sr.id, loop)

            channel_id = int(sr.channel_id)
            await bot.get_channel(channel_id).send(text)
            print(item_url)


async def blackboxstore_com(bot, search_requests):
    html = await get_html('https://www.blackboxstore.com/it/sneakers/uomo.html')
    bs = BeautifulSoup(html, 'lxml')
    items = bs.find_all('li', {'class': 'item'}, limit=10)

    print(len(items))

    for sr in search_requests:
        for item in items:
            brand = item.findChildren('span', {'class': 'brand-name'})[0].text
            name = item.findChildren('h2', {'class': 'product-name'})[0].text
            item_name = brand + ' ' + name

            if not compare(sr.request, item_name):
                continue

            item_url = item.findChildren('a', {'class': 'product-image'})[0]['href']

            if await ItemsShowedDbManager.exist(item_url, sr.id, loop):
                continue

            item_price = item.findChildren('span', {'class': 'price'})[0].text
            item_price = item_price.replace(' ', '')
            item_price = item_price.replace('\n', '')

            product_page = await get_html(item_url)
            bs = BeautifulSoup(product_page, 'lxml')

            sizes = bs.find_all('span', {'class': 'swatch-label'})

            text = tp.blackboxstore_com_text(item_url, item_name, sizes, item_price)

            await ItemsShowedDbManager.add(item_name, item_url, sr.id, loop)

            channel_id = int(sr.channel_id)
            await bot.get_channel(channel_id).send(text)
            print(item_url)


async def footdistrict_com(bot, search_requests):
    html = await get_html('https://footdistrict.com/novedades.html')
    bs = BeautifulSoup(html, 'lxml')
    items = bs.find_all('li', {'class': 'item'}, limit=10)
    print(len(items))

    for sr in search_requests:
        for item in items:
            item_name = item.findChildren('img', {'itemprop': 'image'})[0]['alt']

            if not compare(sr.request, item_name):
                continue

            item_url = item.findChildren('a', {'class': 'mp_quickview_icon mobilehidden'})[0]['href']

            if await ItemsShowedDbManager.exist(item_url, sr.id, loop):
                continue

            item_price = item.findChildren('span', {'class': 'price'})[0].text
            item_price = item_price.replace(' ', '')
            item_price = item_price.replace('\n', '')

            text = tp.common_text(item_url, item_name, item_price)
            print(text)
            await ItemsShowedDbManager.add(item_name, item_url, sr.id, loop)

            channel_id = int(sr.channel_id)
            await bot.get_channel(channel_id).send(text)
            print(item_url)


#  FAIL
async def luisaviaroma_com(bot, search_requests):
    html = await get_html('https://www.luisaviaroma.com/ru-ua/shop/%D0%BC%D1%83%D0%B6%D1%87%D0%B8%D0%BD%D1%8B/%D0%BD%D0%BE%D0%B2%D1%8B%D0%B5-%D0%BF%D0%BE%D1%81%D1%82%D1%83%D0%BF%D0%BB%D0%B5%D0%BD%D0%B8%D1%8F?lvrid=_gm_n&FilterSublines=4')
    bs = BeautifulSoup(html, 'lxml')
    items = bs.find_all('div', {'class': 'item__info___3z_8x7P_Pw'})
    print(len(items))


async def it_oneblockdown_it(bot, search_requests):
    html = await get_html('https://row.oneblockdown.it/collections/latest')
    bs = BeautifulSoup(html, 'lxml')
    items = bs.find_all('div', {'class': 'product-card'}, limit=10)
    print(len(items))

    if len(items) > 10:
        items = items[:10]

    for sr in search_requests:
        for item in items:
            brand = item.findChildren('a', {'class': 'vendor'})[0].text
            name = item.findChildren('h3')[0].text
            item_name = brand + ' ' + name

            if not compare(sr.request, item_name):
                continue

            item_url = 'https://row.oneblockdown.it/' + item.findChildren('a', {'class': 'vendor'})[0]['href']

            if await ItemsShowedDbManager.exist(item_url, sr.id, loop):
                continue

            price = item.find_all('span', {'class': 'price'})[0].text

            text = tp.common_text(item_url, item_name, price)
            await ItemsShowedDbManager.add(item_name, item_url, sr.id, loop)

            channel_id = int(sr.channel_id)
            await bot.get_channel(channel_id).send(text)
            print(item_url)


async def sivasdescalzo_com(bot, search_requests):
    html = await get_html('https://www.sivasdescalzo.com/en/lifestyle/sneakers')
    bs = BeautifulSoup(html, 'lxml')
    items = bs.find_all('div', {'class': 'product'}, limit=10)
    print(len(items))

    if len(items) > 10:
        items = items[:10]

    for sr in search_requests:
        for item in items:
            brand = item.findChildren('span', {'class': 'brand'})[0].text
            name = item.findChildren('span', {'class': 'model'})[0].text
            item_name = brand + ' ' + name

            if not compare(sr.request, item_name):
                continue

            item_url = item.findChildren('a', recursive=False)[0]['href']

            if await ItemsShowedDbManager.exist(item_url, sr.id, loop):
                continue

            product_page = await get_html(item_url)
            bs = BeautifulSoup(product_page, 'lxml')

            try:
                sizes = bs.find_all('ul', {'class': 'sizes small-block-grid-4'})[0]
                sizes = sizes.find_all('a', {'class': 'size-button available'})
            except Exception:
                sizes = []

            item_price = bs.find_all('span', {'class': 'product-price'})[0].text

            text = tp.sivasdescalzo_com_text(item_url, item_name, sizes, item_price)
            await ItemsShowedDbManager.add(item_name, item_url, sr.id, loop)

            channel_id = int(sr.channel_id)
            await bot.get_channel(channel_id).send(text)
            print(item_url)


#  FAIL
async def off_white_com(bot, search_requests):
    html = await get_html('https://www.off---white.com/en/NZ/section/new-arrivals')
    bs = BeautifulSoup(html, 'lxml')
    print(html)
    items = bs.find_all('article', {'class': 'product'})
    print(len(items))


async def shop_havenshop_com(bot, search_requests):
    html = await get_html('https://www.sivasdescalzo.com/en/lifestyle/sneakers')
    bs = BeautifulSoup(html, 'lxml')
    items = bs.find_all('div', {'class': 'product'}, limit=10)
    print(len(items))

    for sr in search_requests:
        for item in items:
            brand = item.findChildren('span', {'class': 'brand'})[0].text
            name = item.findChildren('span', {'class': 'model'})[0].text
            item_name = brand + ' ' + name

            if not compare(sr.request, item_name):
                continue

            item_url = item.findChildren('a', recursive=False)[0]['href']

            if await ItemsShowedDbManager.exist(item_url, sr.id, loop):
                continue

            product_page = await get_html(item_url)
            bs = BeautifulSoup(product_page, 'lxml')

            try:
                sizes = bs.find_all('ul', {'class': 'sizes small-block-grid-4'})[0]
                sizes = sizes.find_all('a', {'class': 'size-button available'})
            except Exception:
                sizes = []

            item_price = bs.find_all('span', {'class': 'product-price'})[0].text

            text = tp.sivasdescalzo_com_text(item_url, item_name, sizes, item_price)
            await ItemsShowedDbManager.add(item_name, item_url, sr.id, loop)

            channel_id = int(sr.channel_id)
            await bot.get_channel(channel_id).send(text)
            print(item_url)


#  FAIL
async def dope_factory_com(bot, search_requests):
    html = await get_html('https://www.dope-factory.com/collections/footwear/M')
    bs = BeautifulSoup(html, 'lxml')
    print(html)
    items = bs.find_all('div', {'class': 'product-grid-item'})
    print(len(items))


#  FAIL
async def suede_store_com(bot, search_requests):
    html = await get_html('https://suede-store.com/collections/footwear-m?sort_by=created-descending')
    bs = BeautifulSoup(html, 'lxml')
    print(html)
    items = bs.find_all('div', {'class': 'tt-product product-parent options-js tt-small'})
    print(len(items))


async def aimeleondore_com(bot, search_requests):
    html = await get_html('https://www.aimeleondore.com/collections/footwear')
    bs = BeautifulSoup(html, 'lxml')
    items = bs.find_all('div', {'class': 'grid-uniform grid-link__container shop-products'})[0]
    items = items.findChildren('div', recursive=False)
    print(len(items))

    if len(items) > 10:
        items = items[:10]

    for sr in search_requests:
        for item in items[:-2]:
            item_name = item.findChildren('div', {'class': 'grid-link__title collectionpage-product-title'})[0].text
            item_name = item_name.replace('QUICKSHOP', '')
            if not compare(sr.request, item_name):
                continue

            item_url = 'https://www.aimeleondore.com/' + item.findChildren('a', {'class': 'grid-link'})[0]['href']

            if await ItemsShowedDbManager.exist(item_url, sr.id, loop):
                continue

            text = tp.aimeleondore_com_text(item_name, item_url)

            await ItemsShowedDbManager.add(item_name, item_url, sr.id, loop)

            channel_id = int(sr.channel_id)
            await bot.get_channel(channel_id).send(text)
            print(item_url)


async def lustmexico_com(bot, search_requests):
    html = await get_html('https://www.lustmexico.com/collections/calzado-womens?sort_by=created-descending')
    bs = BeautifulSoup(html, 'lxml')
    items = bs.find_all('div', {'class': 'grid-product__content'}, limit=10)
    print(len(items))

    for sr in search_requests:
        for item in items:
            item_name = item.findChildren('div', {'class': 'grid-product__title'})[0].text

            if not compare(sr.request, item_name):
                continue

            item_url = 'https://www.lustmexico.com/' + item.findChildren('a', {'class': 'grid-product__link'})[0]['href']

            if await ItemsShowedDbManager.exist(item_url, sr.id, loop):
                continue

            product_page = await get_html(item_url)
            bs = BeautifulSoup(product_page, 'lxml')

            try:
                sizes = bs.find_all('fieldset', {'name': 'Size'})[0]
                sizes = sizes.find_all('label')
            except Exception:
                sizes = []

            item_price = bs.find_all('span', {'class': 'product__price'})[0]['content']

            text = tp.lustmexico_com_text(item_url, item_name, sizes, item_price)
            await ItemsShowedDbManager.add(item_name, item_url, sr.id, loop)

            channel_id = int(sr.channel_id)
            await bot.get_channel(channel_id).send(text)
            print(item_url)


async def onenessboutique_com(bot, search_requests):
    html = await get_html('https://www.onenessboutique.com/collections/mens-shoes-1')
    bs = BeautifulSoup(html, 'lxml')
    items = bs.find_all('div', {'class': 'product-wrap'}, limit=10)
    print(len(items))

    for sr in search_requests:
        for item in items:
            item_name = item.findChildren('span', {'class': 'title'})[0].text

            if not compare(sr.request, item_name):
                continue

            item_url = 'https://www.onenessboutique.com/' + item.findChildren('a', {'class': 'hidden-product-link'})[0]['href']

            if await ItemsShowedDbManager.exist(item_url, sr.id, loop):
                continue

            product_page = await get_html(item_url)
            bs = BeautifulSoup(product_page, 'lxml')

            try:
                sizes = bs.find_all('div', {'class': 'swatch clearfix'})[0]
                sizes = sizes.find_all('label')
            except Exception:
                sizes = []

            item_price = bs.find_all('p', {'class': 'modal_price'})[0].text

            text = tp.onenessboutique_com_text(item_url, item_name, sizes, item_price)

            await ItemsShowedDbManager.add(item_name, item_url, sr.id, loop)

            channel_id = int(sr.channel_id)
            await bot.get_channel(channel_id).send(text)
            print(item_url)


async def shop_exclucitylife_com(bot, search_requests):
    html = await get_html('https://shop.exclucitylife.com/collections/new-arrivals-men')
    bs = BeautifulSoup(html, 'lxml')
    items = bs.find_all('div', {'class': 'product-item product-item--push'}, limit=10)
    print(len(items))

    for sr in search_requests:
        for item in items:
            brand = item.findChildren('h4', {'class': 'product-item__vendor text--uppercase'})[0].text
            name = item.findChildren('a', {'class': 'link'})[0].text
            item_name = brand + ' ' + name

            if not compare(sr.request, item_name):
                continue

            item_url = 'https://shop.exclucitylife.com/' + item.findChildren('a', {'class': 'link'})[0]['href']

            if await ItemsShowedDbManager.exist(item_url, sr.id, loop):
                continue

            product_page = await get_html(item_url)
            bs = BeautifulSoup(product_page, 'lxml')

            try:
                sizes = bs.find_all('select', {'class': 'single-option-selector'})[0]
                sizes = sizes.findChildren('option')
            except Exception:
                sizes = []

            item_price = bs.find_all('span', {'class': 'product__price h5'})[0].text

            text = tp.onenessboutique_com_text(item_url, item_name, sizes, item_price)

            await ItemsShowedDbManager.add(item_name, item_url, sr.id, loop)

            channel_id = int(sr.channel_id)
            await bot.get_channel(channel_id).send(text)
            print(item_url)


async def saintalfred_com(bot, search_requests):
    html = await get_html('https://www.saintalfred.com/collections/footwear')
    bs = BeautifulSoup(html, 'lxml')
    items = bs.find_all('div', {'class': 'product-list-item'}, limit=10)
    print(len(items))

    for sr in search_requests:
        for item in items:
            brand = item.findChildren('p', {'class': 'product-list-item-vendor vendor meta'})[0].text
            name = item.findChildren('h3', {'class': 'product-list-item-title'})[0]
            item_name = brand + ' ' + name.text

            if not compare(sr.request, item_name):
                continue

            item_url = 'https://www.saintalfred.com/' + name.findChildren('a')[0]['href']

            if await ItemsShowedDbManager.exist(item_url, sr.id, loop):
                continue

            product_page = await get_html(item_url)
            bs = BeautifulSoup(product_page, 'lxml')

            try:
                sizes = bs.find_all('select', {'class': 'single-option-selector'})[0]
                sizes = sizes.findChildren('option')
            except Exception:
                sizes = []

            item_price = bs.find_all('span', {'class': 'product-price'})[0].text
            item_price = item_price.replace('\n', '')
            item_price = item_price.replace(' ', '')
            text = tp.onenessboutique_com_text(item_url, item_name, sizes, item_price)

            await ItemsShowedDbManager.add(item_name, item_url, sr.id, loop)

            channel_id = int(sr.channel_id)
            await bot.get_channel(channel_id).send(text)
            print(item_url)


async def undefeated_com(bot, search_requests):
    html = await get_html('https://undefeated.com/collections/footwear?sort_by=created-descending')
    bs = BeautifulSoup(html, 'lxml')
    items = bs.find_all('div', {'class': 'product-grid-item'}, limit=10)
    print(len(items))

    for sr in search_requests:
        for item in items:
            title = item.findChildren('a', recursive=False)[0]
            item_name = title['title']

            if not compare(sr.request, item_name):
                continue

            item_url = 'https://undefeated.com/' + title['href']

            if await ItemsShowedDbManager.exist(item_url, sr.id, loop):
                continue

            product_page = await get_html(item_url)
            bs = BeautifulSoup(product_page, 'lxml')

            try:
                sizes = bs.find_all('div', {'class': 'variants-wrapper clearfix'})[0]
                sizes = sizes.findChildren('option')
            except Exception:
                sizes = []

            item_price = bs.find_all('span', {'class': 'money'})[0].text

            text = tp.undefeated_com_text(item_url, item_name, sizes, item_price)

            await ItemsShowedDbManager.add(item_name, item_url, sr.id, loop)

            channel_id = int(sr.channel_id)
            await bot.get_channel(channel_id).send(text)
            print(item_url)


async def kith_com(bot, search_requests):
    html = await get_html('https://kith.com/collections/new-arrivals/sneakers')
    bs = BeautifulSoup(html, 'lxml')
    items = bs.find_all('li', {'class': 'collection-product'}, limit=10)
    print(len(items))

    for sr in search_requests:
        for item in items:
            item_name = item.findChildren('h1', {'class': 'product-card__title'})[0].text

            if not compare(sr.request, item_name):
                continue

            item_url = 'https://kith.com' + item.findChildren('a')[0]['href']

            if await ItemsShowedDbManager.exist(item_url, sr.id, loop):
                continue

            item_price = bs.find_all('span', {'class': 'product-card__price'})[0].text
            item_price = item_price.replace('\n', '')
            item_price = item_price.replace(' ', '')

            product_page = await get_html(item_url)
            bs = BeautifulSoup(product_page, 'lxml')

            try:
                sizes = bs.find_all('div', {'class': 'swatch clearfix'})[0]
                sizes = sizes.findChildren('label')
            except Exception:
                sizes = []

            text = tp.kith_com_text(item_url, item_name, sizes, item_price)

            await ItemsShowedDbManager.add(item_name, item_url, sr.id, loop)

            channel_id = int(sr.channel_id)
            await bot.get_channel(channel_id).send(text)
            print(item_url)


async def deadstock_ca(bot, search_requests):
    html = await get_html('https://www.deadstock.ca/collections/new-arrivals#')
    bs = BeautifulSoup(html, 'lxml')
    items = bs.find_all('div', {'class': 'grid-product__wrapper'}, limit=10)
    print(len(items))

    for sr in search_requests:
        for item in items:
            item_name = item.findChildren('span', {'class': 'grid-product__title'})[0].text

            if not compare(sr.request, item_name):
                continue

            item_url = 'https://www.deadstock.ca' + item.findChildren('a', {'class': 'grid-product__meta'})[0]['href']

            if await ItemsShowedDbManager.exist(item_url, sr.id, loop):
                continue

            product_page = await get_html(item_url)
            bs = BeautifulSoup(product_page, 'lxml')

            try:
                sizes = bs.find_all('fieldset', {'class': 'single-option-radio'})[0]
                sizes = sizes.findChildren('input')
            except Exception:
                sizes = []

            item_price = bs.find_all('span', {'class': 'money'})[0].text
            text = tp.deadstock_ca_text(item_url, item_name, sizes, item_price)

            await ItemsShowedDbManager.add(item_name, item_url, sr.id, loop)

            channel_id = int(sr.channel_id)
            await bot.get_channel(channel_id).send(text)
            print(item_url)


async def bluetilelounge_ca(bot, search_requests):
    html = await get_html('https://bluetilelounge.ca/collections/shoes?sort_by=created-descending')
    bs = BeautifulSoup(html, 'lxml')
    items = bs.find_all('div', {'class': 'prod-image'}, limit=10)
    print(len(items))

    for sr in search_requests:
        for item in items:
            url = item.findChildren('a')[0]
            item_name = url['title']

            if not compare(sr.request, item_name):
                continue

            item_url = 'https://bluetilelounge.ca' + url['href']

            if await ItemsShowedDbManager.exist(item_url, sr.id, loop):
                continue

            product_page = await get_html(item_url)
            bs = BeautifulSoup(product_page, 'lxml')

            try:
                sizes = bs.find_all('div', {'class': 'swatch-element'})
            except Exception:
                sizes = []

            item_price = bs.find_all('span', {'class': 'product-price'})[0].text
            text = tp.undefeated_com_text(item_url, item_name, sizes, item_price)

            await ItemsShowedDbManager.add(item_name, item_url, sr.id, loop)

            channel_id = int(sr.channel_id)
            await bot.get_channel(channel_id).send(text)
            print(item_url)


async def hanon_shop_com(bot, search_requests):
    html = await get_html('https://www.hanon-shop.com/collections/whats-new/cf-type-footwear?sort_by=created-descending')
    bs = BeautifulSoup(html, 'lxml')
    items = bs.find_all('div', {'class': 'item centered'}, limit=10)
    print(len(items))

    for sr in search_requests:
        for item in items:
            url = item.findChildren('h2', {'class': 'product-name'})[0]
            url = url.findChildren('a')[0]
            item_name = url.text
            item_name = item_name.replace('\n', '')
            item_name = item_name.replace('\t', '')

            if not compare(sr.request, item_name):
                continue

            item_url = 'https://www.hanon-shop.com' + url['href']

            if await ItemsShowedDbManager.exist(item_url, sr.id, loop):
                continue

            item_price = item.findChildren('span', {'class': 'money'})[0].text
            text = tp.common_text(item_url, item_name, item_price)

            await ItemsShowedDbManager.add(item_name, item_url, sr.id, loop)

            channel_id = int(sr.channel_id)
            await bot.get_channel(channel_id).send(text)
            print(item_url)


async def hannibalstore_it(bot, search_requests):
    html = await get_html('https://hannibalstore.it/collections/sneakers')
    bs = BeautifulSoup(html, 'lxml')
    items = bs.find_all('div', {'class': 'grid__item wide--one-fifth large--one-quarter medium-down--one-half'}, limit=10)
    print(len(items))

    for sr in search_requests:
        for item in items:
            item_name = item.findChildren('p', {'class': 'grid-link__title'})[0].text

            if not compare(sr.request, item_name):
                continue

            item_url = 'https://hannibalstore.it' + item.findChildren('a', {'class': 'grid-link text-center'})[0]['href']

            if await ItemsShowedDbManager.exist(item_url, sr.id, loop):
                continue

            item_price = item.findChildren('p', {'class': 'grid-link__meta'})[0].text
            item_price = item_price.replace('\n', '')
            item_price = item_price.replace(' ', '')
            item_price = item_price.replace('Regularprice', '')

            text = tp.common_text(item_url, item_name, item_price)

            await ItemsShowedDbManager.add(item_name, item_url, sr.id, loop)

            channel_id = int(sr.channel_id)
            await bot.get_channel(channel_id).send(text)
            print(item_url)


#  FAIL
async def yeezysupply_com(bot, search_requests):
    html = await get_html('https://www.yeezysupply.com/products')
    bs = BeautifulSoup(html, 'lxml')
    items = bs.find_all('div', {'class': 'col-l-6 col-s-6 plp-item___17OBr'})
    print(len(items))


#  FAIL
async def adidas_ru(bot, search_requests):
    html = await get_html('https://www.adidas.ru/muzhchiny-obuv-novinki?sort=newest-to-oldest')
    bs = BeautifulSoup(html, 'lxml')
    items = bs.find_all('div', {'class': 'col-s-6 col-m-4 col-l-6 no-gutters plp-column___3gy6t'})
    print(len(items))


#  FAIL
async def nike_com(bot, search_requests):
    html = await get_html('https://www.nike.com/w/new-3n82y')
    print(html)
    bs = BeautifulSoup(html, 'lxml')
    items = bs.find_all('div', {'class': 'product-card__info'})
    print(len(items))


#  FAIL
async def km20_ru(bot, search_requests):
    html = await get_html('https://www.km20.ru/catalog/men/footwear/sneakers/')
    print(html)
    bs = BeautifulSoup(html, 'lxml')
    items = bs.find_all('a', {'class': 'cat_item'})
    print(len(items))


async def brandshop_ru(bot, search_requests):
    html = await get_html('https://brandshop.ru/new/')
    bs = BeautifulSoup(html, 'lxml')
    items = bs.find_all('div', {'class': 'product'}, limit=10)
    print(len(items))

    for sr in search_requests:
        for item in items:
            url = item.findChildren('a', {'class': 'product-image'})[0]

            try:
                item_name = url['title']
            except KeyError:
                item_name = item.findChildren('h2')[0].text

                if not compare(sr.request, item_name):
                    continue

                photo_url = item.findChildren('img')[0]['src']

                if await ItemsShowedDbManager.exist(photo_url, sr.id, loop):
                    continue

                await ItemsShowedDbManager.add(item_name, photo_url, sr.id, loop)

                text = tp.brandshop_com_soon_text(item_name, photo_url)

                channel_id = int(sr.channel_id)
                await bot.get_channel(channel_id).send(text)

                continue

            if not compare(sr.request, item_name):
                continue

            item_url = url['href']

            if await ItemsShowedDbManager.exist(item_url, sr.id, loop):
                continue

            item_price = item.findChildren('div', {'class': 'price price-box'})[0].text + ' ₽'
            item_price = item_price.replace('р', '')
            text = tp.common_text(item_url, item_name, item_price)

            await ItemsShowedDbManager.add(item_name, item_url, sr.id, loop)

            channel_id = int(sr.channel_id)
            await bot.get_channel(channel_id).send(text)
            print(item_url)


async def sneakerhead_ru(bot, search_requests):
    html = await get_html('https://sneakerhead.ru/isnew/shoes/sneakers/')
    bs = BeautifulSoup(html, 'lxml')
    items = bs.find_all('div', {'class': 'product-card'}, limit=10)
    print(len(items))

    for sr in search_requests:
        for item in items:
            brand = item.findChildren('meta', {'itemprop': 'manufacturer'})[0]['content']
            name = item.findChildren('meta', {'itemprop': 'name'})[0]['content']
            item_name = brand + ' ' + name

            if not compare(sr.request, item_name):
                continue

            item_url = 'https://sneakerhead.ru' + item.findChildren('a', {'class': 'product-card__link'})[0]['href']

            if await ItemsShowedDbManager.exist(item_url, sr.id, loop):
                continue

            item_price = bs.find_all('span', {'class': 'product-card__price-value'})[0].text + ' ₽'
            item_price = item_price.replace(' ', '')
            item_price = item_price.replace('\n', '')

            text = tp.common_text(item_url, item_name, item_price)

            await ItemsShowedDbManager.add(item_name, item_url, sr.id, loop)

            channel_id = int(sr.channel_id)
            await bot.get_channel(channel_id).send(text)
            print(item_url)


async def slamjam_com(bot, search_requests):
    html = await get_html('https://www.slamjam.com/en_IT/man/footwear/sneakers')
    bs = BeautifulSoup(html, 'lxml')
    items = bs.find_all('div', {'itemprop': 'itemListElement'}, limit=10)
    print(len(items))

    for sr in search_requests:
        for item in items:
            brand = item.findChildren('h2', {'class': 't-up'})[0].text
            name = item.findChildren('span', {'itemprop': 'name'})[0].text
            item_name = brand + ' ' + name
            item_name = item_name.replace('\n', '')

            if not compare(sr.request, item_name):
                continue

            item_url = 'https://www.slamjam.com' + item.findChildren('a', {'class': 'link'})[0]['href']

            if await ItemsShowedDbManager.exist(item_url, sr.id, loop):
                continue

            product_page = await get_html(item_url)
            bs = BeautifulSoup(product_page, 'lxml')

            try:
                sizes = bs.find_all('select', {'id': 'select-prenotation'})[0]
                sizes = sizes.findChildren('option')
                sizes = sizes[1:]
            except Exception:
                sizes = []

            item_price = bs.find_all('span', {'class': 'value'})[0]['content'] + ' €'
            text = tp.sivasdescalzo_com_text(item_url, item_name, sizes, item_price)

            await ItemsShowedDbManager.add(item_name, item_url, sr.id, loop)

            channel_id = int(sr.channel_id)
            await bot.get_channel(channel_id).send(text)
            print(item_url)


async def tres_bien_com(bot, search_requests):
    html = await get_html('https://tres-bien.com/new-items?cat=10')
    bs = BeautifulSoup(html, 'lxml')
    items = bs.find_all('article', {'class': 'product-item-info'}, limit=10)
    print(len(items))

    for sr in search_requests:
        for item in items:
            url = item.findChildren('a', {'class': 'product-item-link'})[0]
            item_name = url.text

            if not compare(sr.request, item_name):
                continue

            item_url = url['href']

            if await ItemsShowedDbManager.exist(item_url, sr.id, loop):
                continue

            item_price = item.findChildren('span', {'class': 'price'})[0].text
            text = tp.common_text(item_url, item_name, item_price)

            await ItemsShowedDbManager.add(item_name, item_url, sr.id, loop)

            channel_id = int(sr.channel_id)
            await bot.get_channel(channel_id).send(text)
            print(item_url)


async def urbanjunglestore_com(bot, search_requests):
    html = await get_html('https://www.urbanjunglestore.com/en/men/footwear/sneakers.html')
    bs = BeautifulSoup(html, 'lxml')
    items = bs.find_all('li', {'class': 'item'}, limit=10)
    print(len(items))

    for sr in search_requests:
        for item in items:
            url = item.findChildren('h2', {'class': 'product-name'})[0]
            url = url.findChildren('a')[0]
            item_name = url['title']

            if not compare(sr.request, item_name):
                continue

            item_url = url['href']

            if await ItemsShowedDbManager.exist(item_url, sr.id, loop):
                continue

            item_price = item.findChildren('span', {'class': 'price'})[0].text
            text = tp.common_text(item_url, item_name, item_price)
            await ItemsShowedDbManager.add(item_name, item_url, sr.id, loop)

            channel_id = int(sr.channel_id)
            await bot.get_channel(channel_id).send(text)
            print(item_url)


if __name__ == '__main__':
    loop.run_until_complete(ItemsShowedDbManager.clear(loop))
    search_requests = [SearchRequest(1, 'air force 1', 640641207491493888)]
    loop.run_until_complete(brandshop_ru(123, search_requests))
