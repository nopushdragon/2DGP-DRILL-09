from pico2d import *
from boy import Boy
from grass import Grass
import game_world

# Game object class here


def handle_events():
    global running

    event_list = get_events()
    for event in event_list:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        else:
            boy.handle_event(event)


def reset_world():
    global boy

    back_grass = Grass()
    game_world.add_object(back_grass,0)

    boy = Boy()
    boy.y = 50
    game_world.add_object(boy,1)

    front_grass = Grass()
    front_grass.y = 15
    game_world.add_object(front_grass, 2)

def update_world():
    game_world.update()

def render_world():
    clear_canvas()
    game_world.render()
    update_canvas()

running = True

open_canvas()
reset_world()
# game loop
while running:
    handle_events()
    update_world()
    render_world()
    delay(0.01)
# finalization code
close_canvas()
