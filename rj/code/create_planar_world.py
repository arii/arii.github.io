"""
Author: Ariel Anders

gui_b2d.py

This createas a simple box2d world for robot juggling.
"""
import pygame
from pygame.locals import (QUIT, KEYDOWN, K_ESCAPE)
from Box2D import b2PolygonShape, b2CircleShape, b2World
class GuiB2D:
    """
    Simple pygame gui for a b2world used in the planar simulator demos.
    
    gui = GuiB2D( (640, 640), (32, 24), 60)
    gui.running=True
    gui.draw(world)
    pygame.quit()
    print('Done!')
    """
    def __init__(self, (screenX,screenY), (simX, simY), fps):
        self.running = True
        self.COLORS = {
            'bg': (253, 246, 227),
            'boundsU': (181,137,0),
            'ground': (133, 153, 0), 
            'robot': (0, 43, 54),
            'boundsL': (220, 50, 47),
            'ball': (211, 54, 130),
            None: (38, 139, 210),
        }
        self.SIZE = screenX, screenY
        self.PPM = float(screenX)/simX
        self.FPS = fps
        pygame.init()
        self.screen = pygame.display.set_mode(self.SIZE, pygame.DOUBLEBUF, 32)
        pygame.display.set_caption("Planar Simulator World")
        self.clock = pygame.time.Clock()
        
        b2PolygonShape.draw=self.draw_polygon
        b2CircleShape.draw=self.draw_circle

    def draw_polygon(self, polygon, body, fixture):
        vertices=[(body.transform*v)*self.PPM for v in polygon.vertices]
        vertices=[(v[0], self.SIZE[1]-v[1]) for v in vertices]
        color = self.COLORS[body.userData]
        pygame.draw.polygon(self.screen, color, vertices)
            
    def draw_circle(self, circle, body, fixture):
        position=(body.transform*fixture.shape.pos)*self.PPM
        position=(position[0], self.SIZE[1]-position[1])
        pygame.draw.circle(self.screen, self.COLORS[body.userData],             [int(x) for x in position], int(circle.radius*self.PPM))
        
    def draw(self, world):
        self.screen.fill(self.COLORS['bg'])
        for event in pygame.event.get():
            if event.type == QUIT or                 (event.type == KEYDOWN and event.key == K_ESCAPE):
                self.running = False
        for body in  world.bodies:
            for fixture in body.fixtures:
                fixture.shape.draw(fixture.shape, body, fixture)

        pygame.display.flip()
        self.clock.tick(self.FPS)
    
    def start(self):
        self.running = True
        
    def stop(self):
        pygame.quit()
 

def createPlanarWorld(gravity):
    """
    world, bodies = create_planar_world(gravity = 9.81)
    """
    world = b2World(gravity=(0, -gravity), doSleep=False)
    world.warmStarting = True
    world.continuousPhysics = True
    world.subStepping = False


    # And a static body to hold the ground shape
    ground_body = world.CreateStaticBody(
        position=(0, 0),
        shapes=b2PolygonShape(box=(50, 1)),
    )
    ground_body.userData='ground'

    goal_upper = world.CreateStaticBody(
        position=(0,0),
        shapes=b2PolygonShape(box=(5, .001)),
    )
    goal_upper.userData = 'boundsU'

    goal_lower = world.CreateStaticBody(
        position=(0,0),
        shapes=b2PolygonShape(box=(5, .001)),
    )
    goal_lower.userData = 'boundsL'

    # Create a ball to bounce
    ball = world.CreateDynamicBody(position=(0,0), angle=0)
    ball.CreateCircleFixture(radius=.5, density=.1, friction=0.)
    ball.userData = 'ball'

    # Construct the robot paddle
    robot = world.CreateDynamicBody(position=(0,0), angle=0)
    robot.CreatePolygonFixture(box=(5, .1), density=1., friction=0.)
    robot.userData = 'robot'

    bodies = {}
    for body in world.bodies:
        bodies[body.userData]= body

    return world, bodies

