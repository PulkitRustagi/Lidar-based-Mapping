import env
import sensors
import pygame
import math

# Building the map by specifying (width,height)
# that get fed into the __init__() inside env.py
environment = env.buildEnvironment((600, 1200))

# keep a copy of the original map
environment.originalMap = environment.map.copy()

# initialize a LIDAR using LaserSensor class in sensor.py
# the feeds parameters in __init__() of LaserSensor class
laser = sensors.LaserSensor(200, environment.originalMap, uncertainty=(0.5, 0.5))

# fill the map with black since it's an initially unknown room
environment.map.fill((0, 0, 0))
# we will be displaying the Lidar discovered points on this black map
environment.sensor_display_map = environment.map.copy()

running = True

while running:
    sensorON = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if pygame.mouse.get_focused():
            sensorON = True
        elif not pygame.mouse.get_focused():
            sensorON = False
    if sensorON:
        position = pygame.mouse.get_pos()
        laser.position = position
        # print("Laser Position:", position)
        sensor_data = laser.sense_obstacle()
        environment.dataStorage(sensor_data)
        environment.show_sensor_data()
        # environment.show_self_pos(sensor_data)
    environment.map.blit(environment.sensor_display_map, (0, 0))
    pygame.display.update()
