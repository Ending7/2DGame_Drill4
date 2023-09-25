#2018184042 장진영 2DGame_Drill4
from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
player = load_image('player.png')




def rendering():
    while True:
        clear_canvas()
        tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
        player.clip_draw(32,683-72,38,45,50,100,100,100)
        update_canvas()




def main():
    rendering()

if __name__ == '__main__':
    main()

