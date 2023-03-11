from info import info
import json
import re

# See: https://www.ibm.com/docs/en/icos/12.9.0?topic=problem-typical-integer-program-knapsack

def handle(pb2_request, repo_path):
  ibm = pb2_request.input.decode('utf-8')

  searched_dat = re.search("Capacity[\s=]*(?P<capacities>\[.*);", ibm)
  capacities = searched_dat.group('capacities')

  searched_dat = re.search("Value[\s=]*(?P<values>\[.*);", ibm)
  values = searched_dat.group('values')

  searched_dat = re.search("Use[\s=]*(?P<weights>\[.*);", ibm, re.DOTALL)
  weights = searched_dat.group('weights')

  capacities = eval(capacities)
  values = eval(values)
  weights = eval(weights)

  standard_encoding = {
    "capacities": capacities,
    "values": values,
    "weights": weights,
  }

  standard_encoding = json.dumps(standard_encoding, indent=2)

  return standard_encoding
