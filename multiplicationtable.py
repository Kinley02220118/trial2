num1=int(input('Enter the number for which you want the multiplication table:'))
limit=int(input('Enter the limit up to which yo wantthe multipliaction table generated:'))
print(f'multiplication table for {num1} up to {limit}')
for i in range(1,limit+1):
    result=num1*i
    print(f'{num1}*{i}={result}')