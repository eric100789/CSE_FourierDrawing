import json
from re import X
from cfourier import cft
from math import cos,sin,pi,e,sqrt,atan2
import pygame
import sys
from pygame.locals import QUIT
WIDTH = 800*1.5
HEIGHT = 600*1.5

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

# 更新畫面，等所有操作完成後一次更新（若沒更新，則元素不會出現）
with open('picture.json', newline='') as jsonfile:
        data = json.load(jsonfile)["drawing"]

LENGTH = len(data)
START = LENGTH//2
END = -LENGTH//2
START_X = 200
START_Y = HEIGHT/2 -200
UNIT_TIME = 2*pi
Has_Rendered = False

def making_circle(t):
    x=START_X
    y=START_Y
    for n in range(LENGTH):
        prevx = x
        prevy = y
        nData = cft(data,n,START,END)
        x += nData["r"]*cos(nData["f"]*t+nData["p"]) 
        y += nData["r"]*sin(nData["f"]*t+nData["p"]) 
        pygame.draw.circle(window_surface , (0,0,0) , (prevx,prevy) ,nData["r"],1)
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