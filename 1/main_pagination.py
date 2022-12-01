import requests
import json
from config import headers, cookies
import os
import math
# sourse = requests.get('https://www.mvideo.ru/noutbuki-planshety-komputery-8/planshety-195?reff=menu_main')
# sourse.encoding='windows-1251'

def get_data():

    params = {
        'categoryId': '195',
        'offset': '0',
        'limit': '24',
        'filterParams': 'WyJ0b2xrby12LW5hbGljaGlpIiwiLTEyIiwiZGEiXQ==',
        'doTranslit': 'true',
    }

    if not os.path.exists("data"):
        os.mkdir("data")

    s = requests.Session()

    response = s.get('https://www.mvideo.ru/bff/products/listing', params=params, cookies=cookies, headers=headers).json()

    total_item = response.get("body").gey("total")

    if total_item is None:
        return "[!] No items :( "

    pages_count = math.ceil(total_item/24)

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
    with open("1/2_items.json", encoding="utf-8") as file:
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

