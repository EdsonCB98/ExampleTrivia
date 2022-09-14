
tfilas = int(input('Ingrese el numero de filas \n'));
signo = input('Signo que desea ver ');

fila = 0;

while fila < tfilas:
  est = 0;
  value = '';
  
  while est <= fila:
    value = value + signo;
    est = est + 1;
    
  print(value)
  fila = fila + 1;