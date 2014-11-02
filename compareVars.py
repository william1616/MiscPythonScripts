def compareVars(base, new, checkDictVals=True):
  if isinstance(base, (list, tuple)):
    for baseItem, newItem in zip(base, new):
      if not compareVars(baseItem, newItem): return False
  elif isinstance(base, (dict)):
    for (baseKey, baseValue), (newKey, newValue) in zip(base.items(), new.items()):
      if not compareVars(baseKey, newKey): return False
      if not compareVars(baseValue, newValue, checkDictVals): return False
  elif isinstance(base, (str, int, bool, float)):
    if checkDictVals:
      return base == new
    else:
      return True
  return True
  
print(compareVars({"key1": {"key2": "value2"}}, {"key1": {"key2": "value3"}}, False))