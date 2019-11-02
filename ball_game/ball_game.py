import pygame
import random



pygame.init()
#larghezza schermo
width = 800
#Altezza schermo
height = 600

screen = pygame.display.set_mode((width,height))

pygame.display.set_caption("gioco di prova")

#dimensioni del personaggio
x_size = 100
y_size = 10

#posizione del personaggio
x_position =  400
y_position = 500
#raggio sfere rosse da evitare
radius = 15
#raggio sfere bianche da prendere
point = 10

label = ""
#tempo che passa all' interno del gioco, serve ad far variare la velocità
tempo = 0
score = 0
#array per la posizione dei nemici
x_enemy_position = [0, 0, 0, 0, 0, 0, 0]
y_enemy_position = [50, 50, 50, 50, 50, 50, 50]
#velocità del gioco
speed = 20
#array per la posizione dei punti
point_x = [0,0,0,0,0,0,0]
point_y = [0,0,0,0,0,0,0]

#inizializzo la posizione dei nemici e dei punti
for i in range(len(x_enemy_position)):
    x_enemy = random.randint(90, 690)
    x_bonus = random.randint(90, 690)
    x_value = random.randint(140,690)

    point_x[i] = x_bonus
    x_enemy_position[i] = x_enemy


#funzione per cambiare la posizione dei nemici
def enemy_position():
 for i in range(len(x_enemy_position)):
  x_enemy = random.randint(90, 690)

  x_enemy_position[i] = x_enemy

#funzione per cambiare la posizione dei punti
def point_position():
 for i in range(len(point_x)):

  x_bonus = random.randint(90, 690)
  point_x[i] = x_bonus


#fino a che è true il gioco continua
game = True

#musica del gioco
pygame.mixer.music.load("Dimitri Vegas_ MOGUAI & Like Mike - Mammoth (Original Mix).mp3")
#suono qundo prendi il punto
effect = pygame.mixer.Sound("2.wav")


pygame.mixer.music.play(-1)

clock = pygame.time.Clock()
text = pygame.font.SysFont("Arial",35)

#funzione che mi fa scendere le palle nemiche e creare delle nuove
def enemy_cordinate():

 global x_enemy_position
 global y_enemy_position
 if(y_enemy_position[6] >= 550):
     x_enemy_position = [0, 0, 0, 0, 0, 0, 0]
     y_enemy_position = [30, 30, 30, 30, 30, 30, 30]
     enemy_position()
 else:
   pygame.draw.circle(screen, (255,0, 0), (x_enemy_position[0], y_enemy_position[0]), radius)
   if(y_enemy_position[0] >170):
     y_enemy_position[0] += 10
     pygame.draw.circle(screen, (255, 0, 0), (x_enemy_position[1], y_enemy_position[1]), radius)
     if (y_enemy_position[1] > 170):
         y_enemy_position[1] += 10
         pygame.draw.circle(screen, (255, 0, 0), (x_enemy_position[2], y_enemy_position[2]), radius)
         if (y_enemy_position[2] > 170):
             y_enemy_position[2] += 10
             pygame.draw.circle(screen, (255, 0, 0), (x_enemy_position[3], y_enemy_position[3]), radius)
             if (y_enemy_position[3] > 170):
                 y_enemy_position[3] += 10
                 pygame.draw.circle(screen, (255, 0, 0), (x_enemy_position[4], y_enemy_position[4]), radius)
                 if (y_enemy_position[4] > 170):
                     y_enemy_position[4] += 10
                     pygame.draw.circle(screen, (255, 0, 0), (x_enemy_position[5], y_enemy_position[5]), radius)
                     if (y_enemy_position[5] > 170):
                         y_enemy_position[5] += 10
                         pygame.draw.circle(screen, (255, 0, 0), (x_enemy_position[6], y_enemy_position[6]), radius)
                         y_enemy_position[6] += 10
                     else:
                         y_enemy_position[5] += 10
                 else:
                     y_enemy_position[4] += 10
             else:
                 y_enemy_position[3] += 10
         else:
             y_enemy_position[2] += 10
     else:
         y_enemy_position[1] += 10
   else:
       y_enemy_position[0] += 10

