import os

from django import test
from test_tools import data_provider, FixtureManager

fx_urls = FixtureManager()
fx_urls.load(fixture_file='data_urls_filter')


class TestSneakersRequests(test.TestCase):

    fixtures = [
        os.path.dirname(__file__) + '/fixtures/db_data.json',
    ]

    def test_get_all_sneakers_response_200(self):
        r = self.client.get('/sneakers/')
        self.assertEquals(r.status_code, 200)
        self.assertTrue(r.content.decode('utf-8').strip('\n'))

    def test_get_sneakers_by_pk_response_200(self):
        r = self.client.get('/sneakers/1/')
        self.assertEquals(r.status_code, 200)
        self.assertTrue(r.content.decode('utf-8').strip('\n'))

    @data_provider(fx_urls['urls'])
    def test_get_sneakers_filter_response_200(self, params):
        r = self.client.get('/sneakers/?'+params)
        self.assertEquals(r.status_code, 200)
        self.assertTrue(r.content.decode('utf-8').strip('\n'))

    def test_get_list_promo_response_200(self):
        r = self.client.get('/sneakers/promo_list/')
        self.assertEquals(r.status_code, 200)
        self.assertTrue(r.content.decode('utf-8').strip('\n'))
