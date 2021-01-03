import sys

import sys
import sdl2
import sdl2.ext


# https://pysdl2.readthedocs.io/en/rel_0_9_7/tutorial/pong.html
WHITE = sdl2.ext.Color(255, 255, 255)
BLACK = sdl2.ext.Color(0, 0, 0)

PADDLE_SPEED = 3
BALL_SPEED = 3

DEFAULT_WIDTH = 1024
DEFAULT_HEIGHT = 1024

RESOURCES = sdl2.ext.Resources(__file__, "resources")


class SoftwareRenderSystem(sdl2.ext.SoftwareSpriteRenderSystem):
    def __init__(self, window):
        super(SoftwareRenderSystem, self).__init__(window)

    def render(self, components):
        sdl2.ext.fill(self.surface, BLACK)
        super(SoftwareRenderSystem, self).render(components)


class TextureRenderSystem(sdl2.ext.TextureSpriteRenderSystem):
    def __init__(self, renderer):
        super(TextureRenderSystem, self).__init__(renderer)
        self.renderer = renderer

    def render(self, components):
        tmp = self.renderer.color
        self.renderer.color = BLACK
        self.renderer.clear()
        self.renderer.color = tmp
        print("render: ", tmp, " , ", components)
        super(TextureRenderSystem, self).render(components)


class MovementSystem(sdl2.ext.Applicator):

    def __init__(self, minx, miny, maxx, maxy):
        super(MovementSystem, self).__init__()
        self.componenttypes = Velocity, sdl2.ext.Sprite
        self.minx = minx
        self.miny = miny
        self.maxx = maxx
        self.maxy = maxy

    def process(self, world, componentsets):
        for velocity, sprite in componentsets:
            swidth, sheight = sprite.size
            sprite.x += velocity.vx
            sprite.y += velocity.vy

            print("MovementSystem ", velocity, " - ", sprite.x, ",", sprite.y)

            sprite.x = max(self.minx, sprite.x)
            sprite.y = max(self.miny, sprite.y)

            pmaxx = sprite.x + swidth
            pmaxy = sprite.y + sheight
            if pmaxx > self.maxx:
                sprite.x = self.maxx - swidth
            if pmaxy > self.maxy:
                sprite.y = self.maxy - sheight

            print("MovementSystem ", velocity, " - ", sprite.x, ",", sprite.y)


class Velocity(object):
    def __init__(self):
        super(Velocity, self).__init__()
        self.vx = 0
        self.vy = 0

    def __str__(self):
        return "(%s,%s)" % (self.vx, self.vy)


class PacMan(sdl2.ext.Entity):
    def __init__(self, world, sprite, posx=0, posy=0):
        self.sprite = sprite
        self.sprite.position = posx, posy
        self.velocity = Velocity()


def main():
    sdl2.ext.init()
    window = sdl2.ext.Window("The Pong Game", size=(DEFAULT_WIDTH, DEFAULT_HEIGHT))
    window.show()

    if "-hardware" in sys.argv:
        print("Using hardware acceleration")
        renderer = sdl2.ext.Renderer(window)
        factory = sdl2.ext.SpriteFactory(sdl2.ext.TEXTURE, renderer=renderer)
    else:
        print("Using software rendering")
        factory = sdl2.ext.SpriteFactory(sdl2.ext.SOFTWARE)

    sp_pacman = factory.from_image(RESOURCES.get_path("pacman.bmp"))
    world = sdl2.ext.World()

    if factory.sprite_type == sdl2.ext.SOFTWARE:
        spriterenderer = SoftwareRenderSystem(window)
    else:
         spriterenderer = TextureRenderSystem(renderer)

    movement = MovementSystem(0, 0, DEFAULT_WIDTH, DEFAULT_HEIGHT)

    pacman = PacMan(world, sp_pacman, 0, 50)
    pacman.velocity.vx = 3
    pacman.velocity.vy = 6

    world.add_system(spriterenderer)
    world.add_system(movement)

    ##############################################################
    running = True
    while running:
        for event in sdl2.ext.get_events():
            if event.type == sdl2.SDL_QUIT:
                running = False
                break
            if event.type == sdl2.SDL_KEYDOWN:
                if event.key.keysym.sym == sdl2.SDLK_UP:
                    pacman.velocity.vy = -3
                elif event.key.keysym.sym == sdl2.SDLK_DOWN:
                    pacman.velocity.vy = +3
                elif event.key.keysym.sym == sdl2.SDLK_LEFT:
                    pacman.velocity.vx = -3
                elif event.key.keysym.sym == sdl2.SDLK_RIGHT:
                    pacman.velocity.vx = 3
        sdl2.SDL_Delay(10)
        world.process()

    return 0


if __name__ == "__main__":
    sys.exit(main())