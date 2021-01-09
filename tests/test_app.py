from flask import Flask
from pytest import fixture
from src import create_app
from unittest import TestCase, main

@fixture
def client():
    app = create_app()
    app.testing = True
    with app.test_client() as client:
        yield client

class TestApp(TestCase):

    def setUp(self):
        self.app = create_app()
        self.app.testing = True
        self.client = self.app.test_client()
 
    def test_index_get(self):
        rv = self.client.get('/')
        resp = rv.get_data(as_text=True)
        self.assertEqual(resp, 'Welcome to the Python Disassembler Service')

    def test_index_with_code(self):
        rv = self.client.post('/', json={
            'code': 'print("hi")'
        })
        resp = rv.get_data(as_text=True)
        self.assertNotEqual(resp, '')

    def test_index_missing_code(self):
        rv = self.client.post('/', json={
            'email': 'flask@example.com', 'password': 'secret'
        })
        resp = rv.get_data(as_text=True)
        self.assertEqual(resp, '')

if __name__ == '__main__': 
    main()