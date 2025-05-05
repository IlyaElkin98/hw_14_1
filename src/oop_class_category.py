from src.oop_class_product import Product


class Category:
    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products
        Category.product_count += len(products) if products else 0
        Category.category_count += 1

    def add_prod(self, product: Product):
        self.products.append(product)




