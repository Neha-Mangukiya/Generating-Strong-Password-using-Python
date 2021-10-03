#!/usr/bin/env python
# coding: utf-8

# In[13]:


import random

#max length of password 12......
MAX_LEN = 12

DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']  
LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 
                     'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                     'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                     'z']
  
UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 
                     'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q',
                     'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                     'Z']
  
SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>', 
           '*', '(', ')', '<']

COMBINE_LIST = DIGITS + LOCASE_CHARACTERS + UPCASE_CHARACTERS + SYMBOLS

random_digit = random.choice(DIGITS)
random_locharacters = random.choice(LOCASE_CHARACTERS)
random_characters = random.choice(UPCASE_CHARACTERS)
random_symbols = random.choice(SYMBOLS)

random_pass = random_digit + random_locharacters + random_characters + random_symbols

#print(random_pass)

for x in range(MAX_LEN-4):
    random_pass += random.choice(COMBINE_LIST)
#     random.shuffle(random_pass)
    
print(random_pass)
    

