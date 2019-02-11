import sys

print("Number of arguments passed", str(len(sys.argv)))

index = 1

for arg in sys.argv:
    print("argument ", index, "-->", arg)
    index+=1
