import numpy as py
import random

def mutation(c, amount):
    r1 = random.randint(0, 3)
    r2 = random.randint(0, (len(amount) - 1))
    c[r1] = int(amount[r2])
    return c


def produce_child(a, b):
    c1 = []
    c2 = []
    for i in range(4):
        if i <= 1:
            c1.append(a[i])
            c2.append(b[i])
        else:
            c2.append(a[i])
            c1.append(b[i])

    child = [c1, c2]
    return child



def fitness_function(ch, amount):
    match = 0
    for i in range(4):
        index = amount.index(int(ch[i]))
        match = match + amount[index]

    return match


def res(array, amount):
    final_result = ''
    for k in range(len(amount)):
        a = amount[k]
        if int(a) in array:
            final_result = final_result + '1'
        else:
            final_result = final_result + '0'
        k = k+1
    return final_result


### taking input from file

transactions = []

with open('input.txt') as f:
    lines = f.readlines()


for line in lines:
    transactions.append(line.split())


numberOfDailyTransactions =  int(transactions[0][0])

amount = []
for i in range(numberOfDailyTransactions):
  if(transactions[i+1][0] == 'l'):
    amount.append(int(transactions[i+1][1]) * -1)
  else:
    amount.append(int(transactions[i+1][1]) * +1)


n = 4
m = 1000
result = ''


population = []
for j in range(m):
    arr = []
    for x in range(4):      ## this for loop is generating 4 random transaction from amount array
        a = random.choice(amount)
        a = int(a)
        arr.append(a)

    population.append(arr)      ## random 4 ta number er array ke population array te appending




mutation_threshold = 0.03

i = 0
while i < 10000:
    updated_population = []
    for j in range(len(population)):
        u = random.choice(population)
        v = random.choice(population)

        children = produce_child(u, v)
        ch1 = children[0]
        ch2 = children[1]

        check = random.random()

        if check < mutation_threshold:
            ch1 = mutation(ch1, amount)
            ch2 = mutation(ch2, amount)

        updated_population.append(ch1)
        updated_population.append(ch2)

        ffc1 = fitness_function(ch1, amount)
        ffc2 = fitness_function(ch2, amount)

        if ffc1 == 0:
            result = res(ch1, amount)
            break
        if ffc2 == 0:
            result = res(ch2, amount)
            break
        population = updated_population
        i = i + 1


if result == '':
    print("-1")
else:
    print(result)