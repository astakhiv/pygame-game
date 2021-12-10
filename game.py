import pygame
import animations
import random

pygame.init()
win_size = (360, 780)
win = pygame.display.set_mode(win_size)
pygame.display.set_caption("Cubes game")
# Making background
apple_size = (55, 55)
bg_size = {
    'height': win_size[1] // 1.15,
    'width': win_size[0]
}
menu_bg = pygame.image.load('images/g-bg.jpg')
menu_bg = pygame.transform.scale(menu_bg, (win_size[0], win_size[1]))
bg_1 = pygame.image.load('images/g-bg.png')
bg_1 = pygame.transform.scale(bg_1, (bg_size['width'], bg_size['height']))
bg_1_BG = pygame.transform.scale(bg_1, (win_size[1] * 0.13, win_size[1] * 0.2))
bg_2 = pygame.image.load('images/g-bg_2.png')
bg_2 = pygame.transform.scale(bg_2, (bg_size['width'], bg_size['height']))
bg_2_BG = pygame.transform.scale(bg_2, (win_size[1] * 0.13, win_size[1] * 0.2))
bg_3 = pygame.image.load('images/g-bg_3.png')
bg_3 = pygame.transform.scale(bg_3, (bg_size['width'], bg_size['height']))
bg_3_BG = pygame.transform.scale(bg_3, (win_size[1] * 0.13, win_size[1] * 0.2))
apple = pygame.image.load('images/pixel_apple.png')
apple = pygame.transform.scale(apple, (apple_size[0], apple_size[1]))
clock = pygame.time.Clock()

BLACK = (0, 0, 0)

# player values

player_pos = {
    "x": win_size[0] // 2,
    "y": win_size[1] // 2
}
player_size = (60, 60)
speed = 5
animCount = 0
score_num = 0
Left = False
Right = False
Up = False
Down = False
menu_button_pressed = 0

# food
food_pos = {
    'x': random.randrange(0, win_size[0] - player_size[0], 5),
    'y': random.randrange(60, bg_size['height'] - player_size[0], 5)
}
food_size = (20, 20)
# main buttons size
button_size = {
    'height': win_size[1] * 0.13,
    'width_1': win_size[0] - win_size[0] * 0.06,
    'width_2': win_size[0],
    'width_3': win_size[1] * 0.13,
    'height_2': win_size[1] - bg_size['height']
}


def move(left: bool, right: bool, up: bool, down: bool):
    global Left, Right, Up, Down

    Up = up
    Down = down
    Left = left
    Right = right


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


def isOver_Up(pos):
    if pos[1] < bg_size['height'] * 0.75:
        return True


def isOver_Down(pos):
    if bg_size['height'] // 4 < pos[1] < bg_size['height']:
        return True


def isOver_Left(pos):
    if bg_size['height'] // 4 < pos[1] < bg_size['height'] * 0.75:
        if bg_size['width'] // 2 < pos[0]:
            return True


def isOver_Right(pos):
    if bg_size['height'] // 4 < pos[1] < bg_size['height'] * 0.75:
        if pos[0] < bg_size['width'] // 2:
            return True


# making text
def Text(x, y, text):
    font = pygame.font.SysFont('coicsans', 60)
    follow = font.render(str(text), 1, (0, 0, 0))
    win.blit(follow, (x, y))


# drawing windows
def Menu():
    win.blit(menu_bg, (0, 0))
    if menu_button_pressed <= 1:
        Start_button_2.draw(win, (0, 0, 0))
    else:
        Start_button_1.draw(win, (0, 0, 0))
        Countinue_button.draw(win, (0, 0, 0))
    Exit_button.draw(win, (0, 0, 0))
    Backgroungs_button.draw(win, (0, 0, 0))
    pygame.display.update()


