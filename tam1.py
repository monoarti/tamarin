inputmember = input("please enter something : ")

try:
  input_data = eval(inputmember)
except (SyntaxError, NameError):
  input_data = inputmember

input_type = type(input_data)

print("type is", input_type.__name__, )

