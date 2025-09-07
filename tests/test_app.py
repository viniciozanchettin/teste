import unittest
from app.app import create_app

class WebTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app().test_client()

    def test_index(self):
        r = self.app.get("/")
        self.assertEqual(r.status_code, 200)
        self.assertIn(b"Bem-vindo", r.data)

    def test_about(self):
        r = self.app.get("/about")
        self.assertEqual(r.status_code, 200)
        self.assertIn(b"Sobre", r.data)

    def test_echo(self):
        r = self.app.post("/echo", data={"name": "Vinício"}, follow_redirects=True)
        self.assertEqual(r.status_code, 200)
        self.assertIn("Olá, Vinício!".encode("utf-8"), r.data)

if __name__ == "__main__":
    unittest.main()