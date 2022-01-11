import re

#Uncomment and use a single address to get the result as dictionary.

# address = '123_Main_St_Vancouver_BC_A1B2C3' 
address = '4-567_W8th_Ave_Vancouver_BC_D4E5F6'

#define the keys 
keys = ['unit','number', 'street', 'city', 'province', 'postal_code']
#reverse the keys so that if unit is optional it won't be involved in the result
keys.reverse()

#split the address string
splitted_address = new_add = re.split('-|_',address)

#join the street part of the address
splitted_address[-5:-3] = [' '.join(splitted_address[-5:-3])]
#reverse address so it aligns with the keys
splitted_address.reverse()

#create tge dictionary
dictionary = dict(zip(keys,splitted_address))

#reverse the dictionary to get the result in the required format
final_dict = dict(reversed(list(dictionary.items())))

print(final_dict)