import turtle
import sys
from fractions import Fraction
import statistics
import keyword
from tkinter import *
import random
import math
start_tk = Tk()
start_screen = Canvas(start_tk, width=400, height=100)
start_screen.pack()

start_screen.create_text(200,20, text='Welcome',font=('Times', 20))
start_screen.create_text(200,50, text='Hello, Im Jarvis, your personal assistant :-)',font=('Times', 15))
start_screen.create_text(200,80, text='What can I do for you today?',font=('Times', 15))
def click():
    print("Welcome")
button = Button(start_tk, text="Show my favorites fruites", command=click)
button1 = Button(start_tk, text="Show my favorite actors", command=click)
button2 = Button(start_tk, text="Generate weapon", command=click)
button3 = Button(start_tk, text="Give me 2 number for addition", command=click)
button4 = Button(start_tk, text="Give me 2 number for subtraction", command=click)
button5 = Button(start_tk, text="Give me 2 number for multiplication", command=click)
button6 = Button(start_tk, text="Give me 2 number for division", command=click)
button7 = Button(start_tk, text="Algebra", command=click)
button8 = Button(start_tk, text="Fractions", command=click)
button9 = Button(start_tk, text="Square rooting", command=click)
button10 = Button(start_tk, text="Median", command=click)
button11 = Button(start_tk, text="Factors", command=click)
button12 = Button(start_tk, text="Mean", command=click)
button13 = Button(start_tk, text="File Encryption", command=click)
button14 = Button(start_tk, text="Keyword", command=click)
button15 = Button(start_tk, text="Random shapes and colors", command=click)
button16 = Button(start_tk, text="Jarvis singing happy birthday", command=click)
button.pack()
button1.pack()
button2.pack()
button3.pack()
button4.pack()
button5.pack()
button6.pack()
button7.pack()
button8.pack()
button9.pack()
button10.pack()
button11.pack()
button12.pack()
button13.pack()
button14.pack()
button15.pack()
button16.pack()
start_tk.mainloop()
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

#
# print("1. Show my favorites fruites.")
# print("2. Show my favorite actors.")
# print("3. Generate weapon.")
# print("4. Give me 2 number for addition")
# print("5. Give me 2 number for subtraction")
# print("6. Give me 2 number for multiplication")
# print("7. Give me 2 number for division")
# print("8. Algebra")
# print("9. Fractions")
# print("10. Square rooting")
# print("11. Median")
# print("12. Factors")
# print("13. Mean")
# print("14. File Encryption")
# print("15. keyword")
# print("16. Random shapes and colors")
# print("17. Jarvis singing happy birthday")
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

if yourchoice == 14:
    print("Welcome in Ceasar encryptor!")
    print("Choose option")
    print("1. Encrypt message")
    print("2. Decrypt message")
    choice = int(input())


    def ceasarEncrypt(message, shift):
        message = message.upper()
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        result = ""

        for letter in message:
            if letter in alphabet:
                letter_index = (alphabet.find(letter) + shift) % len(alphabet)
                result = result + alphabet[letter_index]
            else:
                result = result + letter
        return result


    def ceasarDecrypt(message, shift):
        message = message.upper()
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        result = ""

        for letter in message:
            if letter in alphabet:
                letter_index = (alphabet.find(letter) - shift) % len(alphabet)
                result = result + alphabet[letter_index]
            else:
                result = result + letter
        return result


    if choice == 1:
        print("Give me txt file name:")
        fileName = input()
        print("Which shift?")
        shift = int(input())
        file = open(fileName)
        content = file.read()
        result = ceasarEncrypt(content, shift)
        print(result)
        file.close()
        outputFile = open('output.txt', 'w')
        outputFile.write(result)
        outputFile.close()

    elif choice == 2:
        print("Give me txt file name:")
        fileName = input()
        print("Which shift?")
        shift = int(input())
        file = open(fileName)
        content = file.read()
        result = ceasarDecrypt(content, shift)
        print(result)

    else:
        print("Invalid number")
if yourchoice == 15:
    print("Please enter a keyword: ")
    key_word = input()
    if keyword.iskeyword(key_word):
        print("You can't use it.")
    else:
        print("You can use it.")

if yourchoice == 16:
    tk = Tk()
    img = Canvas(tk, width=400, height=400)
    img.pack()
    colors = ["#2F00FF", "#FF1100", "#00FF00", "#FB00FF", "#6200FF", "#FFFB00", "#00FFDD"]


    def random_squares(width):
        x1 = random.randrange(width)
        y1 = x1
        x2 = x1 + random.randrange(width)
        y2 = x2
        img.create_rectangle(x1, y1, x2, y2, outline=random.choice(colors))


    def random_rectangle(width, height):
        x1 = random.randrange(width)
        y1 = random.randrange(height)
        x2 = x1 + random.randrange(width)
        y2 = y1 + random.randrange(height)
        img.create_rectangle(x1, y1, x2, y2, outline=random.choice(colors))


    def random_circle(width, height):
        x1 = random.randrange(width)
        y1 = random.randrange(height)
        x2 = x1 + random.randrange(width)
        y2 = y1 + random.randrange(height)
        img.create_oval(x1, y1, x2, y2, outline=random.choice(colors))


    def random_shapes(width, height):
        random_rectangle(width, height)
        random_circle(width, height)
        random_squares(width)


    button = Button(tk, text="rectangles", command=lambda: random_rectangle(400, 400))
    button.pack()
    button2 = Button(tk, text="squares", command=lambda: random_squares(400))
    button2.pack()
    button3 = Button(tk, text="circles", command=lambda: random_circle(400, 400))
    button3.pack()
    button4 = Button(tk, text="All shapes", command=lambda: random_shapes(400, 400))
    button4.pack()
    tk.mainloop()


if yourchoice == 17:
    tk=Tk()
    img = Canvas(tk, width=400, height=400)
    img.pack()

    img.create_text(150,150, text = "Happy Birthday To You!")
    img.create_text(150, 200, text="Happy Birthday To You!")
    img.create_text(150, 250, text="Happy Birthday Dear Kevinnnnnn!")
    img.create_text(150, 300, text="Happy Birthday To You!")

    tk.mainloop()




















