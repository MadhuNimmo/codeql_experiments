def A(argA1,argA2):
  return argA1+"strng"
def B(argB1):
  return argB1
def concatStr(s1,s2):
    return s1+s2
def main(argM1,argM2):
  x = concatStr(argM1,argM2)  
  y = A(x,"extra")
  B(y)
main("please","update")
