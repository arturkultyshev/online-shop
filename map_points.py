import sys

import pygame
import requests


z = 12


def function():
    global z
    map_request = f"https://static-maps.yandex.ru/1.x/?ll=76.947820%2C43.260194&z={z}&l=map&pt=76.927956%2C43.263120," \
                  f"pmgrs~76.961451%2C43.250682,flag~76.901359%2C43.252172,pm2rdm~76.947743%2C43.270884," \
                  f"pmors~76.964053%2C43.260835,pm2ywl99~76.909225%2C43.225787"
    response = requests.get(map_request)
    if not response:
        print("Ошибка выполнения запроса:")
        print(map_request)
        print("Http статус:", response.status_code, "(", response.reason, ")")
        sys.exit(1)

    map_file = "map.png"
    with open(map_file, "wb") as file:
        file.write(response.content)
    return map_file


f = function()
pygame.init()
screen = pygame.display.set_mode((600, 450))
screen.blit(pygame.image.load(function()), (0, 0))
pygame.display.flip()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if z != 17:
                    z += 1
            if event.key == pygame.K_DOWN:
                if z != 2:
                    z -= 1
            screen.blit(pygame.image.load(function()), (0, 0))
    pygame.display.flip()
    pygame.display.update()



