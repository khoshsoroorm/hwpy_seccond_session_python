print("Calculate BMI")
w_solution = input('do you want to calculate your BMI in SI? (Y / N):')
w_solution = w_solution.lower()
if w_solution == 'y':
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

elif w_solution == 'n':
    w_in = input('please enter your weight: ')
    h_in = input('Please enter your height: ')

    weight_1 = float(w_in)
    height_1 = float(h_in)
    bmi = (weight_1 * 703) / (height_1 * height_1)

    print(bmi, 'lb/in')
    if bmi < 18.5:
        print('Underweight')
    elif 18.5 <= bmi and bmi <= 25:
        print('Normal')
    elif 25 < bmi and bmi < 30:
        print('Overweight')
    else:
        print('Obesity')
