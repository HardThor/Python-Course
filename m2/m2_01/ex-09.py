num = int(input("Enter the first number: "))
print(num)
length = len(str(num))


if length == 2 and num % 2 == 0:
    print(f"{num} - Парне двухзначне число")
else:
    print("Ні")