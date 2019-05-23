print('Calcute BMI')
w_in = input('please enter your weight(kg): ')
h_in = input('Please enter your height(m2): ')

weight_1 = float(w_in)
height_1 = float(h_in)
bmi = weight_1 / (height_1 * height_1)

print(bmi, 'kg/m2')
if bmi < 18.5:
    print('Underweight')
elif 18.5 <= bmi and bmi <= 25:
    print('Normal')
elif 25 < bmi and bmi < 30:
    print('Overweight')
else:
    print('Obesity')
