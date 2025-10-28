from pico2d import load_image


class Grass:
    x = 400
    y = 30

    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        pass
