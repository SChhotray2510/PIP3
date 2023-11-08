import sys
  
num1 = int(sys.argv[1])
num2 = int(sys.argv[2])
if num1 % num2 == 0 or num2 % num1 == 0:
     print("The numbers are divisible")
else:
        print("No Luck")
