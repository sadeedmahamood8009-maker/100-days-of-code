import arts
print(arts.print)


def add(n1,n2):
  return n1 + n2
def sub(n1,n2):
  return n1 - n2
def mul(n1,n2):
  return n1 * n2
def div(n1,n2):
  return n1 / n2


op = {
  "+" : add,
  "-" : sub,
  "*" : mul,
  "/" : div
}
def calculator():
  repeat_cal = True
  num1 = float(input("Enter the first num: "))
  while repeat_cal:
    for i in op:
      print(i)
    sel_op = input("Select an operactor: ")
    num2 = float(input("Enter the second num: "))
    answer = op[sel_op](num1,num2)
    print(f"{num1} {sel_op} {num2} = {answer}")
    choice = input(f"enter 'y' to continue calculate {answer}, or enter 'n' to start a new calculation: ").lower()

    if choice == 'y':
      num1 = answer
    else:
      repeat_cal = False
      print("\n" * 20)
      print(arts.print)
      calculator()
calculator()