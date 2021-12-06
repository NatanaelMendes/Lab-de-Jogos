from PPlay.window import *
from PPlay.gameimage import *

def dificuldade_menu():
    window = Window(800, 600)
    background = GameImage("menu background.jpg")
    easy_png = GameImage("easy.png")
    medium_png = GameImage("medium.png")
    hard_png = GameImage("hard.png")
"""    easy_png.x = medium_png.x= hard_png.x = """
    while True:
        background.draw()
        easy_png.draw()
    """        medium_png.draw()
            hard_png.draw()"""