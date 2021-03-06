#handle it
#demo handling exceptions
#try/except

try:
    num = float(input("Enter a number:"))
except:
    print("Something went wrong!")
    
#specifying exception type

try:
    num = float(input("\nEnter a number:"))
except ValueError:
    print("That's not a number")
#handle multiple exception types
 print()
 for value in (None, "Hi!"):
     try:
         print("Attempting to convert", value, "-->", end="")
         print(float(value))
      except (TypeError, ValueError):
          print("Something went wrong!")
#get an exception's argument

try:
    num = float(input("\nEnter a number: "))
except ValueError as e:
    print("That was not a number! Or as Python would say...")
    print(e)
#try/except/else

try:
    num = float(input("\nEnter a number:"))
except ValueError:
    print("That was not a number")
else:
    print("You entered the number", num)
input("\n\nPress the enter key to exit.")
