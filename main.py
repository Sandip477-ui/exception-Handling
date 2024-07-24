#exception Handling
try:
    num1 =input("Enter number1: ")
    num2 =input("Enter number2: ")
    sum = float(num1)+float(num2)
    print(f"total is {sum}")
except:
    print("please enter all numberic value.")
finally:
    print("back to progam")

