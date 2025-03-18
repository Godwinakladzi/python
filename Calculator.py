firstNumber = float(input('enter first number  '))
operator = input('Enter operator ')
secondNumber = float(input('enter second number '))

def calculate(firstNumber, operator, secondNumber):
    if  operator == '+':
        return firstNumber + secondNumber
    elif operator == '/':
        return firstNumber / secondNumber
    elif operator == '-':
        return firstNumber - secondNumber
    elif operator == '*':
        return firstNumber * secondNumber 
    else: 
        return 'Check the operator and the numbers'
    
print(calculate(firstNumber, operator, secondNumber))



