/* Task 1 */
print('Hello World')
print('Please enter your name')
a = input()
print('It\'s nice to meet you, ' + a + '.')
import Functions
print('Are you satisfied with these results, ' + a + '?')
print('Choose "yes" or "no"')
b = input()
if b == "Yes" or b == "yes":
    print('Great! Have a nice day, ' + a + '.')
    quit()
elif b == "No" or b == "no":
    print('I think my math is correct. Prove me wrong if you wish.')
    quit()
else:
    print('You did not follow directions correctly. Therefore, your math journey must end here, ' + a + '.')
    quit()


/* Task 2 */
print('Please enter a number:')
n = float(input())
def AddSix(n):
  print('The value of your number plus six is:')
  print(n + 6)
AddSix(n)
def Double(n):
  print('The value of your number doubled is:')
  print(n * 2)
Double(n)
def Square(n):
  print('The value of your number squared is:')
  print(n ** 2)
Square(n)


