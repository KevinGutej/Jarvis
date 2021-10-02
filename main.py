import turtle
import sys
from fractions import Fraction
import statistics
import keyword
from tkinter import *
import random
import math
from itertools import combinations

start_tk = Tk()
start_screen = Canvas(start_tk, width=400, height=100)
start_screen.pack()

start_screen.create_text(200,20, text='Welcome',font=('Times', 20))
start_screen.create_text(200,50, text='Hello, Im Jarvis, your personal assistant :-)',font=('Times', 15))
start_screen.create_text(200,80, text='What can I do for you today?',font=('Times', 15))
Numbers = []

def printElement(list):
    for i in list:
        print(i)

class AI:
    pass
robot = AI()

def fruits():
    Fruits = ["Apple", "Watermelon", "Banana", "Blueberrie"]
    printElement(Fruits)

def actors():
    Actors = {'harry potter': 'Harry Potter and the Goblet of Fire (2005)',
              'Christopher Daniel Barnes': 'Spiderman',
              'Jason Farries': 'InspectorCalls'}
    printElement(Actors)

def weapons():
  print("Which weapon should I generate?\n")
  print("1. Arrow?")
  print("2. Sword?")
  print("3. Trident")
  yourchoice = int(sys.stdin.readline())

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

  if yourchoice == 1:
    generatearrow()

  elif yourchoice == 2:
    generatesword()

  elif yourchoice == 3:
    trident()

def adding():
    print("Please give me your first number")
    number1 = int(sys.stdin.readline())
    print("Please give me yor second number")
    number2 = int(sys.stdin.readline())
    totalamount = number1 + number2
    print(totalamount)

def multiplication():
    print("Please give me your first number")
    number1 = int(sys.stdin.readline())
    print("Please give me yor second number")
    number2 = int(sys.stdin.readline())
    totalamount = number1 * number2
    print(totalamount)

def takeaway():
    print("Please give me your first number")
    number1 = int(sys.stdin.readline())
    print("Please give me yor second number")
    number2 = int(sys.stdin.readline())
    totalamount = number1 - number2
    print(totalamount)

def division():
    print("Please give me your first number")
    number1 = int(sys.stdin.readline())
    print("Please give me yor second number")
    number2 = int(sys.stdin.readline())
    totalamount = number1 / number2
    print(totalamount)

def algebra():
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

def fractions():
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

def fraction_multiplication():
    print("Please give us your number")
    number1 = int(sys.stdin.readline())
    print("Please give me your square root")
    number2 = int(sys.stdin.readline())
    print(number1 ** number2)

def median():
    print("Please tell me how many numbers you want:")
    number = int(sys.stdin.readline())
    for x in range(0,number):
        print("Your number is:")
        number1 = int(sys.stdin.readline())
        Numbers.append(number1)
    print(statistics.median(Numbers))
    print(sorted(Numbers))

def factors():
    print("Please enter you number:")
    number1 = int(sys.stdin.readline())
    number2 = 0
    for i in range(0,number1 +1):
        print('%s + %s' % (number1,number2))
        number1 = number1 - 1
        number2 = number2 + 1

def mean():
    print("How many numbers would you want to add and divide:")
    number = int(sys.stdin.readline())
    for x in range(0,number):
        print("Please give me all your numbers:")
        number1 = int(sys.stdin.readline())
        Numbers.append(number1)
    statistics.mean(Numbers)
    print(statistics.mean(Numbers))

def ceasar_encryptor():
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

def is_keyword():
    print("Please enter a keyword: ")
    key_word = input()
    if keyword.iskeyword(key_word):
        print("You can't use it.")
    else:
        print("You can use it.")

def random_shapes():
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


def birthday_song():
    tk=Tk()
    img = Canvas(tk, width=400, height=400)
    img.pack()

    img.create_text(150,150, text = "Happy Birthday To You!")
    img.create_text(150, 200, text="Happy Birthday To You!")
    img.create_text(150, 250, text="Happy Birthday Dear Kevinnnnnn!")
    img.create_text(150, 300, text="Happy Birthday To You!")

    tk.mainloop()


def combos():


    print("Please enter a number , and we will find different combinations to make that number: ")
    number = int(input())
    list = [1, 5, 3, 7, 9, 2, 3, 4, 3]

    def findNumbers(list, sum):
        output = []
        for i in combinations(list, 2):
            if i[0] + i[1] == sum:
                output.append((i[0], i[1]))

        if output == []:
            print("There was no matching pairs")
        else:
            return output

    print(findNumbers(list, number))


button = Button(start_tk, text="Show my favorites fruites", command=fruits)
button1 = Button(start_tk, text="Show my favorite actors", command=actors)
button2 = Button(start_tk, text="Generate weapon", command=weapons)
button3 = Button(start_tk, text="Give me 2 number for addition", command=adding)
button4 = Button(start_tk, text="Give me 2 number for subtraction", command=multiplication)
button5 = Button(start_tk, text="Give me 2 number for multiplication", command=takeaway)
button6 = Button(start_tk, text="Give me 2 number for division", command=division)
button7 = Button(start_tk, text="Algebra", command=algebra)
button8 = Button(start_tk, text="Fractions", command=fractions)
button9 = Button(start_tk, text="Square rooting", command=fraction_multiplication)
button10 = Button(start_tk, text="Median", command=median)
button11 = Button(start_tk, text="Factors", command=factors)
button12 = Button(start_tk, text="Mean", command=mean)
button13 = Button(start_tk, text="File Encryption", command=ceasar_encryptor)
button14 = Button(start_tk, text="Keyword", command=is_keyword)
button15 = Button(start_tk, text="Random shapes and colors", command=random_shapes)
button16 = Button(start_tk, text="Jarvis singing happy birthday", command=birthday_song)
button17 = Button(start_tk, text="Combinations for your chosen number", command=combos)
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
button17.pack()

start_tk.mainloop()


