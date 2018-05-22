#!/usr/bin/python3
import re

pattern = 'dfdsdfHello'
text = 'Hello Data Science Folks, How are you?'

match = re.search(pattern, text)

if match: 
   s = match.start()
   e = match.end()
   print('Found "{}" in "{}" from {} to {} ("{}")'.format(match.re.pattern, match.string, s, e, text[s:e]))
else:
   print ("Pattern did not match")
