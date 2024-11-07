base = int (input("ENTER BASE :-"))
exp = int (input("ENTER EXPONENT :-"))
result=1
for i in range(1,exp+1):
    result=base*result
    print("POWER = " ,result)