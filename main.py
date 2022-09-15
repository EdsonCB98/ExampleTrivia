import time;
import random;
import re;

#Colores
BLUE = '\033[34m'
YELLOW = '\033[33m'
RED = '\033[31m'
RESET = '\033[39m'
GREEN = '\033[32m'
MAGENTA = '\u001b[35m';

def line(color=YELLOW):
  print(color+ '*'*70 + RESET);
   
#Variables
puntajes=[];
puntaje = random.randint(0,10);
intento = 0
iniciar_trivia = True


name = input('Hola cual es tu nombre: ' + YELLOW).strip();

while (not re.fullmatch(r"[A-Za-z ]{1,20}", name)):
  name = input(RED+' ** No podremos iniciar la trivia, si no escribes un nombre: ' + YELLOW).strip();
  
print('\n');
line(BLUE)
print(BLUE+'A continuación se podra en juego tus conocimientos sobre el ');
line(BLUE);

time.sleep(1);
print('\n');
print(RESET + 'Estas listo ' + YELLOW + name + RESET + ' ?')
print('Tu puntaje actual es de: ' + YELLOW, puntaje)

for i in range(3,0,-1):
  time.sleep(1);
  print((i), '...')
  
input(RESET + '(preciona Enter para empezar ...)\n')

while iniciar_trivia == True:
  time.sleep(1)
  intento += 1  
  puntaje = 0

  line()
  
  print(RESET+'\n Número de intento: ', intento, '\n');
  
  #Question 1
  print(GREEN + '1. ¿ Quién es el vengador más fuerte ?')
  pg1_alt = ['a) Thor','b) Hulk','c) Loki','d) Michael Jordan'];
  for alternativa in pg1_alt:
    print(' ',alternativa);

  res_n1 = input(RESET+'Tu respuesta es: '+YELLOW).lower().strip();

  while res_n1 not in ('a', 'b', 'c', 'd'):
      if res_n1 == 'x':
        puntaje += 1000
        print('Hackeaste el sistema, tu sabes que es Hulk ... :/ .. Ayuda!!');
        break
      res_n1 = input(YELLOW+'Ingrese una opcion dentro de las disponibles, por favor: '+ RESET).lower().strip();
      
  time.sleep(1)
  
  if res_n1 == 'a':
      puntaje+=10
      print(RED+'  mmmm...error')
  elif res_n1 == 'c':
      puntaje+=3
      print(RED+'El fue un Jefe Final')
  elif res_n1 == 'd':
      puntaje+=1 
      print(RED+'Podria ser, pero no pertenece a esta franquicia')
  else:
      puntaje+=25
      print(MAGENTA+'Acertaste !!! puntaje: ', puntaje)

  print('\n')
  time.sleep(1)
  
  #Question 2
  print(GREEN + '2. ¿ Quién es el hombre mas inteligente ?')
  pg2_alt = ['a) Reed Richards','b) Peny Stark','c) Stephen Hawking','d) Box Bunny'];
  
  for alternativa in pg2_alt:
    print(' ', alternativa);

  res_n2 = input(RESET+'Tu respuesta es: '+YELLOW).lower().strip();
  
  while res_n2 not in ('a', 'b', 'c', 'd'):
    res_n2 = input(YELLOW+'Ingrese una opcion dentro de las disponibles, por favor: '+RESET).lower().strip();
    
  time.sleep(1)
  if res_n2 == 'b':
      puntaje-=10
      print(RED+' Te engaño el apellido, pero no era Tony.')
  elif res_n2 == 'c':
      puntaje+=15
      print(RED+' En nuestro universo, podría ser.')
  elif res_n2 == 'd':
      puntaje/=2;
      print(RED + ' Definitivamente no esta en la categoría humano.')
  else:
      puntaje+=10
      puntaje*=2
      print(MAGENTA+' Cuestionable, pero acertaste. ')
  
  print('\n')
  time.sleep(1)

  #Question 3
  print(GREEN +'3. ¿ De que material esta hecho en su mayoria el escudo del "Cap" ?');
  pg3_alt=['a) Octirón ', 'b) Adamantium','c) Vibranium','d) Veritasium']
  for alternativa in pg3_alt:
    print(' ', alternativa)
  
  res_n2 = input(RESET + 'Tu respuesta es: ' + YELLOW).lower().strip();
  
  while res_n2 not in ('a', 'b', 'c', 'd'):
    res_n2 = input(YELLOW+'Ingrese una opcion dentro de las disponibles, por favor: '+RESET).lower().strip();
    
  time.sleep(1)
  if res_n2 == 'a':
      puntaje+=1;
      print(RED+' Nos confundimos de franquicia.')
  elif res_n2 == 'b':
      puntaje+=15
      print(RED+' Pertenecen al mismo universo, pero no.')
  elif res_n2 == 'd':
      puntaje/=2;
      print(RED + ' Definitivamente no es un elemento químico de MARVEL.')
  else:
      puntaje+=15
      puntaje*=2
      print(MAGENTA+' Le diste al clavo !!!.')
    

  print('\n')
  time.sleep(1)
  
  print(RESET+'Cargando resultados...')
  time.sleep(2)
  print('\n')
  print('  Hola ' + YELLOW, name.capitalize(), RESET + 'Gracias por jugar')
  print(RESET + '  Este fue tu puntaje: ' + YELLOW, puntaje)

  time.sleep(1)
  
  repetir_trivia = input('\n¿ Deseas iniciar la trivia nuevamente ?, \nIngresa "y" para repetir, caso contrario, preciona cualquier tecla: '+RESET
  ).lower().strip();
  
  if (repetir_trivia != 'y'):
    iniciar_trivia = False
    print('Gracias por jugar, esperamos que te hayas divertido y vuelvas pronto...')
    print('Hasta luego !!!')
    
  puntajes.append(puntaje);

if (intento>1):
  print('\n'+RESET+'** Hola de nuevo, aqui un breve reporte de tus intentos:');

  for i in range(0,len(puntajes),1):
    print('  '+RESET+'Intento: '+YELLOW, i+1, RESET+' Puntaje: '+YELLOW, puntajes[i]);

  print('\n')
  if (puntajes[0] < puntajes[-1]):
    print(MAGENTA+'  *** Haz mejorado ... estas por buen camino');
  else:
    print(MAGENTA+'  *** Usted es muy observador y detallista. Y un gran fan de MARVEL')
  
