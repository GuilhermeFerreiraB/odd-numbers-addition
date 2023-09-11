number = int(input('Please, write a number: '))
sum_odds = 0
counter = 1
while counter <= number:
    sum_odds += counter
    counter += 2
print(f'The sum of the odd numbers from 1 up to {number} is {sum_odds}.')
