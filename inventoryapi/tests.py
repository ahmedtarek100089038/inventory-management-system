from django.test import TestCase

from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

class SupplierTests(APITestCase):
    def test_get_supplier(self):
        user = User.objects.create_user('test', 'test@test.com', 'testsecret')
        self.client = APIClient()
        self.client.force_authenticate(user=user) 
             
        data = {'name': 'Ahmed'}
        self.client.post('/api/supplier/', data, format='json')
        
        data1 = {'name': 'Tarek'}
        self.client.post('/api/supplier/', data1, format='json')
        
        response = self.client.get('/api/supplier/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_get_a_supplier(self):
        user = User.objects.create_user('test', 'test@test.com', 'testsecret')
        self.client = APIClient()
        self.client.force_authenticate(user=user) 
             
        data = {'name': 'Ahmed'}
        self.client.post('/api/supplier/', data, format='json')
        
        response = self.client.get('/api/supplier/1/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_update_supplier(self):
        user = User.objects.create_user('test', 'test@test.com', 'testsecret')
        self.client = APIClient()
        self.client.force_authenticate(user=user) 
        
        data = {'name': 'Ahmed'}
        self.client.post('/api/supplier/', data, format='json')
        
        data_update = {'name': 'Soap'}
        response = self.client.put('/api/supplier/1/', data_update, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_delete_supplier(self):
        user = User.objects.create_user('test', 'test@test.com', 'testsecret')
        self.client = APIClient()
        self.client.force_authenticate(user=user) 
             
        data = {'name': 'Ahmed'}
        self.client.post('/api/supplier/', data, format='json')
        
        response = self.client.delete('/api/supplier/1', format='json')
        self.assertEqual(response.status_code, status.HTTP_301_MOVED_PERMANENTLY)
        
class InventoryTests(APITestCase):
    def test_get_inventory(self):
        user = User.objects.create_user('test', 'test@test.com', 'testsecret')
        self.client = APIClient()
        self.client.force_authenticate(user=user) 
             
        data = {'name': 'Ahmed'}
        self.client.post('/api/supplier/', data, format='json')
        
        data_inventory = {    
                        "name": "Soap",
                        "description": "Smells good",
                        "note": "Test",
                        "stock": 3,
                        "availability": False,
                        "supplier": [1]
                        }
        
        self.client.post('/api/inventory/', data_inventory, format='json')
        
        response = self.client.get('/api/inventory/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_get_a_inventory(self):
        user = User.objects.create_user('test', 'test@test.com', 'testsecret')
        self.client = APIClient()
        self.client.force_authenticate(user=user) 
             
        data = {'name': 'Ahmed'}
        self.client.post('/api/supplier/', data, format='json')
        
        data_inventory = {    
                        "name": "Shampoo",
                        "description": "Good Quality",
                        "note": "Test",
                        "stock": 2,
                        "availability": False,
                        "supplier": [1]
                }
        
        self.client.post('/api/inventory/', data_inventory, format='json')
        
        response = self.client.get('/api/inventory/1/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_update_inventory(self):
        user = User.objects.create_user('test', 'test@test.com', 'testsecret')
        self.client = APIClient()
        self.client.force_authenticate(user=user) 
        
        data_supplier = {'name': 'Ahmed'}
        self.client.post('/api/supplier/', data_supplier, format='json')
        
        data_inventory = {    
                        "name": "Soap",
                        "description": "Smells good",
                        "note": "Test",
                        "stock": 3,
                        "availability": False,
                        "supplier": [1]
                }
        
        self.client.post('/api/inventory/', data_inventory, format='json')
        
        data_update = {    
                        "name": "Soap",
                        "description": "Smells good",
                        "note": "Test",
                        "stock": 0,
                        "availability": True,
                        "supplier": [1]
                        }
        response = self.client.put('/api/inventory/1/', data_update, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_delete_inventory(self):
        user = User.objects.create_user('test', 'test@test.com', 'testsecret')
        self.client = APIClient()
        self.client.force_authenticate(user=user) 
             
        data_supplier = {'name': 'Ahmed'}
        self.client.post('/api/supplier/', data_supplier, format='json')
        
        data_inventory = {    
                "name": "Soap",
                "price": 1.00,
                "qty": 5,
                "out_of_stock": False,
                "supplier": [1]
                }
        
        self.client.post('/api/inventory/', data_inventory, format='json')
        response = self.client.delete('/api/inventory/1', format='json')
        self.assertEqual(response.status_code, status.HTTP_301_MOVED_PERMANENTLY)
