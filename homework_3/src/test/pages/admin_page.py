from selenium.webdriver.common.by import By
from homework_3.src.test.pages.base_page import BasePage


class AdminPageLocators:

    """ Locators for the Admin Page """

    page_url = 'http://3.122.51.38/litecart/admin'
    login_box = (By.CSS_SELECTOR, 'input.form-control[name=username]')
    password_box = (By.CSS_SELECTOR, 'input.form-control[name=password]')
    login_button = (By.CSS_SELECTOR, 'button[name=login]')

    ### LEFT SIDE-MENU ITEMS ###
    left_side_menu_items_locators = (
        (By.CSS_SELECTOR, 'ul#box-apps-menu li.app[data-code=appearance]'),
        (By.CSS_SELECTOR, 'li.doc[data-code=template]'),
        (By.CSS_SELECTOR, 'li.doc[data-code=logotype]'),
        (By.CSS_SELECTOR, 'ul#box-apps-menu li.app[data-code=catalog]'),
        (By.CSS_SELECTOR, 'li.doc[data-code=catalog]'),
        (By.CSS_SELECTOR, 'li.doc[data-code=attribute_groups]'),
        (By.CSS_SELECTOR, 'li.doc[data-code=manufacturers]'),
        (By.CSS_SELECTOR, 'li.doc[data-code=suppliers]'),
        (By.CSS_SELECTOR, 'li.doc[data-code=delivery_statuses]'),
        (By.CSS_SELECTOR, 'li.doc[data-code=sold_out_statuses]'),
        (By.CSS_SELECTOR, 'li.doc[data-code=quantity_units]'),
        (By.CSS_SELECTOR, 'li.doc[data-code=csv]'),
        (By.CSS_SELECTOR, 'ul#box-apps-menu li.app[data-code=countries]'),
        (By.CSS_SELECTOR, 'ul#box-apps-menu li.app[data-code=currencies]'),
        (By.CSS_SELECTOR, 'ul#box-apps-menu li.app[data-code=customers]'),
        (By.CSS_SELECTOR, 'li.doc[data-code=customers]'),
        (By.CSS_SELECTOR, 'li.doc[data-code=csv]'),
        (By.CSS_SELECTOR, 'li.doc[data-code=newsletter]'),
        (By.CSS_SELECTOR, 'ul#box-apps-menu li.app[data-code=geo_zones]'),
        (By.CSS_SELECTOR, 'ul#box-apps-menu li.app[data-code=languages]'),
        (By.CSS_SELECTOR, 'li.doc[data-code=languages]'),
        (By.CSS_SELECTOR, 'li.doc[data-code=storage_encoding]'),
        (By.CSS_SELECTOR, 'ul#box-apps-menu li.app[data-code=modules]'),
        (By.CSS_SELECTOR, 'li.doc[data-code=customer]'),
        (By.CSS_SELECTOR, 'li.doc[data-code=shipping]'),
        (By.CSS_SELECTOR, 'li.doc[data-code=payment]'),
        (By.CSS_SELECTOR, 'li.doc[data-code=order]'),
        (By.CSS_SELECTOR, 'li.doc[data-code=order_total]'),
        (By.CSS_SELECTOR, 'li.doc[data-code=jobs]'),
        (By.CSS_SELECTOR, 'ul#box-apps-menu li.app[data-code=orders]'),
        (By.CSS_SELECTOR, 'li.doc[data-code=orders]'),
        (By.CSS_SELECTOR, 'li.doc[data-code=order_statuses]'),
        (By.CSS_SELECTOR, 'ul#box-apps-menu li.app[data-code=pages]'),
        (By.CSS_SELECTOR, 'li.doc[data-code=pages]'),
        (By.CSS_SELECTOR, 'li.doc[data-code=csv]'),
        (By.CSS_SELECTOR, 'ul#box-apps-menu li.app[data-code=reports]'),
        (By.CSS_SELECTOR, 'li.doc[data-code=monthly_sales]'),
        (By.CSS_SELECTOR, 'li.doc[data-code=most_sold_products]'),
        (By.CSS_SELECTOR, 'li.doc[data-code=most_shopping_customers]'),
        (By.CSS_SELECTOR, 'ul#box-apps-menu li.app[data-code=settings]'),
        (By.CSS_SELECTOR, 'li.doc[data-code=store_info]'),
        (By.CSS_SELECTOR, 'li.doc[data-code=defaults]'),
        (By.CSS_SELECTOR, 'li.doc[data-code=email]'),
        (By.CSS_SELECTOR, 'li.doc[data-code=listings]'),
        (By.CSS_SELECTOR, 'li.doc[data-code=customer_details]'),
        (By.CSS_SELECTOR, 'li.doc[data-code=legal]'),
        (By.CSS_SELECTOR, 'li.doc[data-code=images]'),
        (By.CSS_SELECTOR, 'li.doc[data-code=checkout]'),
        (By.CSS_SELECTOR, 'li.doc[data-code=advanced]'),
        (By.CSS_SELECTOR, 'li.doc[data-code=security]'),
        (By.CSS_SELECTOR, 'ul#box-apps-menu li.app[data-code=slides]'),
        (By.CSS_SELECTOR, 'ul#box-apps-menu li.app[data-code=tax]'),
        (By.CSS_SELECTOR, 'li.doc[data-code=tax_rates]'),
        (By.CSS_SELECTOR, 'li.doc[data-code=tax_classes]'),
        (By.CSS_SELECTOR, 'ul#box-apps-menu li.app[data-code=translations]'),
        (By.CSS_SELECTOR, 'li.doc[data-code=search]'),
        (By.CSS_SELECTOR, 'li.doc[data-code=scan]'),
        (By.CSS_SELECTOR, 'li.doc[data-code=csv]'),
        (By.CSS_SELECTOR, 'ul#box-apps-menu li.app[data-code=users]'),
        (By.CSS_SELECTOR, 'ul#box-apps-menu li.app[data-code=vqmods]'),
    )


class AdminPage(BasePage, AdminPageLocators):

    """ Methods and helpers to work with the Admin Page """

    def open(self):
        self.driver.get(self.page_url)

    def login_to_the_system(self, credentials: dict):
        """ logs in to the on the admin page with the credentials provided as the parameters
            :param credentials: dict with keys {'username'} and {'password'}
        """
        self.driver.find_element(*self.login_box).send_keys(credentials['username'])
        self.driver.find_element(*self.password_box).send_keys(credentials['password'])
        self.driver.find_element(*self.login_button).click()
