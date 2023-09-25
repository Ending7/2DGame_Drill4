#2018184042 장진영 2DGame_Drill4
from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
player = load_image('player.png')

running = True
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
dirX, dirY = 0, 0

def handle_events():
    global running, dirX, dirY
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE: 
                running = False
            elif event.key == SDLK_LEFT:
                dirX -=1
            elif event.key == SDLK_RIGHT:
                dirX +=1
            elif event.key == SDLK_UP:
                dirY +=1
            elif event.key == SDLK_DOWN:
                dirY -=1
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_LEFT:
                dirX +=1
            elif event.key == SDLK_RIGHT:
                dirX -=1
            elif event.key == SDLK_UP:
                dirY -=1
            elif event.key == SDLK_DOWN:
                dirY +=1

def rendering():
    global dirX, dirY, x, y
    while running:
        clear_canvas()
        tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
        player.clip_draw(32,683-72,38,45,x,y, 100,100)
        update_canvas()
        handle_events()

        x+= dirX * 10
        y+= dirY * 10
        delay(0.05)

        if not running:
            break



def main():
    rendering()

if __name__ == '__main__':
    main()

