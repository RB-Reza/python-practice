number1=int(input('number 1 : '))
op=input('op: ')
number2=int(input('number 2 : '))
def Calculator(number1,op,number2):
    if op=='+':
        return number1+number2
    elif op=='*':
        return number1*number2
    elif op=='-':
       return number1-number2 
    elif op=='/':
        if number2==0:
            return 'error'
        return number1/number2

if op in ('+','-','/','*'):
    print(Calculator(number1,op,number2))
else:
    print('please jast True op')   
