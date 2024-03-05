def f_to_c(f):
  c = (f - 32) * 5 / 9
  return c


def c_to_f(c):
  f = c * 9 / 5 + 32
  return f

direction = input("please enter direction \n1. far to cel\n2. cel to far\n")

if direction == "1" or direction == "2":
  temp = input("please enter temp \n")
  temp = float(temp)
  if direction == "1":
    result = f_to_c(temp)
    print(f"{temp} degrees fahrenheit to {result:.2f} degrees celsius")
  else:
    result = c_to_f(temp)
    print(f"{temp} degrees celsius to {result:.2f} degrees fahrenheit")
else:
  print("input is wrong")