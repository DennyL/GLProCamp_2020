from homeworks_3_4.src.test.generators import generators


class Credentials:

    admin_credentials = (
        {'username': 'admin', 'password': 'gl_admin'},
    )


class Product:
    """
       used to create product instances with random fields
    """
    def __init__(self):

        # GENERAL
        self.product_name = generators.item_names_generator(length=8)
        self.code = generators.item_codes_generator(length=3)
        self.sku = generators.item_codes_generator(length=4)
        self.mpn = generators.item_codes_generator(length=2)
        self.gtin = generators.item_codes_generator(length=5)
        self.taric = generators.item_codes_generator(length=5)
        self.manufacturer = '1'
        self.date_valid_from = '10/02/2019'
        self.date_valid_to = '11/03/2020'
        self.keywords = self.product_name[:8]
        self.image = generators.item_picture_provider()

        # INFORMATION
        self.short_description = 'Nice thing to purchase'
        self.description = 'Superb quality goods from Ukrainian farmers'
        self.technical_data = 'Contact the dealer'
        self.head_title = 'Head Title'
        self.meta_description = 'Meta description is missing'

        # PRICES
        self.tax_class = 'first'
        self.purchase_price = '50'
        self.purchase_price_currency = 'USD'
        self.price_usd = '50'

    def __str__(self):
        """ displays of the fields of a product instance """
        product_info = []
        for k, v in self.__dict__.items():
            product_info.append(f'\n{k.upper()} : {str(v)}')
        return ''.join(product_info)