#funzione che mi fa scendere le palle da prendere e mi fa crearne delle nuove
def point_cordinate():

 global point_x
 global point_y
 if(point_y[6] >= 550):
     point_x = [0, 0, 0, 0, 0, 0, 0]
     point_y = [0, 0, 0, 0, 0, 0, 0]
     point_position()

 else:
   pygame.draw.circle(screen, (255,255, 255),(point_x[0],point_y[0]),point)
   if(point_y[0] >170):
     point_y[0] += 10
     pygame.draw.circle(screen, (255, 255, 255), (point_x[1], point_y[1]), point)
     if (point_y[1] > 170):
         point_y[1] += 10
         pygame.draw.circle(screen, (255, 255, 255), (point_x[2], point_y[2]), point)
         if (point_y[2] > 170):
             point_y[2] += 10
             pygame.draw.circle(screen, (255, 255, 255), (point_x[3], point_y[3]), point)
             if (point_y[3] > 170):
                 point_y[3] += 10
                 pygame.draw.circle(screen, (255, 255, 255), (point_x[4], point_y[4]), point)
                 if (point_y[4] > 170):
                     point_y[4] += 10
                     pygame.draw.circle(screen, (255, 255, 255), (point_x[5], point_y[5]), point)
                     if (point_y[5] > 170):
                         point_y[5] += 10
                         pygame.draw.circle(screen, (255, 255, 255), (point_x[6], point_y[6]), point)
                         point_y[6] += 10
                     else:
                         point_y[5] += 10
                 else:
                     point_y[4] += 10
             else:
                 point_y[3] += 10
         else:
             point_y[2] += 10
     else:
         point_y[1] += 10
   else:
       point_y[0] += 10

#funzione che mi definisce i casi in cui avviene una collisione con le palle nemiche
def enemy_collision():
    global game
    if ((x_enemy_position[0] + radius / 2 > x_position and x_enemy_position[0] + radius / 2 < x_position + x_size + radius)):
        if (y_enemy_position[0] + radius/2 > y_position and y_enemy_position[0] < y_position + y_size):

            game = False

    if ((x_enemy_position[1] + radius / 2 > x_position and x_enemy_position[1] < x_position + x_size + radius)):
        if (y_enemy_position[1] + radius / 2 > y_position and y_enemy_position[1] < y_position + y_size):

            game = False
    if ((x_enemy_position[2] + radius / 2 > x_position and x_enemy_position[2] < x_position + x_size + radius)):
        if (y_enemy_position[2] + radius / 2 > y_position and y_enemy_position[2] < y_position + y_size):

            game = False
    if ((x_enemy_position[3] + radius / 2 > x_position and x_enemy_position[3] < x_position + x_size + radius)):
        if (y_enemy_position[3] + radius / 2 > y_position and y_enemy_position[3] < y_position + y_size):

            game = False
    if ((x_enemy_position[4] + radius / 2 > x_position and x_enemy_position[4] < x_position + x_size + radius)):
        if (y_enemy_position[4] + radius / 2 > y_position and y_enemy_position[4] < y_position + y_size):

            game = False
    if ((x_enemy_position[5] + radius / 2 > x_position and x_enemy_position[5] < x_position + x_size + radius)):
        if (y_enemy_position[5] + radius / 2 > y_position and y_enemy_position[5] < y_position + y_size):

            game = False
    if ((x_enemy_position[6] + radius / 2 > x_position and x_enemy_position[6] < x_position + x_size + radius)):
        if (y_enemy_position[6] + radius / 2 > y_position and y_enemy_position[6] < y_position + y_size):

            game = False


