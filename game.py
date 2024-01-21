# Name: Kaden Nguyen
# ID: YNC5AD
# Description: Players will play as circle cells, and their goal is to try to reach a score of 300 by either 1) eating consumables laid out throughout the map or 2) eating smaller cell-players.
# Basic features:
    # Players will use the mouse to navigate the direction of their cell
    # The game will end when the player gets eaten by a bigger player or achieves a score of 300, or another player reaches 300
    # The cells will change size based on many points have been gained
# Additional features:
    # Object-oriented code: there will a cell class to represent players, enemies, and consumables
    # Enemies: there will be enemy cells that are trying to consume the player and other enemy cells
    # Collectables: the consumables will be collectable and will contribute to the mass of the player
    # Scrolling level: the map is 1600x1200, but the screen window is 800x600. Player can access unseen parts by moving mouse towards area.
import uvage
import random
from entities import Cell


screen_width = 800
screen_height = 600
mapsizex = 1600
mapsizey = 1200
camera = uvage.Camera(screen_width, screen_height)
colors = {1: 'red',
          2: 'orange',
          3: 'yellow',
          4: 'green',
          5: 'purple',
          6: 'cyan',
          7: 'aquamarine',
          8: 'brown',
          9: 'chocolate',
          10: 'cornflowerblue',
          11: 'darkblue',
          12: 'darkgreen',
          13: 'darkorchid ',
          14: 'deeppink',
          15: 'fuchsia',
          16: 'darkolivegreen1',
          17: 'aquamarine4',
          18: 'deeppink3',
          }

numenemies = 10
numfood = int(mapsizey/6)

#end conditions
gameover = False
wongame = False

#bounds for randomly generated food and enemies
minfoodsize = 2
maxfoodsize = 4
mincellsize = 10
maxcellsize = 20

enemies = []
food = []

#creates cells
player = Cell(mapsizex/2, mapsizey/2, 10, 'black')
for i in range(numenemies):
    enemies.append(Cell(random.randint(0, mapsizex), random.randint(0, mapsizey), random.randint(mincellsize, maxcellsize), colors[random.randint(1, len(colors))]))
for i in range(numfood):
    food.append(Cell(random.randint(0, mapsizex), random.randint(0, mapsizey), random.randint(minfoodsize, maxfoodsize), colors[random.randint(1, len(colors))]))

