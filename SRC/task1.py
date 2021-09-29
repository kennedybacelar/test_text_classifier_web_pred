def verify_political_or_non_political(sample, reference_array):

  response = []

  for single_element in sample:
    if str(single_element).lower() in reference_array:
      response.append(1)
      continue
    response.append(0)

  return response


