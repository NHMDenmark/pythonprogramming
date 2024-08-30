a = -3
if a < 10: # and a>0:
    print("True")
    print("Dumt!")
else:
    print("False")
    
if a < 0:
    print("a is negative")
elif a == 0:
    print("a is zero")
else:
    print("a is positive")


monthtable = {"Jan": 1, "Feb": 2, "March":3}
if "dec" in monthtable:
    print(monttable["dec"])
else:
    print("Missing december")

for a in range(10):
    print("a = %d" % a)
    

i = 0
while i < 10:
    print("Hej %d" % i)
    i += 1
    i = i + 1
    
