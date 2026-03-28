#Is it even?
def is_even_odd (number):
 if number%2==0:
  return " It is an even number."
 else:
   return "It is an odd number."
def main():
 number=int(input("Enter a whole number "))
 result= is_even_odd (number)
 print(result)
if __name__ == "__ main __":
 main()
