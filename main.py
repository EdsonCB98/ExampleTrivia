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
CYAN = "\033[0;36m";

def line(color=YELLOW):
  print(color+ '*'*70 + RESET);
   
#Variables
puntajes=[];
puntaje = random.randint(0,10);
intento = 0
iniciar_trivia = True


name = input('Hola cual es tu nombre: ' + YELLOW).strip();

correct=random.randint(20,50);
r_basico=random.randint(10,20);
r_medio=random.randint(3,10);
r_alto=random.randint(1,3);

while (not re.fullmatch(r"[A-Za-z ]{1,20}", name)):
  name = input(RED+' ** No podremos iniciar la trivia, si no escribes un nombre: ' + YELLOW).strip();
  
print('\n');
line(BLUE)
print(BLUE+'A continuación se podra en juego tus conocimientos sobre el Universo Cinematográfico de Marvel (MCU). \n\nLee atentamente cada pregunta y responde según creas conveniente, solo con las letras, dentro de las opciones disponibles. ("a","b","c" o "d") \nSuerte !!! ');
line(BLUE);

time.sleep(1);
print('\n');
print(RESET + 'Estas listo ' + YELLOW + name + RESET + ' ?')
print('Tu puntaje actual es de: ' + YELLOW, puntaje)
input(RESET + '(preciona Enter para empezar ...)\n' + YELLOW)

for i in range(5,0,-1):
  time.sleep(1);
  print((i), '...')
  

while iniciar_trivia == True:
  time.sleep(1)
  intento += 1  
  puntaje = 0

  line(BLUE)
  
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
      puntaje+=r_basico;
      print(RED+'  mmmm...Casi, estas por buen camino')
  elif res_n1 == 'c':
      puntaje+=r_medio;
      print(RED+' El fue un Jefe Final')
  elif res_n1 == 'd':
      puntaje+=r_alto
      print(RED+' Podria ser, pero no pertenece a esta franquicia')
  else:
      puntaje+=correct;
      print(MAGENTA+' Acertaste !!! ')

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
      puntaje-=r_basico;
      print(RED+' Te engaño el apellido, pero no era Tony.')
  elif res_n2 == 'c':
      puntaje+=r_medio;
      print(RED+' En nuestro universo, podría ser.')
  elif res_n2 =='d':
      puntaje/=r_alto;
      print(RED + ' Definitivamente no esta en la categoría humano.')
  else:
      puntaje+=correct;
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
      puntaje+=r_basico;
      print(RED+' Nos confundimos de franquicia.')
  elif res_n2 == 'b':
      puntaje+=r_medio;
      print(RED+' Pertenecen al mismo universo, pero no.')
  elif res_n2 == 'd':
      puntaje/=r_alto;
      print(RED + ' Definitivamente no es un elemento químico de MARVEL.')
  else:
      puntaje+=correct;
      print(MAGENTA+' Le diste al clavo !!!.')
    
  
  print('\n')
  time.sleep(1)
  ruleta=['+','-','*','/'];
  ruleta_valores=[correct, r_basico, r_medio, r_alto];
  
  print(CYAN+ ' **Ruleta de puntaje final');
  print('  **A tu puntaje obtenido le haremos unos cambios.\n Estos seran :')

  for i in range (4):
    time.sleep(1);
    print(' ', ruleta[i], ruleta_valores[i])
  
  puntaje+=ruleta_valores[0];
  puntaje-=ruleta_valores[1];
  puntaje*=ruleta_valores[2];
  puntaje/=ruleta_valores[3];

  print('\n');
  print(RESET+'Cargando resultados...')
  time.sleep(2)
  print('\n');
  
  print('  Hola ' + YELLOW, name.capitalize(), RESET + '\n  Gracias por jugar')
  print(RESET + '  Este fue tu puntaje: ' + YELLOW, int(puntaje))

  time.sleep(1)
  
  repetir_trivia = input('\n¿ Deseas iniciar la trivia nuevamente ?, \nIngresa "y" para repetir, caso contrario, preciona cualquier tecla: '+RESET
  ).lower().strip();

  print('\n')
  
  if (repetir_trivia != 'y'):
    iniciar_trivia = False
    print('Gracias por jugar, esperamos que te hayas divertido y vuelvas pronto...')
    print('Hasta luego !!!')
    
  puntajes.append(puntaje);

if (intento>1):
  print('\n'+RESET+'** Hola de nuevo, aqui un breve reporte de tus intentos:');

  for i in range(0,len(puntajes),1):
    print('  '+RESET+'Intento: '+YELLOW, i+1, RESET+' Puntaje: '+YELLOW, int(puntajes[i]));

  print('\n')
  
  if (puntajes[-1]<puntajes[0]):
    print(MAGENTA+'  *** Haz mejorado ... estas por buen camino');
  else:
    print(MAGENTA+'  *** Usted es muy observador y detallista. Y un gran fan de MARVEL o lograste hackearnos')
  
