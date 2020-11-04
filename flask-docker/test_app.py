import unittest
import requests
import os

class FlaskTest(unittest.TestCase):
    def setUp(self):
        os.environ['NO_PROXY'] = '0.0.0.0'
        self.user = {
            'uid': 312,
            'fname': 'fname312',
            'lname': 'lname312',
            'credit': 0
        }

    def tearDown(self):
        pass

    def test_add_user(self):
        payload = {
            'uid': self.user['uid'],
            'fname': self.user['fname'],
            'lname': self.user['lname'],
            'form_type': 'add_user'
        }
        response = requests.post('http://localhost:5000', data=payload)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b'success')
    
    def test_add_credit(self):
        payload = {
            'uid': self.user['uid'],
            'credit': self.user['credit'],
            'form_type': 'add_credit'
        }
        response = requests.post('http://localhost:5000', data=payload)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b'success') 

    def test_view_user(self):
        payload = {
            'uid': self.user['uid'],
            'form_type': 'view_user'
        }
        response = requests.post('http://localhost:5000', data=payload)

        user_data = "fname: {}, lname: {}, credits: {}".format(
            self.user['fname'],
            self.user['lname'],
            self.user['credit'])

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, user_data.encode()) 

if __name__ == "__main__":
    unittest.main()