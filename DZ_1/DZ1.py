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

def calcHist():
    for counter in range(100):
        start = time.time()
        search()
        end = time.time()
        masstime[counter] = end - start
calcHist()
min = min(masstime)
max = max(masstime)
mean = mean(masstime)
print ("gistogramma = ", gistogramma, "\nmin time is ", min, "\nmax time is ", max, "\nmean time is ", mean )
