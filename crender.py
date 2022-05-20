import json
from cfourier import cft
from math import cos,sin,pi
import pygame
import sys
from pygame.locals import QUIT

with open('data.json', newline='') as jsonfile:
        data = json.load(jsonfile)

with open('picture.json', newline='') as jsonfile:
        picture_data = json.load(jsonfile)["drawing"]

WIDTH = data["width"]*1.5
HEIGHT = data["height"]*1.5
LENGTH = len(picture_data)
START = LENGTH//2
END = -LENGTH//2
START_X = data["x"]
START_Y = data["y"]
UNIT_TIME = 2*pi
ROTATE = data["rotate"] 
CALCULATED_LIST = sorted(cft(picture_data,START,END) , key=lambda x:x['r'],reverse=True)
SIZE = data["size"] 
Has_Rendered = False

# 初始化
pygame.init()
# 建立視窗畫布
window_surface = pygame.display.set_mode((WIDTH, HEIGHT))
# 設置視窗標題為 Flourier Painting
pygame.display.set_caption('Flourier Painting')
# 清除畫面並填滿背景色
window_surface.fill((255, 255, 255))

# 宣告 font 文字物件
head_font = pygame.font.SysFont(None, 60)
# 渲染方法會回傳 surface 物件
text_surface = head_font.render('Flourier Painting', True, (1, 0, 0))
# blit 用來把其他元素渲染到另外一個 surface 上，這邊是 window 視窗
window_surface.blit(text_surface, (10, 10))

def making_circle(t):
    x=START_X
    y=START_Y
    for n in range(LENGTH):
        prevx = x
        prevy = y
        x += SIZE*CALCULATED_LIST[n]["r"]*cos(CALCULATED_LIST[n]["f"]*t+CALCULATED_LIST[n]["p"] + (ROTATE*pi/180) ) 
        y += SIZE*CALCULATED_LIST[n]["r"]*sin(CALCULATED_LIST[n]["f"]*t+CALCULATED_LIST[n]["p"] + (ROTATE*pi/180) ) 
        pygame.draw.circle(window_surface , (0,0,0) , (prevx,prevy) ,CALCULATED_LIST[n]["r"],1)
        pygame.draw.aaline(window_surface , (0,0,0) , (prevx,prevy) , (x,y))
    return (x,y)

while True:
    for event in pygame.event.get():
        # 當使用者結束視窗，程式也結束
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif not Has_Rendered:
            t=0
            coord=[]
            while t <= UNIT_TIME:
                coord.append( making_circle(t) )
                for i in coord:
                    pygame.draw.circle(window_surface,(255,0,0),i,2)
                pygame.display.update()
                window_surface.fill((255, 255, 255))
                t += 2*UNIT_TIME/LENGTH
            print("Had rendered")
            Has_Rendered=True