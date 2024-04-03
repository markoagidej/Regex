# Task 1: Product Description Keyword Tagging

import re

descriptions = [
    "Smartphone with 6-inch screen and 128GB memory",
    "Cotton t-shirt in medium size",
    "Stainless steel kitchen knife set"
]

tags = {
    "Electronics": [],
    "Apparel": [],
    "Home&Kitchen": []
}

def tag_product_by_description(description):
    electronics_pattern = r"\b(screen|memory|phone)\b"
    apparel_pattern = r"\b(shirt|cotton)\b"
    home_pattern = r"\b(kitchen|knife)\b"

    if re.search(electronics_pattern, description):
        return "Electronics"
    elif re.search(apparel_pattern, description):
        return "Apparel"
    elif re.search(home_pattern, description):
        return "Home&Kitchen"

def tag_product_list(product_list, tags_list):
    for description in product_list:
        tags_list[tag_product_by_description(description)].append(description)

    for key, value in tags.items():
        print(f"{key}: {value}")


tag_product_list(descriptions, tags)


# Task 2: Pricing Format Standardization

price_data = "Items cost $15.99, 20.00 USD, and 7.50$."

def price_formatter(prices):
    final_price_pattern = (r"USD \1")

    old_price_formats = [
        r"\$(\d*\.\d{2})",
        r"\b(\d*\.\d{2}) USD",
        r"\b(\d*\.\d{2})\$",
    ]

    for price_format in old_price_formats:
        prices = re.sub(price_format, final_price_pattern, prices)

    print(prices)

price_formatter(price_data)