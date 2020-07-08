from constants import CUSTOMER_TYPE

class OrderDetails(object):
	"""this will hold the order details"""

	def __init__(self, customer_type, purchase_amount):
		super(OrderDetails, self).__init__()
		try:
			purchase_amount = int(purchase_amount)
			if purchase_amount < 0:
				raise ValueError
		except ValueError as e:
			raise Exception("purchase_amount must be a positive integer")

		if customer_type not in CUSTOMER_TYPE:
			raise Exception("customer_type must be one of " + ','.join(CUSTOMER_TYPE))
		

		self.customer_type = customer_type
		self.purchase_amount = purchase_amount


class Discount(object):
	"""details for Discount"""
	def __init__(self, customer_type, percentage, min_amount, max_amount=None):
		super(Discount, self).__init__()
		self.min_amount = min_amount
		self.max_amount = max_amount
		self.percentage = percentage
		self.customer_type = customer_type