def tick():
    global gameover, wongame
    if not gameover:
        if player.radius > 300: #player wins
            wongame = True
            gameover = True
        for enemy in enemies:
            if enemy.radius > 300: #player loses, another player won
                gameover = True
        #player movement
        if (abs(player.x() - camera.mousex) > player.get().speedx) and (player.x() < camera.mousex) and (player.x() < mapsizex):
            player.moveright()
        elif (abs(player.x() - camera.mousex) > player.get().speedx) and (player.x() > camera.mousex) and (player.x() > 0):
            player.moveleft()
        if (abs(player.y() - camera.mousey) > player.get().speedy) and (player.y() < camera.mousey) and (player.y() < mapsizey):
            player.movedown()
        elif (abs(player.y() - camera.mousey) > player.get().speedy) and (player.y() > camera.mousey) and (player.y() > 0):
            player.moveup()
        #enemy run away from player if close enough
        for i in range(len(enemies)):
            if abs(enemies[i].x() - player.x()) < (enemies[i].radius + player.radius) and abs(enemies[i].y() - player.y()) < (enemies[i].radius + player.radius):  # close enough
                if enemies[i].radius < player.radius:  # smaller than other
                    if enemies[i].x() < player.x() and (enemies[i].x() < mapsizex):  # to the left
                        enemies[i].moveleft()
                    elif enemies[i].x() > player.x() and (enemies[i].x() > 0):  # to the right
                        enemies[i].moveright()

        #enemy movement x direction
        for i in range(len(enemies)):
            for j in range(len(enemies)):
                #run away from other bigger enemies
                if abs(enemies[i].x() - enemies[j].x()) < (enemies[i].radius + enemies[j].radius) and abs(enemies[i].y() - enemies[j].y()) < (enemies[i].radius + enemies[j].radius): #close enough
                    if enemies[i].radius < enemies[j].radius: #smaller than other
                        if enemies[i].x() < enemies[j].x() and (enemies[i].x() > 0): #to the left
                            enemies[i].moveleft()
                            break
                        elif enemies[i].x() > enemies[j].x() and (enemies[i].x() < mapsizex): #to the right
                            enemies[i].moveright()
                            break
                else:
                    if enemies[i].x() < enemies[i].destX and (enemies[i].x() < mapsizex):
                        enemies[i].moveright()
                        break
                    elif enemies[i].x() > enemies[i].destX and (enemies[i].x() > 0):
                        enemies[i].moveleft()
                        break
            if abs(enemies[i].x() - enemies[i].destX) < enemies[i].radius:
                enemies[i].destX = random.randint(0, mapsizex)
        #enemy movement y direction
        for i in range(len(enemies)):
            for j in range(len(enemies)):
                #run away from other bigger enemies
                if abs(enemies[i].x() - enemies[j].x()) < (enemies[i].radius + enemies[j].radius) and abs(enemies[i].y() - enemies[j].y()) < (enemies[i].radius + enemies[j].radius): #close enough
                    if enemies[i].radius < enemies[j].radius: #smaller than other
                        if enemies[i].y() < enemies[j].y() and (enemies[i].y() < mapsizey): #to the left
                            enemies[i].movedown()
                            break
                        elif enemies[i].y() > enemies[j].y() and (enemies[i].y() > 0): #to the right
                            enemies[i].moveup()
                            break
                else:
                    if enemies[i].y() < enemies[i].destY and (enemies[i].y() < mapsizey):
                        enemies[i].movedown()
                        break
                    elif enemies[i].y() > enemies[i].destY and (enemies[i].y() > 0):
                        enemies[i].moveup()
                        break
            if abs(enemies[i].y() - enemies[i].destY) < enemies[i].radius:
                enemies[i].destY = random.randint(0, mapsizey)

        #food consumption
        for i in range(len(food)):
            if player.get().touches(food[i].get()):
                player.grow(1)
                food.pop(i)
                food.append(Cell(random.randint(0, mapsizex), random.randint(0, mapsizey), random.randint(minfoodsize, maxfoodsize), colors[random.randint(1, len(colors))]))
                break
        for i in range(len(food)):
            for j in range(len(enemies)):
                if enemies[j].get().touches(food[i].get()):
                    enemies[j].grow(1)
                    food.pop(i)
                    food.append(
                        Cell(random.randint(0, mapsizex), random.randint(0, mapsizey), random.randint(minfoodsize, maxfoodsize),
                             'green'))
                    continue
        #players eating other players
        for i in range(len(enemies)):
            if player.get().contains(enemies[i].x(), enemies[i].y()):
                if player.radius > enemies[i].radius:
                    player.grow(enemies[i].radius/2)
                    enemies.pop(i)
                    enemies.append(Cell(random.randint(0, mapsizex), random.randint(0, mapsizey), random.randint(mincellsize, maxcellsize), colors[random.randint(1, len(colors))]))
                else:
                    gameover = True
        for i in range(len(enemies)):
            for j in range(len(enemies)):
                if i != j and enemies[i].get().contains(enemies[j].x(), enemies[j].y()):
                    if enemies[i].radius > enemies[j].radius:
                        enemies[i].grow(enemies[j].radius/2)
                        enemies.pop(j)
                        enemies.append(Cell(random.randint(0, mapsizex), random.randint(0, mapsizey),
                                            random.randint(mincellsize, maxcellsize), colors[random.randint(1, len(colors))]))

        #draw
        camera.clear('dark gray')
        camera.draw(uvage.from_color(mapsizex/2, mapsizey/2, 'white', mapsizex, mapsizey))
        camera.draw(uvage.from_image(mapsizex/2, mapsizey/2, "map.png"))
        for i in range(len(enemies)):
            camera.draw(enemies[i].get())
            camera.draw(uvage.from_text(enemies[i].x(), enemies[i].y(), str(round(enemies[i].radius, 2)), round(enemies[i].radius), 'white'))
        for i in range(len(food)):
            camera.draw(food[i].get())
        camera.draw(player.get())
        camera.draw(uvage.from_text(player.x(), player.y(), str(round(player.radius, 2)), round(player.radius), 'white'))
        print(player.radius)
        camera.center = [player.x(), player.y()]
    elif gameover and wongame:
        camera.clear('green')
        camera.draw(uvage.from_text(player.x(), player.y(), 'You won!', 100, 'white'))
    elif gameover and not(wongame):
        camera.clear('red')
        camera.draw(uvage.from_text(player.x(), player.y(), 'GAME OVER', 100, 'white'))
    camera.display()

uvage.timer_loop(30, tick)