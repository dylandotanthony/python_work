# Basic - Print all integers from 0 to 150.
# count = 0
# while count <= 150:
#     print(count)
#     count = count + 1

for i in range(151):
    print(i)

# Multiples of Five - Print all the multiples of 5 from 5 to 1,000
for i in range(5,1001,5):
    print(i)

# Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, print "Coding" instead. 
# If divisible by 10, print "Coding Dojo".

for i in range(0,101):
    if i%10 == 0:
        print("coding dojo")
    elif i%5 == 0:
        print("coding")
    else:
        print(i)

# Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.

sum = 0
for x in range(1,500001,2):
    sum += x
print(sum)

# Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.

for y in range (2018,0,-4):
    print(y)


#Flexible Counter - Set three variables: lowNum, highNum, mult. 
# Starting at lowNum and going through highNum, print only the integers that are a multiple of mult. 
# For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)

lownum = 1
highnum = 199
mult = 4

for z in range(lownum,highnum +1):
    if z % mult == 0:
        print(z)