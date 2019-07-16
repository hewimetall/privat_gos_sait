from decimal import Decimal
from django.conf import settings
from product_category.models import items_cat as Product
from .forms import CartAddProductForm ,Cart_one_prod

class Cart(object):
    """
    slug is pole of id from cart

    """
    def __init__(self, request):
        # Инициализация корзины пользователя
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # Сохраняем корзину пользователя в сессию
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    # Добавление товара в корзину пользователя или обновление количеста товара
    def add(self, product, quantity=1, update_quantity=False):
        product_id = str(product.slug)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0,
                                     'price': str(product.price)}
        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()

    # Сохранение данных в сессию
    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        # Указываем, что сессия изменена
        self.session.modified = True

    def remove(self, product):
        product_id = str(product.slug)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def forms_market(selfs):
        f=CartAddProductForm()
        return f

    def forms_for_1(selfs):
        f=Cart_one_prod()
        return f

    # Итерация по товарам
    def __iter__(self):
        product_ids = self.cart.keys()# cart is dict
        products = Product.objects.filter(slug__in=product_ids)
        for product in products:
            self.cart[str(product.slug)]['product'] = product
        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item


    # Количество товаров
    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True

    def get_total_price_after_discount(self):
        return self.get_total_price()
