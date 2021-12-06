from PPlay.window import *
from PPlay.gameimage import *

def menu_tela():
    window = Window(800, 600)
    background = GameImage("menu background.jpg")
    iniciar_png = GameImage("iniciar.png")
    dificuldade_png = GameImage("Dificuldade.png")
    ranking_png = GameImage("Ranking.png")
    sair_png = GameImage("Sair.png")

    iniciar_png.x = window.width/3 - iniciar_png.width/3
    dificuldade_png.x = iniciar_png.x
    ranking_png.x = iniciar_png.x*2
    sair_png.x = iniciar_png.x*2

    iniciar_png.y = window.height/5
    dificuldade_png.y = window.height*2/5
    ranking_png.y = window.height/5
    sair_png.y = window.height*2/5

    while True:
        background.draw()
        iniciar_png.draw()
        dificuldade_png.draw()
        ranking_png.draw()
        sair_png.draw()
        window.update()