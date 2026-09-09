import math
num = int(input("first number"))
num_2 = int(input("2nd number"))
opr = input("operator(+,-,*,/,sin,cos,tan,log,pow)")
if opr == "+":
    print(num + num_2)
elif opr == "-":
    print(num-num_2)
elif opr == "*":
    print(num*num_2)
elif opr == "/":
    print(num/num_2)
elif opr == "sin":
    print(math.sin(num))
elif opr == "tan":
    print(math.tan(num))
elif opr == "log":
    print(math.log(num))
