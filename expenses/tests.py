from rest_framework.test import APITestCase
from .models import Expense
"""
added tests

"""

class ExpenseAPITestCase(APITestCase):

    def setUp(self):
        Expense.objects.create(name="Lunch", amount=10.50, category="Food")
        Expense.objects.create(name="Bus Ticket", amount=2.75, category="Transport")
        Expense.objects.create(name="Movie", amount=15.00, category="Entertainment")

    def test_get_expenses(self):
        response = self.client.get('/api/expenses/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 3)

    def test_create_expense(self):
        data = {"name": "Dinner", "amount": 20.00, "category": "Food"}
        response = self.client.post('/api/expenses/', data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Expense.objects.count(), 4)

    def test_expenses_update(self):
        expense = Expense.objects.first()
        data = {"name": "Updated Lunch", "amount": 12.00, "category": "Food"}
        response = self.client.put(f'/api/expenses/{expense.id}/', data, format='json')
        self.assertEqual(response.status_code, 200)
        expense.refresh_from_db()
        self.assertEqual(expense.name, "Updated Lunch")
        self.assertEqual(float(expense.amount), 12.00)

    def test_expenses_delete(self):
        expense = Expense.objects.first()
        response = self.client.delete(f'/api/expenses/{expense.id}/')
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Expense.objects.count(), 2)
        self.assertFalse(Expense.objects.filter(id=expense.id).exists())