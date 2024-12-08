import unittest
from app import app

'''Unit test for the Smart House Weather Dashboard application'''

class TestRoutes(unittest.TestCase):
    def setUp(self): # Set up the app for testing
        self.app = app.test_client()

    def test_landing_page(self): # Test the Landing page route
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Smart', response.data)

    def test_temperature(self): # Test the temperature route
        response = self.app.get('temperature')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Temperature', response.data)

    def test_humidity(self): # Test the humidity route
        response = self.app.get('humidity')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Humidity', response.data)

    def test_weather(self): # Test the weather route
        response = self.app.get('weather')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Weather', response.data)

    def test_weather_maps(self): # Test the weather maps route
        response = self.app.get('weathermaps')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Weather Maps', response.data)


if __name__ == '__main__':
    unittest.main() # Run the tests