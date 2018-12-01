def calculate_tf(term, document):
  """Calculates the frequency of a term in a document

  Returns:
    float: term frequency
  """

  term_list = [term.lower() for term in document.split()]
  num_of_words_in_doc = len(term_list)
  term_count_in_doc = term_list.count(term)

  return term_count_in_doc / num_of_words_in_doc
