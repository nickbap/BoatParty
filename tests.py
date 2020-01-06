import unittest
from boatparty import create_app, db
from boatparty.models import GuestBookPost
from boatparty.utils import convert_markdown_to_html
from config import TestingConfig


class GuestBookPostModelTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app(TestingConfig)
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_new_post(self):
        name = 'Unit Tester'
        post_md = '# Markdown Test'
        post_html = convert_markdown_to_html(post_md)
        post = GuestBookPost(name=name, post_md=post_md, post_html=post_html)
        db.session.add(post)
        db.session.commit()
        p = GuestBookPost.query.first()
        self.assertEqual(p.name, 'Unit Tester')
        self.assertEqual(p.post_md, '# Markdown Test')
        self.assertEqual(p.post_html, '<h1>Markdown Test</h1>\n')


class ClientTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app(TestingConfig)
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        self.client = self.app.test_client()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_index_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('Nick & Natalie' in response.get_data(as_text=True))

    def test_home_page(self):
        response = self.client.get('/home')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('Nick & Natalie' in response.get_data(as_text=True))

    def test_photos_page(self):
        response = self.client.get('/photos')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('photo-gallery' in response.get_data(as_text=True))
        # check that get_gallery_photos is working
        self.assertTrue(
            'NickNatalie-01.jpg' in response.get_data(as_text=True))

    def test_the_big_day_page(self):
        response = self.client.get('/the-big-day')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('The Big Day' in response.get_data(as_text=True))

    def test_guest_book_page(self):
        response = self.client.get('/guest-book')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('Guest Book' in response.get_data(as_text=True))

    def test_guest_book_post(self):
        name = 'Test Poster'
        md = '# Markdown Header'
        html = convert_markdown_to_html(md)
        data = {'name': name,
                'pagedown': md}
        response = self.client.post(
            '/guest-book', data=data, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(html in response.get_data(as_text=True))

    def test_where_to_stay_page(self):
        response = self.client.get('/where-to-stay')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('Where to Stay' in response.get_data(as_text=True))

    def test_faq_page(self):
        response = self.client.get('/faq')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(
            'Frequently Asked Questions' in response.get_data(as_text=True))


if __name__ == '__main__':
    unittest.main(verbosity=2)
