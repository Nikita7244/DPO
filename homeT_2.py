from math import sqrt
from random import randint
from statistics import mean
import time


mass = [0]*1000000
gistogramma = [0]*10
masstime = [0]*100
sum = 0
for counter in range(1000000):
    mass[counter] = randint(0,999)

def search():
    for counter in range(1000000):
        gistogramma[mass[counter] // 100] +=1

def histDistance (X1, X2):
    distance = float (sqrt((X1-X2)**2 + (gistogramma[X1]-gistogramma[X2])**2))
    print ("distance = ", distance)

def RWinFile():
    file = open("test.txt", "w+")
    file.write(str(gistogramma))
    file.seek(0)
    print ("Вывод из файла ", file.read())
    file.close()

def space(count):
    for i in range (count):
        print(" ", end="")

def triangle(a):
    for i in range (a+1):
        space(a-i)
        for j in range (1+i*2):
            print("*",end="")
        print("\n")

def main():
    triangle(7)
    search()
    histDistance(5, 8)
    RWinFile()
    
main()