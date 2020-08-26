# Collect values from two dictionaries and store them as key:value pairs within one single dictionary.

dict1 = {'a':bin(0b0000), 'b':bin(0b0001), 'c':bin(0b0010), 'd':bin(0b0011), 
         'e':bin(0b0100), 'f':bin(0b0101), 'g':bin(0b0110), 'h':bin(0b0111)}

dict2 = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7}

zipped_kv_pairs = dict(zip(dict1.values(), dict2.values()))

print(zipped_kv_pairs)