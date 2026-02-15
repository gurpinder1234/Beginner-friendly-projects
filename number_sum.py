# number_sum.py
count = 0

while True:
    num = int(input("Write a number: "))
    if num == 0:
        break
    count += num
    print("Current total:", count)

print("Final sum:", count)
