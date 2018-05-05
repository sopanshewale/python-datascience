#!/usr/bin/python3

import re

text = 'ababb222aa10x20abbb28d2baaaaa'

pattern = '(ab)'

for match in re.finditer(pattern, text):
    print (type(match))
    s = match.start()
    e = match.end()
    print ('Found "%s" at %d:%d' % (text[s:e], s, e))
