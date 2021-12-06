from PPlay.window import *
from PPlay.gameimage import *
from PPlay.mouse import *
from PPlay.sprite import *

def menu_dificuldade(nivel):
    window = Window(800, 600)
    const = 100
    background = GameImage("menu background.jpg")
    easy_png = GameImage("easy.png")
    medium_png = GameImage("medium.png")
    hard_png = GameImage("hard.png")
    easy_png.x = medium_png.x = hard_png.x = window.width/2 - easy_png.width/2
    easy_png.y = const
    medium_png.y = easy_png.y + const
    hard_png.y = medium_png.y + const
    while True:
        if mouse.is_button_pressed(1) and (mouse.is_over_object(easy_png)):
            return (1)
        if mouse.is_button_pressed(1) and mouse.is_over_object(medium_png):
            return (2)
        if mouse.is_button_pressed(1) and mouse.is_over_object(hard_png):
            return (3)
        background.draw()
        easy_png.draw()
        medium_png.draw()
        hard_png.draw()
        window.update()


def exit_game():
    window.close()


def play(bool):
    window = Window(800, 600)
    background = GameImage("menu background.jpg")
    teclado = Window.get_keyboard()
    while True:
        if teclado.key_pressed("ESC"):
            return True
        background.draw()
        window.update()

window = Window(800, 600)
background = GameImage("menu background.jpg")
iniciar_png = GameImage("iniciar.png")
dificuldade_png = GameImage("Dificuldade.png")
ranking_png = GameImage("Ranking.png")
sair_png = GameImage("Sair.png")

iniciar_png.x = window.width / 3 - iniciar_png.width / 3
dificuldade_png.x = iniciar_png.x
ranking_png.x = iniciar_png.x * 2
sair_png.x = iniciar_png.x * 2

iniciar_png.y = window.height / 5
dificuldade_png.y = window.height * 2 / 5
ranking_png.y = window.height / 5
sair_png.y = window.height * 2 / 5
mouse = Window.get_mouse()
nivel = 0
bool = True

while bool:
    if mouse.is_button_pressed(1) and (mouse.is_over_object(sair_png)):
        exit_game()
    if mouse.is_button_pressed(1) and mouse.is_over_object(dificuldade_png):
        nivel = menu_dificuldade(nivel)
    if mouse.is_button_pressed(1) and mouse.is_over_object(iniciar_png):
        bool = play(bool)
    background.draw()
    iniciar_png.draw()
    dificuldade_png.draw()
    ranking_png.draw()
    sair_png.draw()
    window.update()
    mouse = Mouse()