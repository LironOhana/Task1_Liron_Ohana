def my_func(x1,x2,x3):
   if not (isinstance(x1, float) and isinstance(x2, float) and isinstance(x3, float)):
       if (isinstance(x1, int) or isinstance(x2, int) or isinstance(x3, int)):
           return print("Error: parameters should be float")
       else:
           return print(None)
   elif (x1+x2+x3)==0:
       print("Not a number – denominator equals zero")
   else:
        Numerator = (x1+x2+x3)*(x2+x3)*x3
        Denominator = x1+x2+x3
        calc = Numerator/Denominator
        return print(calc)

my_func(1,1,1)