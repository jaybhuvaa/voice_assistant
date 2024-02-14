import re


pattern = re.compile("^[A-Z]$")

parameter = "AA"

if pattern.match(parameter):
    print("Parameter is valid.")
else:
    print("Parameter is not valid.")
    