def Backgrounds():
    # buttons
    win.blit(menu_bg, (0, 0))
    BG_1_button.draw(win, (0, 0, 0))
    BG_2_button.draw(win, (0, 0, 0))
    BG_3_button.draw(win, (0, 0, 0))
    Menu_button2.draw(win, (0, 0, 0))
    # images
    win.blit(bg_1_BG, (10, win_size[1] // 2.5))
    win.blit(bg_2_BG, (130, win_size[1] // 2.5))
    win.blit(bg_3_BG, (250, win_size[1] // 2.5))
    pygame.display.update()


def Animations():
    global animCount
    if animCount + 1 >= 20:
        animCount = 0
    if Left:
        win.blit(animations.walkLeft[animCount // 5],
                 (player_pos["x"] - player_size[0] // 2.7, player_pos["y"] - player_size[1] // 1.5))
        animCount += 1
    elif Right:
        win.blit(animations.walkRight[animCount // 5],
                 (player_pos["x"] - player_size[0] // 2.7, player_pos["y"] - player_size[1] // 1.5))
        animCount += 1
    elif Up:
        win.blit(animations.walkUp[animCount // 5],
                 (player_pos["x"] - player_size[0] // 2.7, player_pos["y"] - player_size[1] // 1.5))
        animCount += 1
    elif Down:
        win.blit(animations.walkDown[animCount // 5],
                 (player_pos["x"] - player_size[0] // 2.7, player_pos["y"] - player_size[1] // 1.5))
        animCount += 1
    else:
        win.blit(animations.playerStand,
                 (player_pos["x"] - player_size[0] // 2.7, player_pos["y"] - player_size[1] // 1.5))


def Game():
    global animCount
    win.fill((0, 0, 0))
    Menu_button.draw(win, (0, 0, 0))
    if BG_2:
        win.blit(bg_2, (0, 0))
    elif BG_3:
        win.blit(bg_3, (0, 0))
    else:
        win.blit(bg_1, (0, 0))
    Text(0, 0, score_num)
    win.blit(apple,
             (food_pos['x'] - apple_size[0] // 3, food_pos['y'] - apple_size[1] // 3, food_size[0], food_size[1]))
    Animations()
    pygame.display.update()


# creating buttons
# menu buttons
Start_button_1 = Button((255, 209, 0), 10, win_size[1] // 6.7, button_size['width_1'], button_size['height'], 'Start')
Start_button_2 = Button((255, 209, 0), 10, win_size[1] // 3.45, button_size['width_1'], button_size['height'], 'Start')
Countinue_button = Button((255, 209, 0), 10, win_size[1] // 3.45, button_size['width_1'], button_size['height'],
                          'Countinue')
Exit_button = Button((255, 209, 0), 10, win_size[1] // 2.32, button_size['width_1'], button_size['height'], 'Exit')
Backgroungs_button = Button((255, 209, 0), 10, win_size[1] // 1.75, button_size['width_1'], button_size['height'],
                            'Backgrounds')
# game buttons
Menu_button = Button((255, 209, 0), 0, win_size[1] - button_size['height'], button_size['width_2'],
                     button_size['height'], 'Menu')
# backgrounds buttons
BG_1_button = Button((255, 209, 0), 10, win_size[1] * 0.01, button_size['width_3'], button_size['height'], 'BG-1')
BG_2_button = Button((255, 209, 0), 130, win_size[1] * 0.01, button_size['width_3'], button_size['height'], 'BG-2')
BG_3_button = Button((255, 209, 0), 250, win_size[1] * 0.01, button_size['width_3'], button_size['height'], 'BG-3')
Menu_button2 = Button((255, 209, 0), 10, 650, button_size['width_1'], button_size['height'], 'Menu')

run = True
# window
menu = True
game = False
background = False
# background types
BG_2 = False
BG_3 = False
# starting game

while run:
    clock.tick(30)
    pygame.time.delay(20)
    pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    if not menu:
        # menu button function
        if game:
            if event.type == pygame.MOUSEBUTTONDOWN and Menu_button.isOver(pos):
                menu = True
                game = False
                Menu_button.color = (117, 96, 0)
                menu_button_pressed += 2
            else:
                Menu_button.color = (255, 209, 0)
            # changing food position
            if food_pos['x'] <= player_pos["x"] <= food_pos['x'] + food_size[0] or \
                    food_pos['x'] <= player_pos["x"] + player_size[0] <= food_pos['x'] + food_size[0]:
                if food_pos['y'] <= player_pos["y"] <= food_pos['y'] + food_size[1] or \
                        food_pos['y'] <= player_pos["y"] + player_size[1] <= food_pos['y'] + food_size[1]:
                    food_pos = {
                        'x': random.randrange(0, win_size[0] - player_size[0], 5),
                        'y': random.randrange(60, bg_size['height'] - player_size[0], 5)
                    }
                    score_num += 1
            move(False, False, False, False)
            if event.type == pygame.MOUSEBUTTONDOWN and isOver_Up(pos):
                if player_pos["y"] > 40:
                    player_pos['y'] -= speed
                    move(False, False, True, False)

            if event.type == pygame.MOUSEBUTTONDOWN and isOver_Down(pos):
                if player_pos["y"] < bg_size['height'] - player_size[0]:
                    player_pos['y'] += speed
                    move(False, False, False, True)

            if event.type == pygame.MOUSEBUTTONDOWN and isOver_Left(pos):
                if player_pos["x"] < win_size[0] - player_size[0]:
                    player_pos['x'] += speed
                    move(False, True, False, False)

            if event.type == pygame.MOUSEBUTTONDOWN and isOver_Right(pos):
                if player_pos["x"] > 0:
                    player_pos['x'] -= speed
                    move(True, False, False, False)

            Game()
        elif backgrounds:
            # menu button
            if event.type == pygame.MOUSEBUTTONDOWN and Menu_button2.isOver(pos):
                menu = True
                backgrounds = False
            else:
                Menu_button.color = (255, 209, 0)
            # BG 1 button
            if event.type == pygame.MOUSEBUTTONDOWN and BG_1_button.isOver(pos):
                BG_2 = False
                BG_3 = False
                BG_1_button.color = (117, 96, 0)
                menu = True
                backgrounds = False
            else:
                BG_1_button.color = (255, 209, 0)
            # BG 2 button
            if event.type == pygame.MOUSEBUTTONDOWN and BG_2_button.isOver(pos):
                BG_2 = True
                BG_3 = False
                BG_2_button.color = (117, 96, 0)
                menu = True
                backgrounds = False
            else:
                BG_2_button.color = (255, 209, 0)
            # BG 3 button
            if event.type == pygame.MOUSEBUTTONDOWN and BG_3_button.isOver(pos):
                BG_3 = True
                BG_2 = False
                BG_3_button.color = (117, 96, 0)
                menu = True
                backgrounds = False
            else:
                BG_3_button.color = (255, 209, 0)
            Backgrounds()

    else:
        # start button function
        if menu_button_pressed <= 1:
            if event.type == pygame.MOUSEBUTTONDOWN and Start_button_2.isOver(pos):
                menu = False
                game = True
                player_pos = {
                    "x": win_size[0] // 2,
                    "y": win_size[1] // 2
                }
                score_num = 0
                Start_button_2.color = (117, 96, 0)
            else:
                Start_button_2.color = (255, 209, 0)
        else:
            if event.type == pygame.MOUSEBUTTONDOWN and Start_button_1.isOver(pos):
                menu = False
                game = True
                player_pos = {
                    "x": win_size[0] // 2,
                    "y": win_size[1] // 2
                }
                score_num = 0
                Start_button_1.color = (117, 96, 0)
            else:
                Start_button_1.color = (255, 209, 0)
        # Continue button function
        if event.type == pygame.MOUSEBUTTONDOWN and Countinue_button.isOver(pos):
            menu = False
            game = True
            Countinue_button.color = (117, 96, 0)
        else:
            Countinue_button.color = (255, 209, 0)
        # exit button function
        if event.type == pygame.MOUSEBUTTONDOWN and Exit_button.isOver(pos):
            run = False
            Exit_button.color = (117, 96, 0)
        else:
            Exit_button.color = (255, 209, 0)
        # backgrounds button function
        if event.type == pygame.MOUSEBUTTONDOWN and Backgroungs_button.isOver(pos):
            Backgroungs_button.color = (117, 96, 0)
            backgrounds = True
            menu = False
        else:
            Backgroungs_button.color = (255, 209, 0)
        Menu()

pygame.quit()
