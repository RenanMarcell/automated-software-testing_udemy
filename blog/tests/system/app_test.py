from unittest import TestCase
from unittest.mock import patch
from blog import Blog
import app


class AppTest(TestCase):
    def setUp(self):
        b = Blog('Test', 'Test Author')
        b.create_post('Test Post', 'Test Content')
        app.blogs = {'Test': b}

    def test_menu_calls_create_blog(self):
        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = ('c', 'Test Title', 'Test Author', 'q')
            app.menu()
            self.assertIsNotNone(app.blogs.get('Test Title'))

    @staticmethod
    def test_menu_options():
        with patch('builtins.input', return_value='q') as mocked_input:
            app.menu()
            mocked_input.assert_called_with(app.MENU_PROMPT)

    @staticmethod
    def test_menu_calls_print_blogs():
        with patch('app.print_blogs') as mocked_print_blogs:
            with patch('builtins.input', return_value='q'):
                app.menu()
                mocked_print_blogs.assert_called_with()

    @staticmethod
    def test_print_blogs():
        b = app.blogs.get('Test')
        with patch('builtins.print') as mocked_print:
            app.print_blogs()
            mocked_print.assert_called_with('- {}'.format(b))

    def test_ask_create_blog(self):
        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = ('Teste', 'Test Author')
            app.ask_create_blog()

            self.assertIsNotNone(app.blogs.get('Teste'))

    @staticmethod
    def test_ask_read_blog():
        with patch('builtins.input', return_value='Test'):
            with patch('builtins.print') as mocked_print:
                app.ask_read_blog()
                mocked_print.assert_called_with('{}\n{}'.format('Test Post', 'Test Content'))

    def test_ask_create_post(self):
        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = ('Test Post', 'Test Content', 'Test')
            self.assertTrue(len(app.blogs.get('Test').posts) > 0)
