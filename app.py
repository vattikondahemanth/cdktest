from flask import Flask, current_app
import unittest

from discountmanager import DiscountManager
from models import OrderDetails, Discount
from constants import REGULAR_CUSTOMER, PREMIUM_CUSTOMER

app = Flask(__name__)


@app.route('/add')
def add():
	DiscountManager.add_all_discounts()
	return "added the data"

@app.route('/remove')
def remove():
	DiscountManager.remove_all_discounts()
	return "removed all the data"

@app.route('/')
def hello():
	return 'hello world'


class TestDiscountMethods(unittest.TestCase):

	discount_manager = DiscountManager()

	def calculate_discount(self, customer_type, purchase_amount):
		order_details = OrderDetails(customer_type, purchase_amount)
		discount = TestStringMethods.discount_manager.calculate_discount(order_details)
		return abs(order_details.purchase_amount - discount)

	def test_discounts(self):
		self.assertEqual(self.calculate_discount(REGULAR_CUSTOMER, 5000), 5000.0)
		self.assertEqual(self.calculate_discount(REGULAR_CUSTOMER, 10000), 9500.0)
		self.assertEqual(self.calculate_discount(REGULAR_CUSTOMER, 15000), 13500.0)

		self.assertEqual(self.calculate_discount(PREMIUM_CUSTOMER, 4000), 3600.0)
		self.assertEqual(self.calculate_discount(PREMIUM_CUSTOMER, 8000), 7000.0)
		self.assertEqual(self.calculate_discount(PREMIUM_CUSTOMER, 12000), 10200.0)
		self.assertEqual(self.calculate_discount(PREMIUM_CUSTOMER, 20000), 15800.0)


if __name__ == '__main__':
	unittest.main()