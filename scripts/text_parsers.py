def hypedc_com_text(item_info, item_sizes, item_url):
    price = item_info['price']
    item_name = item_info['brand'] + ' ' + item_info['name']

    try:
        us_man = item_sizes['US Men']
        us_man_text = '**US:** '
        for s in us_man:
            us_man_text += f'{s}/'
        us_man_text = us_man_text[:-1]
    except KeyError:
        us_man = None

    try:
        europe = item_sizes['Europe']
        europe_text = '**EU:** '
        for s in europe:
            europe_text += f'{s}/'
        europe_text = europe_text[:-1]
    except KeyError:
        europe = None

    text = f'''**{item_name}**

**Цена:** {price}$

**Ссылка на товар:** {item_url}

**Размеры**
'''
    if us_man is not None:
        text += f'''
{us_man_text}'''

    if europe is not None:
        text += f'''
{europe_text}'''

    return text


def subtypestore_com_text(url, item_name, sizes, price):
    sizes_text = ''
    for size in sizes:
        sizes_text += f'{size.text}/'
    sizes_text = sizes_text[:-1]

    price = price
    price = price.replace(' ', '')
    price = price.replace('\n', '')
    print(price, url, sizes_text, item_name)
    text = f'''**{item_name}**

**Цена:** {price}

**Ссылка на товар:** {url}

**Размеры**
**US:** {sizes_text}'''

    return text


def lockwood_avenue_com_text(url, item_name, sizes, price):

    sizes_text = ''
    for size in sizes:
        text = size.text
        text = text.replace('\n', '')
        text = text.replace('\t', '')
        sizes_text += f'''\n
{text}'''

    text = f'''**{item_name}**

**Цена:** {price}

**Ссылка на товар:** {url}

**Размеры**
'''
    text += sizes_text

    return text


def rezetstore_dk_text(url, item_name, sizes, price):

    sizes_text = ''
    for size in sizes:
        text = size.text
        text = text.replace('\n', '')
        text = text.replace('\t', '')
        sizes_text += f'''
{text}'''

    text = f'''**{item_name}**

**Цена:** {price}

**Ссылка на товар:** {url}

**Размеры**
'''
    text += sizes_text

    return text


def stormfashion_dk_text(url, item_name, price):
    item_name = item_name.replace('\n', '')
    item_name = item_name.replace(' ', '')

    text = f'''**{item_name}**

**Цена:** {price} DKK

**Ссылка на товар:** {url}'''

    return text


def common_text(url, item_name, price):
    text = f'''**{item_name}**

**Цена:** {price}

**Ссылка на товар:** {url}'''

    return text


def basket4ballers_com(url, item_name, sizes, price):
    sizes_text = ''
    for size in sizes:
        txt = size.text
        txt = txt.replace('\n', '')
        txt = txt.replace('\t', '')
        sizes_text += f'''\n{txt}'''

    text = f'''**{item_name}**

**Цена:** {price}  €

**Ссылка на товар:** {url}

**Размеры (EU)**'''
    text += sizes_text

    return text


def bouncewear_com_text(url, item_name, sizes, price):
    sizes_text = ''
    for size in sizes:
        if 'not in stock' not in size.text:
            sizes_text += f'''\n{size.text}'''

    text = f'''**{item_name}**
**Цена:** {price}

**Ссылка на товар:** {url}

**Размеры**'''
    text += sizes_text
    return text


def chezvibe_com_text(url, item_name, sizes, price):
    sizes_text = ''
    for size in sizes:
        sizes_text += f'''{size.text}/'''
    sizes_text = sizes_text[:-1]
    text = f'''**{item_name}**

**Цена:** {price}

**Ссылка на товар:** {url}

**Размеры (EU)**
'''
    text += sizes_text

    return text


def galerieslafayette_com_text(url, item_name, sizes, price):
    sizes_text = ''
    if sizes is not []:
        sizes_text = '''**Размеры**'''
        for size in sizes:
            t = size.text
            t = t.replace('\n', '')
            t = t.replace('\t', '')
            t = t.replace(' ', '')
            sizes_text += f'''\n{t}'''
        sizes_text = sizes_text[:-1]
    text = f'''**{item_name}**

**Цена:** {price}

**Ссылка на товар:** {url}

'''
    text += sizes_text

    return text


def thenextdoor_fr_text(url, item_name, sizes, price):
    sizes_text = ''
    if sizes is not []:
        sizes_text = '''**Размеры**'''
        for size in sizes:
            sizes_text += f'''\n{size['value']}'''
        sizes_text = sizes_text[:-1]
    text = f'''**{item_name}**

**Цена:** {price}

**Ссылка на товар:** {url}

'''
    text += sizes_text

    return text


def the_broken_arm_com_tex(url, item_name, sizes, price):
    sizes_text = ''
    if sizes is not []:
        sizes_text = '''**Размеры**'''
        for size in sizes[1:]:
            txt = size.text.replace('\n', '')
            if 'OUT OF STOCK' not in txt:
                sizes_text += f'''\n{txt}'''
    text = f'''**{item_name}**

**Цена:** {price}

**Ссылка на товар:** {url}

'''
    text += sizes_text

    return text


def allikestore_com_text(url, item_name, sizes, price):
    sizes = sizes.replace('Sizes Available', '**Размеры**')
    text = f'''**{item_name}**

**Цена:** {price}

**Ссылка на товар:** {url}

{sizes}'''
    return text


def footdistrict_com_text(url, item_name, sizes, price):
    sizes_text = ''
    if sizes is not []:
        sizes_text = '''**Размеры**'''
        for size in sizes[1:]:
            txt = size.text.replace('\n', '')
            if 'No disponible' not in txt:
                sizes_text += f'''\n{txt}'''
    text = f'''**{item_name}**

**Цена:** {price}

**Ссылка на товар:** {url}

'''
    text += sizes_text

    return text
