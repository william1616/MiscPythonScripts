#compare two python variables
#base => any python variable
#new => variable to compare base against
#checkDictVals => check if the values of dict variables which are not dict variables themselves match ie only check dict keys but do it recursivley
def compareVars(base, new, checkDictVals=True):
  if type(base) != type(new): return False
  if isinstance(base, dict): #if the base is a dict
    for (baseKey, baseValue), (newKey, newValue) in zip(sorted(base.items()), sorted(new.items())): #iterate through the key, value pairs in both the base and the new dicts
      if not compareVars(baseKey, newKey) or not compareVars(baseValue, newValue, checkDictVals): return False #compare the two lists of keys checking the vals then compare the two lists of vals only checking any dict vals if specified by the checkDictVars parameter; if the two variables are not the same return False
  else: #if the base is not a dict
    if checkDictVals: #if checking vals
      return base == new #compare the base and new variables
    else: #otherwise in not checking vals
      return True #return that the vals are equal
  return True #if return false has not yet been executed the two variables must match so return True
  
print(compareVars({"key1": {"key2": "value2"}}, {"key1": {"key2": "value3"}}, False))