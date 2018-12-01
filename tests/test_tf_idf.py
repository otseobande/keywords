from tf_idf import *

def test_calculate_tf():
  """calculate_tf function should return the right term frequency"""

  document = 'The man is the king'

  assert calculate_tf('the', document) == 0.4
