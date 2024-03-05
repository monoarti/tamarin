balance = 0

while True:
 
  print(f"Your current balance is ${balance}")

  operation = input("which one (deposit, withdraw, quit)? : ")

  if operation == "deposit":
    amount = float(input("How much do u want to deposit? $"))

    balance += amount

    print(f"Deposited ${amount}. Your new balance is ${balance}")
  elif operation == "withdraw":
    amount = float(input("How much do u want to withdraw? $"))

    if amount > balance:
      print("Insufficient funds.")
    else:
      balance -= amount

      print(f"Withdraw ${amount}. Your new balance is ${balance}")
  elif operation == "quit":
    break
  else:
    print("Invalid operation.")

print("bye")