def my_func(x1,x2,x3):
   if not (isinstance(x1, float) and isinstance(x2, float) and isinstance(x3, float)):
       if (isinstance(x1, str) or isinstance(x2, str) or isinstance(x3, str)):
           return print(None)
       else:
           return print("Error: parameters should be float")
   elif (x1+x2+x3)==0:
       print("Not a number – denominator equals zero")
   else:
        Numerator = (x1+x2+x3)*(x2+x3)*x3
        Denominator = x1+x2+x3
        calc = Numerator/Denominator
        return print(calc)

my_func(2.0,2.0,-4.0)