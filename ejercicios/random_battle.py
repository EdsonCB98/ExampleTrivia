import random;

player1=input('Primer jugador: ');
player2=input('Segundo jugador: ');

players=[];
players.append(player1)
players.append(player2)

inicia = random.randint(0,1);

print('\nEl primero es iniciar sera: ', players[inicia]);

jugador1_puntos = 20
jugador2_puntos = 20

jugador_1_turnos = []
jugador_2_turnos = []

jugador_1_turnos.append(jugador1_puntos);
jugador_2_turnos.append(jugador2_puntos);

turnos=0;
jugar=True;

def verifcar():
  if (jugador1_puntos<=0 or jugador2_puntos<=0):
    global jugar;
    jugar=False;
    print('\n')
    print('Termino el juego.')
    print('Gano el jugador', players[inicia].capitalize())
   
    print('Player 1: ',players[0],jugador_1_turnos);
    print('Player 2: ',players[1],jugador_2_turnos);
  
while jugar:
  turnos+=1;

  print('\n** Turno - ',turnos,' **');
  restar=random.randint(0,5);
  
  if (inicia==0):
    jugador2_puntos-= restar;
    #    print(restar,'** Puntos restantes: ', jugador2_puntos);

    print('** Puntos restantes: ', jugador2_puntos);

    jugador_2_turnos.append(jugador2_puntos);
    verifcar();   
    inicia = 1;
  else:
    jugador1_puntos-= restar;
    print(restar,'** Puntos restantes: ', jugador1_puntos);

    jugador_1_turnos.append(jugador1_puntos);
    verifcar();    
    inicia = 0;

  print('\n')
