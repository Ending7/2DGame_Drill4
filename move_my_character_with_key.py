#2018184042 장진영 2DGame_Drill4
#프레임 이미지 크기가 고정되지 않은 sprite sheet 사용
from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
player = load_image('player.png')

running = True
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
dirX, dirY, motion, index = 0, 0, 0, 0

def player_idle():
    global index, x, y  
    frame = [(32, 683-72,39,45), (83, 683-72,39,45), (132, 683-72,39,45), (182, 683-72,39,45)]
    frameX, frameY, width, height = frame[index]
    player.clip_draw(frameX,frameY,width,height,x,y, 100,100)
    index += 1
    if(index == 4):
        index = 0

def player_heading():
    pass
def player_die():
    pass
def player_jump():
    pass
def player_attack():
    pass
def player_run():
    pass
def player_jump2():
    pass
def player_animation():
    global dirX, dirY
    if dirX == 0 and dirY == 0:
        player_idle()        
  

def handle_events():
    global running, dirX, dirY, index
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
        player_animation()
        update_canvas()
        handle_events()

        x+= dirX * 10
        y+= dirY * 10
        delay(0.5)

        if not running:
            break

def main():
    rendering()

if __name__ == '__main__':
    main()

