import turtle
import sys
from fractions import Fraction
import statistics
import math

Fruits = ["Apple","Watermelon","Banana","Blueberrie"]
Actors = {'harry potter' : 'Harry Potter and the Goblet of Fire (2005)',
        'Christopher Daniel Barnes' : 'Spiderman',
        'Jason Farries' : 'InspectorCalls'}
Numbers = []
def printElement(list):
    for i in list:
        print(i)

# printElement(Fruits)
# printElement(Actors)

class AI:
    pass
robot = AI()

def generatearrow():
    drawer = turtle.Pen()
    drawer.forward(90)
    turtle.mainloop()

def trident():
  ewa = turtle.Pen()
  ewa.forward(50)
  ewa.right(90)
  ewa.left(180)
  ewa.forward(40)

  kasia = turtle.Pen()
  kasia.left(90)
  kasia.forward(130)
  kasia.left(180)
  kasia.forward(400)
  kasia.left(180)
  kasia.forward(400)

  jakub = turtle.Pen()
  jakub.forward(80)
  jakub.left(90)
  jakub.forward(90)

  maja = turtle.Pen()
  maja.left(180)
  maja.forward(90)
  maja.right(90)
  maja.forward(90)

  tata = turtle.Pen()
  tata.left(180)
  tata.forward(40)
  tata.right(90)
  tata.forward(40)
  turtle.mainloop()

def generatesword():
    drawer = turtle.Pen()
    drawer.forward(90)
    drawer.left(180)
    drawer.forward(20)
    drawer.right(90)
    drawer.forward(20)
    drawer.left(180)
    drawer.forward(40)
    turtle.mainloop()
print("Hello, Im Jarvis, your personal assistant.\n")
print("What should I do?\n")
print("1. Show my favorites fruites.")
print("2. Show my favorite actors.")
print("3. Generate weapon.")
print("4. Give me 2 number for addition")
print("5. Give me 2 number for subtraction")
print("6. Give me 2 number for multiplication")
print("7. Give me 2 number for division")
print("8. Algebra")
print("9. Fractions")
print("10. Square rooting")
print("11. Median")
print("12. Factors")
print("13. Mean")
yourchoice = int(sys.stdin.readline())

if yourchoice == 1:
  printElement(Fruits)

elif yourchoice == 2:
  printElement(Actors)

elif yourchoice == 3:
  print("Which weapon should I generate?\n")
  print("1. Arrow?")
  print("2. Sword?")
  print("3. Trident")
  yourchoice = int(sys.stdin.readline())

  if yourchoice == 1:
    generatearrow()

  elif yourchoice == 2:
    generatesword()

  elif yourchoice == 3:
    trident()

elif yourchoice == 4:
    print("Please give me your first number")
    number1 = int(sys.stdin.readline())
    print("Please give me yor second number")
    number2 = int(sys.stdin.readline())
    totalamount = number1 + number2
    print(totalamount)
elif yourchoice == 6:
    print("Please give me your first number")
    number1 = int(sys.stdin.readline())
    print("Please give me yor second number")
    number2 = int(sys.stdin.readline())
    totalamount = number1 * number2
    print(totalamount)
elif yourchoice == 5:
    print("Please give me your first number")
    number1 = int(sys.stdin.readline())
    print("Please give me yor second number")
    number2 = int(sys.stdin.readline())
    totalamount = number1 - number2
    print(totalamount)
elif yourchoice == 7:
    print("Please give me your first number")
    number1 = int(sys.stdin.readline())
    print("Please give me yor second number")
    number2 = int(sys.stdin.readline())
    totalamount = number1 / number2
    print(totalamount)

elif yourchoice == 8:
    print("Give me your x")
    number1 = float(sys.stdin.readline())
    number2 = float(sys.stdin.readline())
    print("Give me your y")
    number3 = float(sys.stdin.readline())
    number4 = float(sys.stdin.readline())
    print("Give me your z")
    number5 = float(sys.stdin.readline())
    number6 = float(sys.stdin.readline())
    print("Sum x %s, sum y %s, sum z %s" % ((number1+number2),(number3+number4),(number5+number6)))

elif yourchoice == 9:
  print("Fractions Please chose your option?\n")
  print("1. Addition?")
  print("2. Subtraction?")
  print("3. Division")
  print("4. Multiplication")
  yourchoice = int(sys.stdin.readline())

  if yourchoice == 1:
      print("How many fractions do you want to add?")
      fractions = int(sys.stdin.readline())
      z = Fraction()
      for i in range(0,fractions):
          print("Give me numerator and denomenator...")
          numerator = int(sys.stdin.readline())
          denomenator = int(sys.stdin.readline())
          z = z + Fraction(numerator,denomenator)
      print(z)

  if yourchoice == 2:
          print("How many fractions do you want to subtract?")
          fractions = int(sys.stdin.readline())
          z = Fraction()
          for i in range(0, fractions):
              print("Give me numerator and denomenator...")
              numerator = int(sys.stdin.readline())
              denomenator = int(sys.stdin.readline())
              z = z - Fraction(numerator, denomenator)
          print(z)

  if yourchoice == 3:
          print("How many fractions do you want to divide?")
          fractions = int(sys.stdin.readline())
          z = Fraction()
          for i in range(0, fractions):
              print("Give me numerator and denomenator...")
              numerator = int(sys.stdin.readline())
              denomenator = int(sys.stdin.readline())
              z = z / Fraction(numerator, denomenator)
          print(z)

  if yourchoice == 4:
          print("How many fractions do you want to multiply?")
          fractions = int(sys.stdin.readline())
          z = Fraction()
          for i in range(0, fractions):
              print("Give me numerator and denomenator...")
              numerator = int(sys.stdin.readline())
              denomenator = int(sys.stdin.readline())
              z = z * Fraction(numerator, denomenator)
          print(z)

if yourchoice == 10:
    print("Please give us your number")
    number1 = int(sys.stdin.readline())
    print("Please give me your square root")
    number2 = int(sys.stdin.readline())
    print(number1 ** number2)

if yourchoice == 11:
    print("Please tell me how many numbers you want:")
    number = int(sys.stdin.readline())
    for x in range(0,number):
        print("Your number is:")
        number1 = int(sys.stdin.readline())
        Numbers.append(number1)
    print(statistics.median(Numbers))
    print(sorted(Numbers))

if yourchoice == 12:
    print("Please enter you number:")
    number1 = int(sys.stdin.readline())
    number2 = 0
    for i in range(0,number1 +1):
        print('%s + %s' % (number1,number2))
        number1 = number1 - 1
        number2 = number2 + 1

if yourchoice == 13:
    print("How many numbers would you want to add and divide:")
    number = int(sys.stdin.readline())
    for x in range(0,number):
        print("Please give me all your numbers:")
        number1 = int(sys.stdin.readline())
        Numbers.append(number1)
    statistics.mean(Numbers)
    print(statistics.mean(Numbers))


























