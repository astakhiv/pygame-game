import pygame
import random
import animations

pygame.init()
win_size = (360, 780)
win = pygame.display.set_mode(win_size)
pygame.display.set_caption("Cubes game")
# Making background
bg_size = {
    'height': win_size[1] // 1.55,
    'width': win_size[0]
}
bg = pygame.image.load('images/g-bg.png')
bg = pygame.transform.scale(bg, (bg_size['width'], bg_size['height']))

clock = pygame.time.Clock()

BLACK = (0, 0, 0)

# player values

player_pos = {
    "x": win_size[0] // 2,
    "y": win_size[1] // 2.15
}
player_size = (50, 50)
speed = 5

isJump = False
jumpCount = 10
animCount = 0
left = False
right = False
up = False
down = False

# main buttons size
button_size = {
    'height': win_size[1] * 0.13,
    'width_1': win_size[0] - win_size[0] * 0.06,
    'width_2': win_size[0],
    'height_2': win_size[1] - bg_size['height'],
    'control_button_height': win_size[0] * 0.2,
    'control_button_width': win_size[0] * 0.2
}
# food values
food_pos = {
    "x": round(random.randrange(0, win_size[0], 5)),
    "y": round(random.randrange(0, win_size[1] // 1.55, 5)),
}

food_size = (20, 20)
food_eaten = 0


# Making buttons


class Button:
    def __init__(self, color, btn_x, btn_y, btn_width, btn_height, text=''):
        self.color = color
        self.x = btn_x
        self.y = btn_y
        self.width = btn_width
        self.height = btn_height
        self.text = text

    def draw(self, win, outline=None):
        if outline:
            pygame.draw.rect(win, outline, (self.x - 2, self.y - 2, self.width + 4, self.height + 4), 0)

        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height), 0)

        if self.text != '':
            font = pygame.font.SysFont('coicsans', 60)
            text = font.render(self.text, 1, (0, 0, 0))
            win.blit(text, (
                self.x + (self.width / 2 - text.get_width() / 2), self.y + (self.height / 2 - text.get_height() / 2)))

    def isOver(self, pos):
        if self.x < pos[0] < self.x + self.width:
            if self.y < pos[1] < self.y + self.height:
                return True


# drawing windows

def Menu():
    win.fill((202, 228, 241))
    Start_button.draw(win, (0, 0, 0))
    Exit_button.draw(win, (0, 0, 0))
    pygame.display.update()


def Game():
    global animCount
    Up_button.draw(win, (0, 0, 0))
    Down_button.draw(win, (0, 0, 0))
    Left_button.draw(win, (0, 0, 0))
    Right_button.draw(win, (0, 0, 0))
    Menu_button.draw(win, (0, 0, 0))
    win.blit(bg, (0, 0))

    if animCount + 1 >= 20:
        animCount = 0

    if left:
        win.blit(animations.walkLeft[animCount // 5], (player_pos["x"], player_pos["y"]))
        animCount += 1
    elif right:
        win.blit(animations.walkRight[animCount // 5], (player_pos["x"], player_pos['y']))
        animCount += 1
    elif up:
        win.blit(animations.walkUp[animCount // 5], (player_pos["x"], player_pos["y"]))
        animCount += 1
    elif down:
        win.blit(animations.walkDown[animCount // 5], (player_pos["x"], player_pos["y"]))
        animCount += 1
    else:
        win.blit(animations.playerStand, (player_pos["x"], player_pos["y"]))
    pygame.display.update()


# creating buttons
Start_button = Button((255, 209, 0), 10, 200, button_size['width_1'], button_size['height'], 'Start')
Exit_button = Button((255, 209, 0), 10, 400, button_size['width_1'], button_size['height'], 'Exit')
Menu_button = Button((255, 209, 0), 0, 505, button_size['width_2'], button_size['height'], 'Menu')
Up_button = Button((255, 209, 0), win_size[0] // 2.5, 620, button_size['control_button_width'],
                   button_size['control_button_height'], 'U')
Down_button = Button((255, 209, 0), win_size[0] // 2.5, 700, button_size['control_button_width'],
                     button_size['control_button_height'], 'D')
Left_button = Button((255, 209, 0), 60, 660, button_size['control_button_width'], button_size['control_button_height'],
                     'L')
Right_button = Button((255, 209, 0), 230, 660, button_size['control_button_width'],
                      button_size['control_button_height'], 'R')
run = True
menu = True
# starting game
while run:
    clock.tick(30)
    pygame.time.delay(20)
    pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    if not menu:

        if event.type == pygame.MOUSEBUTTONDOWN:
            if Menu_button.isOver(pos):
                menu = True
        if event.type == pygame.MOUSEMOTION:
            if Menu_button.isOver(pos):
                Menu_button.color = (117, 96, 0)
            else:
                Menu_button.color = (255, 209, 0)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if Up_button.isOver(pos):
                player_pos['y'] -= speed
                up = True
                down = False
                left = False
                right = False
                Up_button.color = (117, 96, 0)
            else:
                Up_button.color = (255, 209, 0)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if Down_button.isOver(pos):
                player_pos['y'] += speed
                down = True
                up = False
                left = False
                right = False
                Down_button.color = (117, 96, 0)
            else:
                Down_button.color = (255, 209, 0)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if Right_button.isOver(pos):
                player_pos['x'] += speed
                down = False
                up = False
                left = False
                right = True
                Right_button.color = (117, 96, 0)
            else:
                Right_button.color = (255, 209, 0)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if Left_button.isOver(pos):
                player_pos['x'] -= speed
                down = False
                up = False
                left = True
                right = False
                Left_button.color = (117, 96, 0)
            else:
                Left_button.color = (255, 209, 0)
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            if player_pos["x"] > 0:
                player_pos["x"] -= speed
                left = True
                right = False
                up = False
                down = False
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            if player_pos["x"] < win_size[0]:
                player_pos["x"] += speed
                right = True
                left = False
                up = False
                down = False
        elif keys[pygame.K_UP] or keys[pygame.K_w]:
            if player_pos["y"] > 0:
                player_pos["y"] -= speed
                up = True
                down = False
                left = False
                right = False
        elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
            if player_pos["y"] < bg_size['height']:
                player_pos["y"] += speed
                down = True
                up = False
                left = False
                right = False
        else:
            left = False
            right = False
            up = False
            down = False

        Game()
    else:
        if event.type == pygame.MOUSEBUTTONDOWN:
            if Start_button.isOver(pos):
                menu = False
        if event.type == pygame.MOUSEMOTION:
            if Start_button.isOver(pos):
                Start_button.color = (117, 96, 0)
            else:
                Start_button.color = (255, 209, 0)

        if event.type == pygame.MOUSEBUTTONDOWN:
            if Exit_button.isOver(pos):
                run = False

        if event.type == pygame.MOUSEMOTION:
            if Exit_button.isOver(pos):
                Exit_button.color = (117, 96, 0)
            else:
                Exit_button.color = (255, 209, 0)

            Menu()

pygame.quit()
