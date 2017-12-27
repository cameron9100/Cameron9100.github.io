/* Task 1 */
def SomeFunction(n):
    y = n**2 + 3*n + 1
    return y

acc=0
for i in range(2, 6):
    print(SomeFunction(i))
    if i < 5:
        print('+')
    else:
        print('=')
    acc = acc + SomeFunction(i)

print(acc)



/* Task 2 */
import math

def taylor(x):
    series = 0
    for n in range (16):
        z = ((-1)**n)*(x**(2*n))/(math.factorial(2*n))
        series = series + z
    return series

print('Pick any radian value of your choice:')
x = int(input())

print('The cosine of ' + str(x) +' is: ')

print(taylor(x))



/* Task 3 */
import math

def taylor(x):
    series = 0
    for n in range (16):
        z = ((-1)**n)*(x**(2*n))/(math.factorial(2*n))
        series = series + z
    return series

def deg_rad(deg):
    radians  = deg * math.pi / 180
    return radians

x = float(input('Pick any degree value of your choice:'))
x = deg_rad(x)

print('The cosine of ' + str(x) +', or your degree value put into radians, is: ')

print(taylor(x))



/* Task 4 */
import math

def taylor(x):
    series = 0
    for n in range(16):
        z = ((-1)**n)*(x**(2*n))/(math.factorial(2*n))
        series = series + z
    return series

def deg_rad(deg):
    radians = deg * math.pi / 180
    return radians

print('Hello! Since I can calculate the cosine of any value you give me, do you prefer for me to use radians or degrees?')
decision1 = input('Type "rad" for Radians or "deg" for Degrees. ')
decision1 = decision1.lower()

if decision1 == "rad":
    x = float(input('Please enter the value in radians:'))

elif decision1 == "deg":
    x = float(input('Please enter the value in Degrees:'))
    x = deg_rad(x)

print('The cosine of ' + str(x) +' is: ')

print(taylor(x))



/* Task 5 */
print('Hello! I will demonstrate the fibonacci sequence, if you give me the amount of numbers: ')
z = int(input())
def fib(n):
  first = 1
  second = 1
  sum = 2
  print (first)
  print(second)
  for i in range (n-2):
    third = first + second
    print (third)
    first = second
    second = third
    sum = sum + third
  print('The total sum of this equation is: ' + str(sum))

print('The numbers of this given sequence come out to: ')
fib(z)



/* Task 6 */
print('Enter the amount of numbers that you want added together after being multiplied by 3: ')
x = int(input())
def rec(n):
  first = 1
  rate = 3
  sum = 1
  print (first)
  for i in range (n-1):
    second = first * rate 
    print (second)
    first = second
    kiwi = first * rate 
    sum = sum + second
  print('The sum of all these numbers is: ' + str(sum))

rec(x) 







