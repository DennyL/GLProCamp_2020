from homework_3.src.test.generators import generators


class Credentials:

    admin_credentials = (
        {'username': 'admin', 'password': 'gl_admin'},
    )


class LitecartProduct:

    def __init__(self):
        self.product_name = generators.item_name_generator()
