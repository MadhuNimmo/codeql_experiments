def source():
  x1 = "John Doe"
  x2 = inter(x1)
  sink(x2)
def inter(y):
  return y
def sink(z):
  print(z)
source()