count = 0
total = 0
average = 0

while True:
    number = input('Enter a number: ')

    if number == 'done':
        break

    try:
        checker = float(number)
    except:
        print("Invalid input")
        continue

    total = total + checker
    count = count + 1
    average = total / count

print(total, count, average)

    