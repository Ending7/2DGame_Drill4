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
def again(frame):
    global index, x, y  
    frameX, frameY, width, height = frame[index]
    if motion == 0 or motion == 3 or motion == 5 or motion == 7 or motion == 9:
        player.clip_draw(frameX,frameY,width,height,x,y, 100,100)
    elif motion == 1 or motion == 2 or motion == 4 or motion == 6 or motion == 8:
        player.clip_composite_draw(frameX,frameY,width,height, 0, 'h', x, y, 100,100)

def player_idle():
    global index  
    frame = [(32, 683-72,39,60), (83, 683-72,39,60), (132, 683-72,39,60), (182, 683-72,39,60)]
    again(frame) 
    index += 1
    if(index == 4):
        index = 0

def player_die():
    global index
    frame = [(32, 683-203,35,60), (70, 683-203,40,60), (120,683-203,57,60), (180,683-203,43,60), (227,683-203,43,60)]
    again(frame) 
    index += 1
    if(index == 5):
        index = 0

def player_attack():
    global index
    frame = [(29, 683-362,37,60), (74, 683-362,51,60),(131, 683-362,46,60),(179, 683-362,45,60),(223, 683-362,47,60),
    (273, 683-362,57,60),(330, 683-362,52,60),(386, 683-362,36,60),(435, 683-362,33,60),(472, 683-362,36,60),
    (514, 683-362,55,60),(569, 683-362,39,60),(611, 683-362,36,60),(652, 683-362,38,60)]
    again(frame) 
    index += 1
    if(index == 14):
        index = 0

def player_run():
    global index
    frame = [(27,683-428,40,60), (71, 683-428,41,60), (123,683-428,38,60), 
    (173,683-428,33,60), (213,683-428,46,60), (261,683-428,41,60), 
    (312,683-428,38,60), (358,683-428,32,60)]
    again(frame)
    index += 1
    if(index == 8):
        index = 0

def player_animation():
    global dirX, dirY, motion
    if motion == 0 or motion == 1:
        player_idle()        
    if motion == 2 or motion == 3 or motion == 4 or motion == 5:
        player_run()
    if motion == 6 or motion == 7:
        player_die()
    if motion == 8 or motion == 9:
        player_attack()

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
                index = 0
                dirX -=1
                motion = 2
                tempmotion = 2
            elif event.key == SDLK_RIGHT:
                index = 0
                dirX +=1
                motion = 3
                tempmotion = 3
            elif event.key == SDLK_UP:
                index = 0
                dirY +=1
                if tempmotion == 2:
                    motion = 4
                if tempmotion == 3:
                    motion = 5
            elif event.key == SDLK_DOWN:
                index = 0
                dirY -=1
                if tempmotion == 2:
                    motion = 4
                if tempmotion == 3:
                    motion = 5
            elif event.key == SDLK_d:
                index = 0
                if tempmotion == 2:
                    motion = 6
                if tempmotion == 3:
                    motion = 7
            elif event.key == SDLK_a:
                index = 0
                if tempmotion == 2:
                    motion = 8
                if tempmotion == 3:
                    motion = 9    

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
            elif event.key == SDLK_d:
                index = 0
            elif event.key == SDLK_a:
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