#funzione che mi definisce i casi in cui avviene collisioni con i le palle punti
def point_collision():
    global score
    global textscore
    global label
    if ((point_x[0] + point > x_position and point_x[0] + point < x_position + x_size + 2 * point)):
        if (point_y[0] + point > y_position and point_y[0] + point < y_position + y_size+ 2*point):
            point_x[0] = -200
            score+=1
            pygame.mixer.Sound.play(effect)
            textscore = "Score" +":"+" " +str(score)
            label = text.render(textscore,1,(255,255,0))
            screen.blit(label,(600,500))

    elif ((point_x[1] + point > x_position and point_x[1] + point < x_position + x_size + 2 * point)):
        if (point_y[1] + point  > y_position and point_y[1] + point < y_position + y_size+ 2*point):
            point_x[1] = -200
            score += 1
            pygame.mixer.Sound.play(effect)
            textscore = "Score" +":"+" " +str(score)
            label = text.render(textscore, 1, (255, 255, 0))
            screen.blit(label, (600, 500))

    elif ((point_x[2] + point > x_position and point_x[2] + point < x_position + x_size + 2 * point)):
        if (point_y[2] + point > y_position and point_y[2] + point < y_position + y_size+ 2*point):
            point_x[2] = -200
            score += 1
            textscore = "Score" +":"+" " +str(score)
            label = text.render(textscore, 1, (255, 255, 0))
            screen.blit(label, (600, 500))

    elif ((point_x[3] + point > x_position and point_x[3] + point < x_position + x_size + 2 * point)):
        if (point_y[3] + point  > y_position and point_y[3]+ point < y_position + y_size+ 2*point):
            point_x[3] = -200
            score += 1
            pygame.mixer.Sound.play(effect)
            textscore = "Score" +":"+" " +str(score)
            label = text.render(textscore, 1, (255, 255, 0))
            screen.blit(label, (600, 500))
    elif ((point_x[4] + point > x_position and point_x[4] + point < x_position + x_size + 2 * point)):
        if (point_y[4] + point  > y_position and point_y[4]+ point < y_position + y_size+ 2*point):
            point_x[4] = -200
            score += 1
            pygame.mixer.Sound.play(effect)
            textscore = "Score" +":"+" " +str(score)
            label = text.render(textscore, 1, (255, 255, 0))
            screen.blit(label, (600, 500))

    elif ((point_x[5] + point > x_position and point_x[5] + point < x_position + x_size + 2 * point)):
        if (point_y[5] + point  > y_position and point_y[5]+ point < y_position + y_size+ 2*point):
            point_x[5] = -200
            score += 1
            pygame.mixer.Sound.play(effect)
            textscore = "Score" +":"+" " +str(score)
            label = text.render(textscore, 1, (255, 255, 0))
            screen.blit(label, (600, 500))
    elif ((point_x[6] + point > x_position and point_x[6] + point < x_position + x_size + 2 * point)):
        if (point_y[6] + point  > y_position and point_y[6]+ point < y_position + y_size+ 2*point):
            point_x[6] = -200
            score += 1
            pygame.mixer.Sound.play(effect)
            textscore = "Score" +":"+" " +str(score)
            label = text.render(textscore, 1, (255, 255, 0))
            screen.blit(label, (600, 500))
    else:
        textscore = "Score" +":"+" " +str(score)
        label = text.render(textscore, 1, (255, 255, 0))
        screen.blit(label, (600, 500))

#aumento della velocità
def difficolty():
    global speed
    if(tempo > 500 and tempo < 700):

        speed = 25

    if(tempo > 700 and tempo < 1200):
        speed = 30

    if (tempo > 1200 and tempo < 1800):
        speed = 35

    if (tempo > 1800):
        speed = 40
    if (tempo > 2800):
        speed = 45

    if (tempo > 3800):
  
        speed = 50

    if (tempo > 5800):
        speed = 60
#ciclo while presente in tutti i giochi con pygame

while game:

    for evento in pygame.event.get():
        if(evento.type == pygame.QUIT):
            print("fine gioco")
            game = False
        if (evento.type == pygame.KEYDOWN):
           if(evento.key == pygame.K_LEFT)  and x_position > x_size :
               x_position -= x_size

           elif(evento.key == pygame.K_RIGHT) and x_position+x_size < width-x_size:
               x_position += x_size

    screen.fill((0,0,0))

    enemy_cordinate()
    point_cordinate()
    enemy_collision()
    point_collision()
    difficolty()
    textscore = "Score" +":"+" " +str(score)
    label = text.render(textscore, 1, (255, 255, 0))
    screen.blit(label, (600, 500))
    pygame.draw.rect(screen, (0,255,0), (x_position, y_position, x_size, y_size))
    pygame.display.update()
    tempo += 1
    print(tempo)
    clock.tick(speed)

pygame.quit()
