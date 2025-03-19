"""Програма яка приймає два числа, рахує та вивидоить середнє арефметичне з відрізку а, б які кратні числу 3."""

a = int(input("Please set 'a': ")) # 2
b = int(input("Please set 'b': ")) # 10
counter, sum = 0, 0

for item in range(a, b+1): # b+1 - це тому, що range не включає останнє число
    if item % 3 == 0:
        counter = counter + 1
        # counter = 1 + 1 + 1
        sum = sum + item
        # sum = 3 + 6 + 9
print (sum / counter)
