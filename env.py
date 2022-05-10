import math
import pygame


class buildEnvironment():
    def __init__(self, MapDimensions):
        pygame.init()
        self.pointcloud = []
        self.externalMap = pygame.image.load('maps/map1.png')
        self.mapH, self.mapW = MapDimensions
        self.MapWindowName = 'RRT Path Planning'
        pygame.display.set_caption(self.MapWindowName)
        self.map = pygame.display.set_mode((self.mapW, self.mapH))
        self.map.blit(self.externalMap, (0, 0))
        # Setting some colors for later use
        self.black = (0, 0, 0)
        self.red = (255, 0, 0)
        self.green = (0, 255, 0)
        self.blue = (0, 0, 255)
        self.grey = (70, 70, 70)
        self.white = (255, 255, 255)

    def conv_2_cartesian(self, distance, angle, robot_position):
        x = distance * math.cos(angle) + robot_position[0]
        y = -distance * math.sin(angle) + robot_position[1]
        return (int(x), int(y))

    def dataStorage(self, data):
        # print("Point Cloud Size: ", len(self.pointcloud))
        # print("Element in Data1: ", data[0])
        # if data == True:
        for element in data:
            # print("Element in Data3: ", element)
            cartesian_point = self.conv_2_cartesian(element[0], element[1], (element[2], element[3]))
            if cartesian_point not in self.pointcloud:
                # print("PointCloud: ", self.pointcloud)
                self.pointcloud.append(cartesian_point)

    def show_sensor_data(self):
        self.sensor_display_map = self.map.copy()
        for point in self.pointcloud:
            self.sensor_display_map.set_at((int(point[0]), int(point[1])), (255, 0, 0))

    # # Plot your own position in yellow
    # def show_self_pos(self, data):
    #     # self.sensor_display_map = self.map.copy()
    #     for element in data:
    #         self.sensor_display_map.set_at((int(element[2]), int(element[3])), (255, 255, 0))
