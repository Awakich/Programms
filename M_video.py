import requests
import json

def get_data():
    cookies = {
        'HINTS_FIO_COOKIE_NAME': '2',
        'MAIN_PAGE_VARIATION': '6',
        'MVID_ABC_TEST_WIDGET': '0',
        'MVID_AB_PROMO_DAILY': '1',
        'MVID_AB_SERVICES_DESCRIPTION': 'var2',
        'MVID_AB_TEST_COMPARE_ONBOARDING': 'true',
        'MVID_ADDRESS_COMMENT_AB_TEST': '2',
        'MVID_BLACK_FRIDAY_ENABLED': 'true',
        'MVID_CALC_BONUS_RUBLES_PROFIT': 'false',
        'MVID_CART_MULTI_DELETE': 'false',
        'MVID_CATALOG_STATE': '1',
        'MVID_CITY_ID': 'CityCZ_15507',
        'MVID_FILTER_CODES': 'true',
        'MVID_FILTER_TOOLTIP': '1',
        'MVID_FLOCKTORY_ON': 'true',
        'MVID_GEOLOCATION_NEEDED': 'true',
        'MVID_GET_LOCATION_BY_DADATA': 'DaData',
        'MVID_GIFT_KIT': 'true',
        'MVID_GUEST_ID': '20648688942',
        'MVID_IS_NEW_BR_WIDGET': 'true',
        'MVID_KLADR_ID': '3100000100000',
        'MVID_LAYOUT_TYPE': '1',
        'MVID_NEW_ACCESSORY': 'true',
        'MVID_NEW_LK_CHECK_CAPTCHA': 'true',
        'MVID_NEW_LK_OTP_TIMER': 'true',
        'MVID_NEW_MBONUS_BLOCK': 'true',
        'MVID_NEW_SUGGESTIONS': 'true',
        'MVID_PRICE_FIRST': '2',
        'MVID_PRM20_CMS': 'true',
        'MVID_REGION_ID': '78',
        'MVID_REGION_SHOP': 'S943',
        'MVID_SERVICES_MINI_BLOCK': 'var2',
        'MVID_TAXI_DELIVERY_INTERVALS_VIEW': 'old',
        'MVID_TIMEZONE_OFFSET': '3',
        'MVID_WEBP_ENABLED': 'true',
        'NEED_REQUIRE_APPLY_DISCOUNT': 'true',
        'PRESELECT_COURIER_DELIVERY_FOR_KBT': 'true',
        'PROMOLISTING_WITHOUT_STOCK_AB_TEST': '2',
        'searchType2': '2',
        'popmechanic_sbjs_migrations': 'popmechanic_1418474375998%3D1%7C%7C%7C1471519752600%3D1%7C%7C%7C1471519752605%3D1',
        '__SourceTracker': 'google__organic',
        'admitad_deduplication_cookie': 'google__organic',
        'MVID_NEW_DESKTOP_FILTERS': 'true',
        '__ttl__widget__ui': '1651926952248-009528dfc0b1',
        '__lhash_': '6a28f02accc38b2b37db6d522b828546',
        'CACHE_INDICATOR': 'false',
        'COMPARISON_INDICATOR': 'false',
        'JSESSIONID': '19WjvGvLV44sRRzLDf2tPKzMpW8hkPcqGwGQ2Vfx1MgrvxJHVXGJ!-1157120473',
        'MVID_2_exp_in_1': '1',
        'MVID_CART_AVAILABILITY': 'true',
        'MVID_CREDIT_AVAILABILITY': 'true',
        'MVID_GTM_DELAY': 'true',
        'MVID_LP_SOLD_VARIANTS': '3',
        'MVID_MCLICK': 'true',
        'MVID_MOBILE_FILTERS': 'false',
        'MVID_MULTIOFFER': 'true',
        'MVID_SERVICES': '111',
        'bIPs': '1613809182',
        'flacktory': 'no',
        'MVID_ENVCLOUD': 'prod1',
        'mindboxDeviceUUID': 'f35ee677-2041-473c-a7b4-9993400f781b',
        'directCrm-session': '%7B%22deviceGuid%22%3A%22f35ee677-2041-473c-a7b4-9993400f781b%22%7D',
        '_ga_CFMZTSS5FM': 'GS1.1.1657037337.1.1.1657037390.0',
        '_ga': 'GA1.1.670363774.1657037337',
        '_ga_BNX5WPP3YK': 'GS1.1.1657037337.1.1.1657037390.7',
        'SMSError': '',
        'authError': '',
        'gdeslon.ru.__arc_domain': 'gdeslon.ru',
        'gdeslon.ru.user_id': 'e0d9f3ff-7c42-4973-adc1-ce97c47e387b',
        'advcake_track_id': 'eb34de2c-def5-955d-cc3d-10a50e883445',
        'advcake_session_id': 'c85543ad-b1b2-5097-39ea-cd78a1c56c94',
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0',
        'Accept': 'application/json',
        'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
        # 'Accept-Encoding': 'gzip, deflate, br',
        'x-set-application-id': '01a9fc11-caf9-40ea-812d-891d29f7015c',
        'DNT': '1',
        'Connection': 'keep-alive',
        'Referer': 'https://www.mvideo.ru/noutbuki-planshety-komputery-8/planshety-195/f/skidka=da/tolko-v-nalichii=da',
        # Requests sorts cookies= alphabetically
        # 'Cookie': 'HINTS_FIO_COOKIE_NAME=2; MAIN_PAGE_VARIATION=6; MVID_ABC_TEST_WIDGET=0; MVID_AB_PROMO_DAILY=1; MVID_AB_SERVICES_DESCRIPTION=var2; MVID_AB_TEST_COMPARE_ONBOARDING=true; MVID_ADDRESS_COMMENT_AB_TEST=2; MVID_BLACK_FRIDAY_ENABLED=true; MVID_CALC_BONUS_RUBLES_PROFIT=false; MVID_CART_MULTI_DELETE=false; MVID_CATALOG_STATE=1; MVID_CITY_ID=CityCZ_15507; MVID_FILTER_CODES=true; MVID_FILTER_TOOLTIP=1; MVID_FLOCKTORY_ON=true; MVID_GEOLOCATION_NEEDED=true; MVID_GET_LOCATION_BY_DADATA=DaData; MVID_GIFT_KIT=true; MVID_GUEST_ID=20648688942; MVID_IS_NEW_BR_WIDGET=true; MVID_KLADR_ID=3100000100000; MVID_LAYOUT_TYPE=1; MVID_NEW_ACCESSORY=true; MVID_NEW_LK_CHECK_CAPTCHA=true; MVID_NEW_LK_OTP_TIMER=true; MVID_NEW_MBONUS_BLOCK=true; MVID_NEW_SUGGESTIONS=true; MVID_PRICE_FIRST=2; MVID_PRM20_CMS=true; MVID_REGION_ID=78; MVID_REGION_SHOP=S943; MVID_SERVICES_MINI_BLOCK=var2; MVID_TAXI_DELIVERY_INTERVALS_VIEW=old; MVID_TIMEZONE_OFFSET=3; MVID_WEBP_ENABLED=true; NEED_REQUIRE_APPLY_DISCOUNT=true; PRESELECT_COURIER_DELIVERY_FOR_KBT=true; PROMOLISTING_WITHOUT_STOCK_AB_TEST=2; searchType2=2; popmechanic_sbjs_migrations=popmechanic_1418474375998%3D1%7C%7C%7C1471519752600%3D1%7C%7C%7C1471519752605%3D1; __SourceTracker=google__organic; admitad_deduplication_cookie=google__organic; MVID_NEW_DESKTOP_FILTERS=true; __ttl__widget__ui=1651926952248-009528dfc0b1; __lhash_=6a28f02accc38b2b37db6d522b828546; CACHE_INDICATOR=false; COMPARISON_INDICATOR=false; JSESSIONID=19WjvGvLV44sRRzLDf2tPKzMpW8hkPcqGwGQ2Vfx1MgrvxJHVXGJ!-1157120473; MVID_2_exp_in_1=1; MVID_CART_AVAILABILITY=true; MVID_CREDIT_AVAILABILITY=true; MVID_GTM_DELAY=true; MVID_LP_SOLD_VARIANTS=3; MVID_MCLICK=true; MVID_MOBILE_FILTERS=false; MVID_MULTIOFFER=true; MVID_SERVICES=111; bIPs=1613809182; flacktory=no; MVID_ENVCLOUD=prod1; mindboxDeviceUUID=f35ee677-2041-473c-a7b4-9993400f781b; directCrm-session=%7B%22deviceGuid%22%3A%22f35ee677-2041-473c-a7b4-9993400f781b%22%7D; _ga_CFMZTSS5FM=GS1.1.1657037337.1.1.1657037390.0; _ga=GA1.1.670363774.1657037337; _ga_BNX5WPP3YK=GS1.1.1657037337.1.1.1657037390.7; SMSError=; authError=; gdeslon.ru.__arc_domain=gdeslon.ru; gdeslon.ru.user_id=e0d9f3ff-7c42-4973-adc1-ce97c47e387b; advcake_track_id=eb34de2c-def5-955d-cc3d-10a50e883445; advcake_session_id=c85543ad-b1b2-5097-39ea-cd78a1c56c94',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        # Requests doesn't support trailers
        # 'TE': 'trailers',
    }

    params = {
        'categoryId': '195',
        'offset': '0',
        'limit': '24',
        'filterParams': [
            'WyJza2lka2EiLCIiLCJkYSJd',
            'WyJ0b2xrby12LW5hbGljaGlpIiwiIiwiZGEiXQ==',
        ],
        'doTranslit': 'true',
    }

    response = requests.get('https://www.mvideo.ru/bff/products/listing', params=params, cookies=cookies, headers=headers).json()
    products_ids = response.get('body').get('products') # берем id товаров

    with open('1_products_ids.json', 'w') as file:
        json.dump(products_ids, file, indent=4, ensure_ascii=False)

    json_data = {
        'productIds': products_ids,
        'mediaTypes': [
            'images',
        ],
        'category': True,
        'status': True,
        'brand': True,
        'propertyTypes': [
            'KEY',
        ],
        'propertiesConfig': {
            'propertiesPortionSize': 5,
        },
        'multioffer': False,
    }

    response = requests.post('https://www.mvideo.ru/bff/product-details/list', cookies=cookies, headers=headers, json=json_data).json()

    with open('2_items.json', 'w') as file:
        json.dump(response, file, indent=4, ensure_ascii=False)

    products_ids_str = ','.join(products_ids)

    params = {
        'productIds': products_ids_str,
        'addBonusRubles': 'true',
        'isPromoApplied': 'true',
    }

    response = requests.get('https://www.mvideo.ru/bff/products/prices', params=params, cookies=cookies, headers=headers).json()
    # берем ценники бонусы описанием акций

    with open('3_prices.json', 'w') as file:
        json.dump(response ,file, indent=4, ensure_ascii=False)

    items_prices = {}

    material_prices = response.get('body').get('materialPrices')

    for item in material_prices:
        item_id = item.get('price').get('productId')
        item_base_price = item.get('price').get('basePrice')
        item_sale_price = item.get('price').get('salePrice')
        item_bonus = item.get('bonusRubles').get('total')

        items_prices[item_id] = {
            'item_base_price': item_base_price,
            'item_sale_price': item_sale_price,
            'item_bonus': item_bonus
        }
    with open('4_item_prices.json', 'w') as file:
        json.dump(items_prices, file, indent=4, ensure_ascii=False)

def get_result():
    with open('2_items.json') as file:
        products_data = json.load(file)

    with open('4_item_prices.json') as file:
        products_prices = json.load(file)

    products_data = products_data.get('body').get('products')

    for item in products_data:
        product_id = item.get('productId')

        if product_id in products_prices:
            prices = products_prices[product_id]

        item['item_basePrice'] = prices.get('item_basePrice')
        item['item_salePrice'] = prices.get('item_salePrice')
        item['item_bonus'] = prices.get('item_bonus')

    with open('5_result.json', 'w') as file:
        json.dump(products_data, file, indent=4, ensure_ascii=False)

def main():
    get_data()
    get_result()


if __name__ == '__main__':
    main()