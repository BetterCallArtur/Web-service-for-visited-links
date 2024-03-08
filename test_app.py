import unittest
from app import app, db

class TestVisitedLinksService(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app = app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_add_visited_links(self):
        response = self.app.post('/visited_links', json={'links': ['https://example.com']})
        self.assertEqual(response.status_code, 200)

    def test_get_visited_domains(self):
        self.app.post('/visited_links', json={'links': ['https://example.com']})
        response = self.app.get('/visited_domains?from=0&to=9999999999')
        self.assertEqual(response.status_code, 200)
        self.assertIn('example.com', response.json['domains'])

if __name__ == '__main__':
    unittest.main()
