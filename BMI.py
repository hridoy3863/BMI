weight = float(input('Input your weight KG: '))
height = float(input('Input your height meters:  '))
bmi = weight/(height*height)
if bmi <= 18.5:
    print('Your BMI is: ', bmi, 'That means you are underweight')
elif bmi >18.5 and bmi < 25:
    print('Your BMI is ', bmi, 'That means You are normal')
elif bmi > 25 and bmi < 30:
    print('Your BMI is ', bmi, ' That means you are overweight.')
elif bmi > 30:
    print('Your BMI is ', bmi, 'That means you are obese.')
else:
    print('There is an error with your input')