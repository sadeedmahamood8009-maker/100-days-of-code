def add(n1,n2):
  return n1 + n2
def sub(n1,n2):
  return n1 - n2
def mul(n1,n2):
  return n1 * n2
def div(n1,n2):
  return n1 / n2

op = {
  '+' : add,
  '-' : sub,
  '*' : mul,
  '/' : div
}
def calculator():
  repeat = True
  num1 = float(input("Enter the first no: "))
  while repeat:
    for i in op:
      print(i)
    sel_op = input("Select an operactor: ")
    num2 = float(input("Enter the second no: "))
    answer = (op[sel_op](num1,num2))
    print(f"{num1} {sel_op} {num2} = {answer}")

    choice = input("enter 'y' if u want to continue calculation, enter 'n' no start a new calculation: ").lower()

    if choice == "y":
      num1 = answer
    else:
      repeat = False
      print("\n" * 20)
      calculator()
calculator()

