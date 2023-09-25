#2018184042 장진영 2DGame_Drill4
#프레임 이미지 크기가 고정되지 않은 sprite sheet 사용
from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
player = load_image('player.png')

running = True
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
dirX, dirY, motion, tempmotion, index = 0, 0, 0, 3, 0

def player_idle():
    global index, x, y  
    frame = [(32, 683-72,39,45), (83, 683-72,39,45), (132, 683-72,39,45), (182, 683-72,39,45)]
    frameX, frameY, width, height = frame[index]
    if motion == 0:
        player.clip_draw(frameX,frameY,width,height,x,y, 100,100)
    elif motion == 1:
        player.clip_composite_draw(frameX,frameY,width,height, 0, 'h', x, y, 100,100)
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
    global index, x, y 
    frame = [(27,683-428,40,45), (71, 683-428,41,45), (123,683-428,38,45), 
    (173,683-428,33,45), (213,683-428,46,45), (261,683-428,41,45), 
    (312,683-428,38,45), (358,683-428,32,45)]
    frameX, frameY, width, height = frame[index]
    if motion == 3 or motion == 5:
        player.clip_draw(frameX,frameY,width,height,x,y, 100,100)
    elif motion == 2 or motion == 4:
        player.clip_composite_draw(frameX,frameY,width,height, 0, 'h', x, y, 100,100)
    index += 1
    if(index == 8):
        index = 0

def player_jump2():
    pass
def player_animation():
    global dirX, dirY, motion
    if motion == 0 or motion == 1:
        player_idle()        
    if motion == 2 or motion == 3 or motion == 4 or motion == 5:
        player_run()

def handle_events():
    global running, dirX, dirY, index, motion, tempmotion
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE: 
                running = False
            elif event.key == SDLK_LEFT:
                dirX -=1
                motion = 2
                tempmotion = 2
            elif event.key == SDLK_RIGHT:
                dirX +=1
                motion = 3
                tempmotion = 3
            elif event.key == SDLK_UP:
                dirY +=1
                if tempmotion == 2:
                    motion = 4
                if tempmotion == 3:
                    motion = 5
            elif event.key == SDLK_DOWN:
                dirY -=1
                if tempmotion == 2:
                    motion = 4
                if tempmotion == 3:
                    motion = 5

        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dirX -=1
                if dirX == 0 and dirY ==0:
                    motion = 0
                index = 0
            elif event.key == SDLK_LEFT:
                dirX +=1
                if dirX == 0 and dirY ==0:
                    motion = 1
                index = 0         
            elif event.key == SDLK_UP:
                dirY -=1
                if dirX == 0 and dirY ==0:
                    if tempmotion ==2:
                        motion = 1
                    elif tempmotion == 3:
                        motion = 0
                index = 0  
            elif event.key == SDLK_DOWN:
                dirY +=1
                if dirX == 0 and dirY ==0:
                    if tempmotion ==2:
                        motion = 1
                    elif tempmotion == 3:
                        motion = 0
                index = 0  

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
        delay(0.05)

        if not running:
            break

def main():
    rendering()

if __name__ == '__main__':
    main()

