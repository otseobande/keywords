def calculate_tf(term, document):
  """Calculates the frequency of a term in a document

  Args:
    term (str): The term (word) to find the frequency of.
    document (str): The document to search for the term in.

  Returns:
    float: The term frequency (tf)
  """

  term_list = [term.lower() for term in document.split()]
  num_of_words_in_doc = len(term_list)
  term_count_in_doc = term_list.count(term)

  return term_count_in_doc / num_of_words_in_doc

def calculate_idf(term, documents):
  """Calculates the total number of documents divided by the
  number of documents containing the term (word)

  Args:
    term (str): The term (word) to search for
    documents (list): A list of all the documents to search through

  Returns:
    float: The Inverse document frequency (idf)
  """

  num_of_docs = len(documents)
  documents_containing_term = len([document for document in documents if term in document])

  return num_of_docs / documents_containing_term
