num1 = int(input('Agresa el primer número: '));
num2 = int(input('Agresa el segundo un número: '));
operation = input('Agresa la operación: ');

res = 0;

#while operation not in ('*','/','-','+'):
  #operation = input('Resultado: Operador inválido. \nPor favor ingrese +, -, / o *');
  
if (operation == '*'):
  res = num1*num2;
elif (operation == '/'):
  res = num1/num2;
elif (operation == '-'):
  res = num1-num2;
elif (operation == '+'):
  res = num1+num2;
else:
  res = 'Operador inválido. \n Por favor ingrese +, -, / o *';
  
print('Resultado: ', res);