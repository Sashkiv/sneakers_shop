import os

from django import test


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

    def test_get_sneakers_filter_response_200(self):
        r = self.client.get('/sneakers/?brand=0&sex=0')
        self.assertEquals(r.status_code, 200)
        self.assertTrue(r.content.decode('utf-8').strip('\n'))
