import os
import pickle

from models import OrderDetails, Discount
from constants import REGULAR_CUSTOMER, PREMIUM_CUSTOMER



class DiscountManager(object):
	"""This is used to calculate discount"""
	def __init__(self):
		super(DiscountManager, self).__init__()

	def calculate_discount(self, order_details):
		total_discount = 0
		for each_discount in self.get_all_discounts():
			if order_details.customer_type != each_discount.customer_type:
				continue

			if order_details.purchase_amount < each_discount.min_amount:
				continue
			
			if each_discount.max_amount:
				max_amount = each_discount.max_amount if order_details.purchase_amount > each_discount.max_amount else order_details.purchase_amount
			else:
				max_amount = order_details.purchase_amount

			discount_price = ((max_amount - each_discount.min_amount)*each_discount.percentage)/100			

			total_discount += discount_price

		return total_discount

		if not isinstance(order_details, OrderDetails):
			raise TypeError('argument should be of type <OrderDetails>') 

	def add_discount(self, discount_obj):
		if not isinstance(discount_obj, Discount):
			raise TypeError('argument should be of type <Discount>')

		dbfile = open('discount_table', 'ab')
		pickle.dump(discount_obj, dbfile)


	def update_discount(self, discount_obj):
		if not isinstance(discount_obj, Discount):
			raise TypeError('argument should be of type <Discount>')

		all_discounts = DiscountManager.get_all_discounts()
		

		filtered_objs = filter(filter_discounts(x), all_discounts)


	@staticmethod
	def add_all_discounts():
		if os.path.exists('discount_table'):
			raise FileExistsError('File Already Exists')

		all_objs = [
		Discount(REGULAR_CUSTOMER, 0, 0, 5000),
		Discount(REGULAR_CUSTOMER, 10, 5000, 10000),
		Discount(REGULAR_CUSTOMER, 20, 10000),
		Discount(PREMIUM_CUSTOMER, 10, 0, 4000),
		Discount(PREMIUM_CUSTOMER, 15, 4000, 8000),
		Discount(PREMIUM_CUSTOMER, 20, 8000, 12000),
		Discount(PREMIUM_CUSTOMER, 30, 12000)
		]
		dbfile = open('discount_table', 'ab')

		for discount_obj in all_objs:
			pickle.dump(discount_obj, dbfile)

	@staticmethod
	def remove_all_discounts():
		os.remove('discount_table')

	@staticmethod
	def get_all_discounts():
		with open('discount_table', "rb") as f:
			while True:
				try:
					yield pickle.load(f)
				except EOFError:
					break

