from app.test.system.base_test import BaseTest


class HomeTest(BaseTest):
    def test_home(self):
        with self.app() as c:
            resp = c.get('/')
            self.assertEqual(resp.status_code, 200)
