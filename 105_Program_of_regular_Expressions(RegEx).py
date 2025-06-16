# Program of regular Expressions(RegEx)
import re
string= "   I love python   "
x=re.sub(r'^\s+|\s+$x','',string)
print(x)