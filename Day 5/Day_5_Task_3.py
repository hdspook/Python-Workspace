#Traversing the current directory

import os

for _,_,files in os.walk("."):
    for x in files:
        if x.endswith("py"):
            print(x)
