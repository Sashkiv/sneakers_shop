from django import test


class TestMainRequests(test.TestCase):

    def test_request_index_response_200(self):
        r = self.client.get('/')
        self.assertEquals(r.status_code, 200)
        self.assertTrue(r.content.decode('utf-8').strip('\n'))

    def test_request_about_response_200(self):
        r = self.client.get('/about/')
        self.assertEquals(r.status_code, 200)
        self.assertTrue(r.content.decode('utf-8').strip('\n'))

    def test_request_contacts_response_200(self):
        r = self.client.get('/contacts/')
        self.assertEquals(r.status_code, 200)
        self.assertTrue(r.content.decode('utf-8').strip('\n'))

    def test_request_catalog_response_200(self):
        r = self.client.get('/catalog/')
        self.assertEquals(r.status_code, 200)
        self.assertTrue(r.content.decode('utf-8').strip('\n'))

    def test_google_verification_response_200(self):
        r = self.client.get('/google4346c5c573bda2ea.html')
        self.assertEquals(r.status_code, 200)
        self.assertTrue(r.content.decode('utf-8').strip('\n'))
