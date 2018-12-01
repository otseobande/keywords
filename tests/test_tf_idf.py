from tf_idf import *

def test_calculate_tf():
  """The calculate_tf function should return the right term frequency"""

  assert calculate_tf('the', 'The man is the king') == 0.4

def test_calculate_idf():
  """The calculate_idf function"""

  assert calculate_idf('food', ['the food is cold', 'I dont want this food']) == 1.0
  assert calculate_idf('food', ['the food is cold', 'lets go out']) == 2.0
