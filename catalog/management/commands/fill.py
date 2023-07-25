from django.core.management import BaseCommand

from catalog.models import Product


class Command(BaseCommand):

    def handle(self, *args, **options):
        product_list = [
            {'name': 'яблоко', 'description': 'зеленое'},
            {'name': 'банан', 'description': 'желтый'},
            {'name': 'апельсин', 'description': 'оранжевый'},
        ]

        product_for_create = []
        for product_item in product_list:
            product_for_create.append(
                Product(**product_item)
            )

        Product.objects.bulk_create(product_for_create)
