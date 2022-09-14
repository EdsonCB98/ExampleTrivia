n_exer = int(input('Ingrese el numero de ejercicio: '));

if n_exer==1: 
  num1 = int(input('Ingrese el primer valor:'));
  num2 = int(input('Ingrese el segundo valor:'));

  prom = (num1 + num2)/ 2

  print('Promedio', prom);
elif n_exer==2:
  num1 = int(input('Ingrese el primer valor:'));
  num2 = int(input('Ingrese el segundo valor:'));
  
  poten = num1**num2;

  print('Potencia', poten);
elif n_exer==3:
  num3 = int(input('Ingrese el primer valor:'));
  raiz = num3**(1/2) 

  print('Raiz cuadrada: ', raiz)
elif n_exer==4:
  num3 = int(input('Ingrese el primer valor:'));
  num4 = int(input('Ingrese el segundo valor:'));
  s_cuad = ((num3**2)+(num4**2))**(1/2)
  
  print('Suma de cuadrados: ', s_cuad);
else: 
  print('Ingrese una opcion válida por favor.')