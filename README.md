# zip_kv_pairs

This is a short Python script demonstrating how to take values from two separate dictionaries and fuse them together as key:value pairs in a single dictionary.

# Script Operation

We start with two separate dictionaries.
```python
  dict1 = {'a':bin(0b0000), 'b':bin(0b0001), 'c':bin(0b0010), 'd':bin(0b0011), 
           'e':bin(0b0100), 'f':bin(0b0101), 'g':bin(0b0110), 'h':bin(0b0111)}

  dict2 = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7}
```
Next, we generate a new dictionary whose key:value pairs are formed of the values from the two separate dictionaries.
```python
  zipped_kv_pairs = dict(zip(dict1.values(), dict2.values()))
```
The resulting `zipped_kv_pairs` dictionary is shown below.
```python
  {'0b0': 0, '0b1': 1, '0b10': 2, '0b11': 3, '0b100': 4, '0b101': 5, '0b110': 6, '0b111': 7}
```

