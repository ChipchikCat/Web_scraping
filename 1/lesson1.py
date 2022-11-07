import requests
import json
# sourse = requests.get('https://www.mvideo.ru/noutbuki-planshety-komputery-8/planshety-195?reff=menu_main')
# sourse.encoding='windows-1251'

def get_data():

    cookies = {
        '__lhash_': '0f260e67b33dad8e238dc4c481b970c9',
        'CACHE_INDICATOR': 'false',
        'COMPARISON_INDICATOR': 'false',
        'HINTS_FIO_COOKIE_NAME': '2',
        'MVID_AB_PDP_CHAR': '2',
        'MVID_AB_SERVICES_DESCRIPTION': 'var4',
        'MVID_AB_TOP_SERVICES': '1',
        'MVID_BLACK_FRIDAY_ENABLED': 'true',
        'MVID_CALC_BONUS_RUBLES_PROFIT': 'false',
        'MVID_CART_AVAILABILITY': 'true',
        'MVID_CART_MULTI_DELETE': 'false',
        'MVID_CATALOG_STATE': '1',
        'MVID_CHECKOUT_REGISTRATION_AB_TEST': '2',
        'MVID_CREDIT_AVAILABILITY': 'true',
        'MVID_CRITICAL_GTM_INIT_DELAY': '3000',
        'MVID_FILTER_CODES': 'true',
        'MVID_FILTER_TOOLTIP': '1',
        'MVID_FLOCKTORY_ON': 'true',
        'MVID_GET_LOCATION_BY_DADATA': 'DaData',
        'MVID_GIFT_KIT': 'true',
        'MVID_GLC': 'true',
        'MVID_GLP': 'true',
        'MVID_GTM_ENABLED': '011',
        'MVID_GUEST_ID': '21789157613',
        'MVID_HANDOVER_SUMMARY': 'true',
        'MVID_IS_NEW_BR_WIDGET': 'true',
        'MVID_LAYOUT_TYPE': '1',
        'MVID_LP_SOLD_VARIANTS': '3',
        'MVID_MCLICK': 'true',
        'MVID_MINDBOX_DYNAMICALLY': 'true',
        'MVID_MINI_PDP': 'true',
        'MVID_MOBILE_FILTERS': 'true',
        'MVID_NEW_ACCESSORY': 'true',
        'MVID_NEW_DESKTOP_FILTERS': 'true',
        'MVID_NEW_LK_CHECK_CAPTCHA': 'true',
        'MVID_NEW_LK_OTP_TIMER': 'true',
        'MVID_NEW_MBONUS_BLOCK': 'true',
        'MVID_PROMO_CATALOG_ON': 'true',
        'MVID_SERVICES': '111',
        'MVID_SERVICES_MINI_BLOCK': 'var2',
        'MVID_WEBP_ENABLED': 'true',
        'NEED_REQUIRE_APPLY_DISCOUNT': 'true',
        'PRESELECT_COURIER_DELIVERY_FOR_KBT': 'true',
        'PROMOLISTING_WITHOUT_STOCK_AB_TEST': '2',
        'SENTRY_ERRORS_RATE': '0.1',
        'SENTRY_TRANSACTIONS_RATE': '0.5',
        'flacktory': 'no',
        'searchType2': '2',
        'MVID_ENVCLOUD': 'prod1',
        'MVID_CITY_ID': 'CityCZ_6270',
        'MVID_GEOLOCATION_NEEDED': 'false',
        'MVID_REGION_ID': '24',
        'MVID_REGION_SHOP': 'S924',
        'MVID_TIMEZONE_OFFSET': '4',
        'JSESSIONID': '1vyVjnhSWlL437Smhxy0r6wvDnB21kwT8FhcYTY3lDGv21tgHJLv!-1462946723',
        'MVID_CITY_CHANGED': 'false',
        'MVID_KLADR_ID': '6300000700000',
        'bIPs': '-955324074',
    }

    headers = {
        'authority': 'www.mvideo.ru',
        'accept': 'application/json',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'baggage': 'sentry-transaction=%2F,sentry-public_key=1e9efdeb57cf4127af3f903ec9db1466,sentry-trace_id=8c71b3862b34463a910099462e607848,sentry-sample_rate=0%2C5',
        # Requests sorts cookies= alphabetically
        # 'cookie': '__lhash_=0f260e67b33dad8e238dc4c481b970c9; CACHE_INDICATOR=false; COMPARISON_INDICATOR=false; HINTS_FIO_COOKIE_NAME=2; MVID_AB_PDP_CHAR=2; MVID_AB_SERVICES_DESCRIPTION=var4; MVID_AB_TOP_SERVICES=1; MVID_BLACK_FRIDAY_ENABLED=true; MVID_CALC_BONUS_RUBLES_PROFIT=false; MVID_CART_AVAILABILITY=true; MVID_CART_MULTI_DELETE=false; MVID_CATALOG_STATE=1; MVID_CHECKOUT_REGISTRATION_AB_TEST=2; MVID_CREDIT_AVAILABILITY=true; MVID_CRITICAL_GTM_INIT_DELAY=3000; MVID_FILTER_CODES=true; MVID_FILTER_TOOLTIP=1; MVID_FLOCKTORY_ON=true; MVID_GET_LOCATION_BY_DADATA=DaData; MVID_GIFT_KIT=true; MVID_GLC=true; MVID_GLP=true; MVID_GTM_ENABLED=011; MVID_GUEST_ID=21789157613; MVID_HANDOVER_SUMMARY=true; MVID_IS_NEW_BR_WIDGET=true; MVID_LAYOUT_TYPE=1; MVID_LP_SOLD_VARIANTS=3; MVID_MCLICK=true; MVID_MINDBOX_DYNAMICALLY=true; MVID_MINI_PDP=true; MVID_MOBILE_FILTERS=true; MVID_NEW_ACCESSORY=true; MVID_NEW_DESKTOP_FILTERS=true; MVID_NEW_LK_CHECK_CAPTCHA=true; MVID_NEW_LK_OTP_TIMER=true; MVID_NEW_MBONUS_BLOCK=true; MVID_PROMO_CATALOG_ON=true; MVID_SERVICES=111; MVID_SERVICES_MINI_BLOCK=var2; MVID_WEBP_ENABLED=true; NEED_REQUIRE_APPLY_DISCOUNT=true; PRESELECT_COURIER_DELIVERY_FOR_KBT=true; PROMOLISTING_WITHOUT_STOCK_AB_TEST=2; SENTRY_ERRORS_RATE=0.1; SENTRY_TRANSACTIONS_RATE=0.5; flacktory=no; searchType2=2; MVID_ENVCLOUD=prod1; MVID_CITY_ID=CityCZ_6270; MVID_GEOLOCATION_NEEDED=false; MVID_REGION_ID=24; MVID_REGION_SHOP=S924; MVID_TIMEZONE_OFFSET=4; JSESSIONID=1vyVjnhSWlL437Smhxy0r6wvDnB21kwT8FhcYTY3lDGv21tgHJLv!-1462946723; MVID_CITY_CHANGED=false; MVID_KLADR_ID=6300000700000; bIPs=-955324074',
        'referer': 'https://www.mvideo.ru/noutbuki-planshety-komputery-8/planshety-195?reff=menu_main',
        'sec-ch-ua': '"Not-A.Brand";v="99", "Opera GX";v="91", "Chromium";v="105"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'sentry-trace': '8c71b3862b34463a910099462e607848-b19ee265ed5ee908-0',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 OPR/91.0.4516.106',
        'x-set-application-id': '276c0bc1-d77c-4837-8744-766e10685abc',
    }

    params = {
        'categoryId': '195',
        'offset': '0',
        'limit': '24',
        'filterParams': 'WyJ0b2xrby12LW5hbGljaGlpIiwiLTEyIiwiZGEiXQ==',
        'doTranslit': 'true',
    }

    response = requests.get('https://www.mvideo.ru/bff/products/listing', params=params, cookies=cookies, headers=headers).json()
    # print(response)

    products_id = response.get("body").get("products")

    with open('1/1_product_id.json', "w") as file: json.dump(products_id, file, indent=4, ensure_ascii=False)

    # print(products_id)

    json_data = {
        'productIds': products_id,
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

    with open("1/2_items.json", "w", encoding="utf-8") as file:
        json.dump(response, file, indent=4, ensure_ascii=False)

    # print(len(response.get("body").get("products")))

    products_id_str = ",".join(products_id)

    params = {
        'productIds': products_id_str,
        'addBonusRubles': 'true',
        'isPromoApplied': 'true',
    }

    response = requests.get('https://www.mvideo.ru/bff/products/prices', params=params, cookies=cookies, headers=headers).json()

    with open("1/3_prices.json", "w", encoding="utf-8") as file:
        json.dump(response, file, indent=4, ensure_ascii=False)

    items_prices = {}

    material_prices = response.get("body").get("materialPrices")

    for item in material_prices:
        item_id = item.get  ("price").get("productId")
        item_base_price = item.get("price").get("basePrice")
        item_sale_price = item.get("price").get("salePrice")
        item_bonus = item.get("bonusRubles").get("total")

        items_prices[item_id] = {
            "item_basePrice" : item_base_price,
            "item_salePrice" : item_sale_price,
            "item_bonus" : item_bonus
        }

    with open("1/4_item_prices.json", "w", encoding="utf-8") as file:
        json.dump(items_prices, file, indent=4, ensure_ascii=False)

def get_result():
    with open("1/2_items.json") as file:
        products_data = json.load(file)

    with open("1/4_item_prices.json") as file:
        products_prices = json.load(file)

    products_data = products_data.get("body").get("products")

    for item in products_data:
        product_id = item.get('productId')

        if product_id in products_prices:
            prices = products_prices[product_id]

        item["item_basePrice"] = prices.get("item_basePrice")
        item["item_salePrice"] = prices.get("item_salePrice")
        item["item_bonus"] = prices.get("item_bonus")


    
    with open("1/5_result.json", "w", encoding="utf-8") as file:
        json.dump(products_data, file, indent=4, ensure_ascii=False)


def main():
    get_data()
    get_result()


if __name__ == "__main__":
    main()
