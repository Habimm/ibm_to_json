from info import info
import json
import re

# See: https://www.ibm.com/docs/en/icos/12.9.0?topic=problem-typical-integer-program-knapsack

def handle(pb2_request, repo_path):
  ibm = pb2_request.input.decode('utf-8')

  info(ibm)
  searched_dat = re.search("Capacity[\s=]*(?P<capacities>\[.*);", ibm)
  capacities = searched_dat.group('capacities')

  searched_dat = re.search("Value[\s=]*(?P<values>\[.*);", ibm)
  values = searched_dat.group('values')

  searched_dat = re.search("Use[\s=]*(?P<weights>\[.*);", ibm, re.DOTALL)
  weights = searched_dat.group('weights')

  info(ibm)
  capacities = eval(capacities)
  info(ibm)
  values = eval(values)
  info(ibm)
  try:
    weights = eval(weights)
  except Exception as exception:
    weights = str(exception)

  info(capacities)
  info(values)
  info(weights)

  standard_encoding = {
    "capacities": capacities,
    "values": values,
    "weights": weights,
  }

  standard_encoding = json.dumps(standard_encoding, indent=2)

  return standard_encoding
