

name=input("\n\n\n\t ENTER YOUR NAME :::")

print("\n\n\t\t\t\t\t\t\t\t\t ***WELCOME {} TO THE CALCULATOR*** ".format(name.upper()))

print("\n\n\n\n\n\t *FIRST CHOOSE OPERATOR* \n\t 1.+ \n\t 2.- \n\t 3.* \n\t 4./ ")
op=input("\n\t ENTER ::: ")

if op=='+' or op==1:
    print("\n\t YOU CHOOSE '+' OPERATOR WHICH WILL GIVE YOU THE SUM OF NUMBERS")
elif op=='-' or op==2:
    print("\n\t YOU CHOOSE '-' OPERATOR WHICH WILL GIVE YOU THE SUBTRACTION OF NUMBERS")
elif op=='*' or op==3:
    print("\n\t YOU CHOOSE '*' OPERATOR WHICH WILL GIVE YOU THE MULTIPLICATION OF NUMBERS")
else:
    print("\n\t YOU CHOOSE '/' OPERATOR WHICH WILL GIVE YOU THE DIVISION OF NUMBERS")

print("\n\n\n\n\n\t *NOW ENTER TWO OPERANDS* ")
num1=int(input("\n\t ENTER FIRST OPERAND ::: "))
num2=int(input("\n\t ENTER SECOND OPERAND ::: "))

if op=="+" or op=="1":
    print("\n\n\n\t THE ADDITION OF NUMBERS IS: ",num1+num2)

elif op=="-" or op=="2":
    print("\n\n\n\t THE SUBTRACTION OF NUMBERS IS: ",num1-num2)

elif op=="*" or op=="3":
    print("\n\n\n\t THE MULTIPLICATION OF NUMBERS IS: ",num1*num2)

elif op=="/" or op=="4":
    print("\n\n\n\t THE DIVISION OF NUMBERS IS: ",num1/num2)

else:
    print("\n\n\n\t YOU HAVE GIVEN WRONG INPUT ")


print("\n\n\t\t\t\t\t\t\t\t\t\t THANK YOU FOR USING CALCULATOR ")
