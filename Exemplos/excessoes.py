# -*- coding: utf-8 -*-

import sys
print(sys.version_info.major)

a = input("Diz aí ")

try:
    print(range(a))

except TypeError:
    print("tipo errado")

except IOError:
    print("Problema de tipo IO") 

except:
    print("Qualquer outro problema")
