import json
from fourier import dft
from math import cos,sin,pi
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
pygame.display.update()
with open('picture.json', newline='') as jsonfile:
    data = json.load(jsonfile)
xy=data['drawing']
xlist=[]
ylist=[]
for i in xy:
    xlist.append(i["x"])
    ylist.append(i["y"])


X=dft(xlist)
Y=dft(ylist)
coord=[]
t=0
Has_Rendered=False
while True:
    for event in pygame.event.get():
        # 當使用者結束視窗，程式也結束
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif not Has_Rendered:
            while t<=2*pi:
                x=1100
                y=HEIGHT/2 +100
                for i in range(len(Y)):
                    prevx=x
                    prevy=y
                    radius=Y[i]['amp']
                    freq=Y[i]['freq']
                    phase=Y[i]['phase']
                    x+=radius*cos(freq*t+phase+3*pi/2)
                    y+=radius*sin(freq*t+phase+3*pi/2)
                    pygame.draw.circle(window_surface , (0,0,0) , (prevx,prevy) ,radius,1)
                    pygame.draw.aaline(window_surface , (0,0,0) , (prevx,prevy) , (x,y))
                pygame.draw.line(window_surface,(0,0,0),(x,y),(0,y))
                finaly=y
                x=WIDTH/2+100
                y=800
                for i in range(len(X)):
                    prevx=x
                    prevy=y
                    radius=X[i]['amp']
                    freq=X[i]['freq']
                    phase=X[i]['phase']
                    x+=radius*cos(freq*t+phase+pi)
                    y+=radius*sin(freq*t+phase+pi)
                    pygame.draw.circle(window_surface , (0,0,0) , (prevx,prevy) ,radius,1)
                    pygame.draw.aaline(window_surface , (0,0,0) , (prevx,prevy) , (x,y))
                pygame.draw.line(window_surface,(0,0,0),(x,y),(x,0))
                finalx=x
                coord.append([finalx,finaly])
                for i in range(len(coord)-1):
                    pygame.draw.line(window_surface,(255,0,0),coord[i],coord[i+1],width=2)
                pygame.display.update()
                window_surface.fill((255, 255, 255))
                t+=2*pi/len(Y)
            print("Had rendered")
            Has_Rendered=True