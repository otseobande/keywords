from tf_idf import *

def test_get_tf():
  """The get_tf function should return the right term frequency"""

  assert get_tf('the', 'The man is the king') == 0.4

def test_get_idf():
  """The get_idf function should return the right idf"""

  assert get_idf('food', ['the food is cold', 'I dont want this food']) == 0.0
  assert get_idf('food', ['the food is cold', 'lets go out']) == 0.30103

def test_get_tf_idf():
  """The get_tf_idf function should return the product of the tf and idf"""

  assert get_tf_idf('food', 'the food is cold', ['the food is cold', 'lets go out']) == 0.07526
