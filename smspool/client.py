import requests


class smspool():

    def __init__(self, apikey: str, base_url: str = "https://smspool.net/api/"):
        self.apikey = apikey
        self.base_url = base_url

        self.session = requests.Session()

    # SMS

    def get_countries(self):
        """
        Returns the list of countries supported by smspool.net
        """
        url = self.base_url + "country/retrieve_all"
        response = self.session.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(response.text)

    def get_services(self, country: str = "United States"):
        """
        Returns the list of services supported by smspool.net in the given country
        """
        url = self.base_url + "service/retrieve_all"
        response = self.session.get(url, params={"country": country})
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(response.text)

    def get_balance(self):
        """
        Returns the balance of the account
        """
        url = self.base_url + "request/balance"
        response = self.session.get(url, params={'key': self.apikey})
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(response.text)

    def get_order_history(self):
        """
        Returns the order history of the account
        """
        url = self.base_url + "request/history"
        response = self.session.get(url, params={'key': self.apikey})
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(response.text)

    def get_active_orders(self):
        """
        Returns the active orders of the account
        """
        url = self.base_url + "request/active"
        response = self.session.get(url, params={'key': self.apikey})

        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(response.text)

    def get_service_price(self, country: str = "United States", service: str = "Discord", pool: str = None):
        """
        Returns the price of the service in the given country
        """
        url = self.base_url + "request/price"
        if pool is not None:
            params = {'key': self.apikey, 'country': country, 'service': service, 'pool': pool}
        else:
            params = {'key': self.apikey, 'country': country, 'service': service}
        response = self.session.get(url, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(response.text)

    def purchase_sms(self, country: str = "United States", service: str = "Discord", pool: str = None):
        """
        Purchases the service in the given country
        """
        url = self.base_url + "purchase/sms"
        if pool is not None:
            params = {'key': self.apikey, 'country': country, 'service': service, 'pool': pool}
        else:
            params = {'key': self.apikey, 'country': country, 'service': service}
        response = self.session.get(url, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(response.text)

    def check_sms(self, order_id: int = None):
        """
        Checks the status of the order
        """
        url = self.base_url + "sms/check"
        response = self.session.get(url, params={'key': self.apikey, 'order_id': order_id})
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(response.text)

    def resend_sms(self, order_id: int = None):
        """
        Resends the SMS
        """
        url = self.base_url + "sms/resend"
        response = self.session.get(url, params={'key': self.apikey, 'order_id': order_id})
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(response.text)

    def cancel_sms(self, order_id: int = None):
        """
        Cancels the SMS
        """
        url = self.base_url + "sms/cancel"
        response = self.session.get(url, params={'key': self.apikey, 'order_id': order_id})
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(response.text)

    def archive_sms_orders(self):
        """
        Archives the SMS orders
        """
        url = self.base_url + "request/archive"
        response = self.session.get(url, params={'key': self.apikey})
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(response.text)

    # Rentals

    def get_rentals(self, type: int = 0):
        """
        Returns the list of rentals
        """
        url = self.base_url + "rental/retrieve_all"
        response = self.session.get(url, params={'type': type})
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(response.text)

    def purchase_rental(self, rental_id: int = None, days: int = 1, service_id: int = None):
        """
        Purchases the rental
        """
        if service_id is not None:
            params = {'key': self.apikey, 'rental_id': rental_id, 'days': days, 'service_id': service_id}
        else:
            params = {'key': self.apikey, 'rental_id': rental_id, 'days': days}
        url = self.base_url + "purchase/rental"
        response = self.session.get(url, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(response.text)

    def get_rental_message(self, rental_code : int = None):
        """
        Returns the rental message
        """
        url = self.base_url + "rental/retrieve_messages"
        response = self.session.get(url, params={'key': self.apikey, 'rental_code': rental_code})
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(response.text)

    def get_rental_status(self, rental_code: int = None):
        """
        Returns the rental status
        """
        url = self.base_url + "rental/retrieve_status.php"
        response = self.session.get(url, params={'key': self.apikey, 'rental_code': rental_code})
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(response.text)

    def refund_rental(self, rental_code: int = None):
        """
        Refunds the rental
        """
        url = self.base_url + "rental/refund.php"
        response = self.session.get(url, params={'key': self.apikey, 'rental_code': rental_code})
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(response.text)

    def extend_rental(self, rental_code: int = None, days: int = 1):
        """
        Extends the rental
        """
        url = self.base_url + "rental/extend.php"
        response = self.session.get(url, params={'key': self.apikey, 'rental_code': rental_code, 'days': days})
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(response.text)