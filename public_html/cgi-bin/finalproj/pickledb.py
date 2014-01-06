# pickledb.py                                                                                                                                                                                                 
# A simple module for storing arbitrary python values in a persistent datbase.                                    

import anydbm
import pickle

def open(filename, mode):
  '''Open the pickle database'''
  return anydbm.open(filename, mode)

def close(db):
  '''Close the pickle database'''
  return db.close()

def storeValue(db, key, val):
  '''Store the Python value val with the given key in database db'''
  db[key] = pickle.dumps(val)

def getValue(db, key, defaultValue = None): # Allow an optional defaultValue that defaults to None                
  '''Return the Python value ssociated with the given key in database db.                                         
     Returns defaultValue if the key is not in the database.'''
  try:
    return pickle.loads(db[key])
  except:
    return defaultValue # Special case when key is not in the database                                            

def keys(db):
  '''Return the keys in this database'''
  return db.keys()

def items(db):
  '''Return a list of key/list-value pairs from the database'''
  return map(lambda (key,val): (key, pickle.loads(val)), db.items())
