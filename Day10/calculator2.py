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


for i in op:
  optr = op[i]
  if optr == add:
    print(add)
  if optr == sub:
    print(sub)
  if optr == mul:
    print(mul)
  if optr == div:
    print(div)
  
print(op["*"](4,6))