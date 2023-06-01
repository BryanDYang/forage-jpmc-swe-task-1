import unittest
from client3 import getDataPoint
from client3 import getRatio

class ClientTest(unittest.TestCase):
  def __init__(self, methodName: str = ...):
    super().__init__(methodName)
    self.calculator = None

  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], (quote['top_bid']['price'] + quote['top_ask']['price'])/2))

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
     self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], (quote['top_bid']['price'] + quote['top_ask']['price'])/2))

  """ ------------ Add more unit tests ------------ """

  # The assertion: normal price testing for getRatio method
  def test_getRatio_calculateRatio(self):

    prices = [
      120.2, 121.68,
      120.48, 117.87,
      119.2, 121.68,
      120.48, 117.87
    ]

    for price in range(0, len(prices), 2):
      self.assertEqual((prices[price]/prices[price+1]), getRatio(prices[price],prices[price+1]))

  # The assertion: testing getRatio method if non is return when divided by zero
  def test_getRatio_zeroDivisionError(self):
    with self.assertRaises(ZeroDivisionError):
      self.assertEqual(None, getRatio(120.2, 0))

if __name__ == '__main__':
    unittest.main()
