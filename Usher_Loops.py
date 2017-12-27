/* Task 1 */
start = 1
stop = 11
iterate = 1

for i in range (start, stop, iterate):
    print(i)


/* Task 2 */
acc = 1
while acc < 11:
    print(acc)
    acc = acc + 1


/* Task 3 */
start = 10
stop = -1
iterate = -1
for i in range(start, stop, iterate):
    print(i)


/* Task 4 */
acc = 10
while acc > -1:
    print(acc)
    acc = acc -1
    

/* Task 5 */
start = 5
stop = -1
iterate = -1
for i in range(start, stop, iterate):
    print(i)
    

/* Task 6 */
acc = 5
while acc > 0:
    print(acc)
    acc = acc - 1
    

/* Task 7 */
for i in range (10):
    print(i)

start = 0
stop = 20
iterate = 2
for i in range(start, stop, iterate):
    print(i)


/* Task 8 */
print('Pick any number of your choice.')
a = int(input())
import time
for i in range(a,-1,-1):
    time.sleep(1)
    print(i)
if i == 0:
    print('Timer done!')
    quit() 


/* Task 9 */
print('Pick any number of your choice')
acc = int(input())
import time
while acc > 0:
    time.sleep(1)
    acc = acc -1
    print(acc)
if acc == 0:
    print('Timer done!')
    quit()
