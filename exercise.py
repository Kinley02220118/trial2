age =int(input('Enter your age:'))
student=input('Are you student:')
eligible = (age <=12) or (age >=13 and age <= 18 and student=='yes')
if eligible:
    print ('you are eligible for movie ticket discount')
else:
    print('you are not eligible for movie ticket')