cat = 1

def howmanycat():
  cat = 2
  print(f"local cat {cat}")
howmanycat()
print(f"global cat {cat}")


cat = 1
def howmanycat():
  global cat
  cat += 2
  print(f"local cat {cat}")
howmanycat()
print(f"global cat {cat}")


cat = 1
def howmanycat(ccc):
  print(f"local cat {cat}")
  return ccc + 1

caaat = howmanycat(cat)
print(f"local cat {caaat}")
print(f"global cat {cat}")
