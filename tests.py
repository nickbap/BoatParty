import unittest

from werkzeug import generate_password_hash, check_password_hash
from boatparty import create_app, db, mail
from boatparty.models import GuestBookPost, User
from boatparty.utils import convert_markdown_to_html, send_email_notification
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

    def test_admin_page(self):
        response = self.client.get('/admin')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(
            'placeholder="Email"' in response.get_data(as_text=True))

    def test_404_handler(self):
        response = self.client.get('/foo')
        self.assertEqual(response.status_code, 404)
        self.assertTrue('cannot be found!' in response.get_data(as_text=True))

    def test_post_email_notifications(self):
        with mail.record_messages() as outbox:
            send_email_notification(
                'Test Sender', 'Test Message', 'guest book post')
        assert len(outbox) == 1
        assert outbox[0].subject == 'New Guest Book Post from Test Sender'

    def test_question_email_notifications(self):
        with mail.record_messages() as outbox:
            send_email_notification('Test Sender', 'Test Question', 'question')
        assert len(outbox) == 1
        assert outbox[0].subject == 'New Question from Test Sender'


class AdminTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app(TestingConfig)
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        self.client = self.app.test_client()
        # Test user
        self.username = 'Admin'
        self.email = 'admin@boatparty.com'
        self.password = 'admin_password'

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_add_admin_user(self):
        password = generate_password_hash(self.password)
        new_user = User(username=self.username, email=self.email, password=password)
        db.session.add(new_user)
        db.session.commit()
        test_user = User.query.filter_by(username='Admin').first()
        self.assertTrue(test_user.email, self.email)

    def test_admin_login(self):
        data = {'email': self.email, 'password': self.password}
        response = self.client.post(
            '/admin', data=data, follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_delete_post(self):
        # Create Admin
        password = generate_password_hash(self.password)
        new_user = User(username=self.username, email=self.email, password=password)
        db.session.add(new_user)
        db.session.commit()
        test_user = User.query.filter_by(username='Admin').first()
        self.assertTrue(test_user.email, self.email)
        # Create 1st Post
        name = 'Test Poster 1'
        md = '# Markdown Header 1'
        html = convert_markdown_to_html(md)
        data = {'name': name,
                'pagedown': md}
        response = self.client.post(
            '/guest-book', data=data, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(html in response.get_data(as_text=True))
        post_one  = GuestBookPost.query.filter_by(id=1).first()
        self.assertTrue(post_one.id, 1)
        # Create 2nd Post
        name2 = 'Test Poster 2'
        md2 = '# Markdown Header 2'
        html2 = convert_markdown_to_html(md2)
        data2 = {'name': name2,
                'pagedown': md2}
        response2 = self.client.post(
            '/guest-book', data=data2, follow_redirects=True)
        self.assertEqual(response2.status_code, 200)
        self.assertTrue(html2 in response2.get_data(as_text=True))
        post_two  = GuestBookPost.query.filter_by(id=2).first()
        self.assertTrue(post_two.id, 2)
        # Log in as Admin
        data3 = {'email': self.email, 'password': self.password}
        response3 = self.client.post(
            '/admin', data=data3, follow_redirects=True)
        self.assertEqual(response3.status_code, 200)
        # The correct modal targets should be populated with post ids
        self.assertTrue('#postDeleteWarningModal1' in response3.get_data(as_text=True))
        self.assertTrue('#postDeleteWarningModal2' in response3.get_data(as_text=True))
        # Delete 1st Post Only
        response4 = self.client.post(
            '/delete/{}'.format(post_one.id), follow_redirects=True)
        self.assertEqual(response4.status_code, 200)
        self.assertFalse('#postDeleteWarningModal1' in response4.get_data(as_text=True))
        self.assertTrue('#postDeleteWarningModal2' in response4.get_data(as_text=True))


if __name__ == '__main__':
    unittest.main(verbosity=2)
