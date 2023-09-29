import pygame
from pygame.locals import *
from rt import RayTracer
from figures import *
from lights import *
from materials import *

width = 750
height = 600

pygame.init()
screen = pygame.display.set_mode((width, height), pygame.DOUBLEBUF | pygame.HWACCEL | pygame.HWSURFACE)
screen.set_alpha(None)

raytracer = RayTracer(screen)
raytracer.envMap = pygame.image.load("textures/natural.bmp")
raytracer.rtClearColor(0.25, 0.25, 0.25)

brick = Material(diffuse=(1, 0.4, 0.4), spec=8, Ks=0.01,matType=REFLECTIVE)
grass = Material(diffuse=(0.4, 1, 0.4), spec=32, Ks=0.1,matType=REFLECTIVE)
water = Material(diffuse=(0.4, 0.4, 1), spec=256, Ks=0.2,matType=OPAQUE)
mirror = Material(diffuse=(0.9, 0.9, 0.9), spec=64, Ks=0.2, matType=OPAQUE)
glass = Material(diffuse=(0.9, 0.9, 0.9), spec=64, Ks=0.15, ior=1.5, matType=TRANSPARENT)
diamond = Material(diffuse=(0.9, 0.9, 0.9), spec=128, Ks=0.2, ior=2.417, matType=TRANSPARENT)


raytracer.scene.append(Sphere(position=(-3, 1, -7), radius=1, material=glass))
raytracer.scene.append(Sphere(position=(3, 1, -7), radius=1, material=diamond))
raytracer.scene.append(Sphere(position=(0, 2, -6), radius=1, material=mirror))
raytracer.scene.append(Sphere(position=(-3, -2, -7), radius=1, material=brick))
raytracer.scene.append(Sphere(position=(3, -2, -7), radius=1, material=grass))
raytracer.scene.append(Sphere(position=(0, -1, -6), radius=1, material=water))


raytracer.lights.append(AmbientLight(intensity=0.1))
raytracer.lights.append(DirectionalLight(direction=(-1, -1, -1), intensity=0.9))

raytracer.rtClear()
raytracer.rtRender()

print("\nRender Time:", pygame.time.get_ticks() / 1000, "secs")

isRunning = True
while isRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                isRunning = False

pygame.quit()
