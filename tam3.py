numb1 = float(input("enter first number:"))
numb2 = float(input("enter second number:"))

operation = input("enter your operation {sum , difference , multiply , divide}:")

if operation == "sum":
    print( numb1 + numb2 )

elif operation == "difference":
    print( numb1 - numb2 )
    
elif operation == "multiply":
    print( numb1 * numb2 )

elif operation == "divide":
    if numb2 == 0:
        print("it is not divided")
    else: 
        print( numb1 / numb2 )

else:    
    print("your operation invalid")