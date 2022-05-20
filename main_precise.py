import sys
import pygame
from pygame.locals import QUIT
import json

with open('data.json', newline='') as jsonfile:
        data = json.load(jsonfile)

WIDTH = data["width"]
HEIGHT = data["height"]

def output_picture_txt():
    global WIDTH,HEIGHT,window_surface
    print("Saving Txt Data...")
    with open("picture.txt","w",encoding="utf-8") as f:
        f.write(str(WIDTH) + '\n')
        f.write(str(HEIGHT) + '\n')
        for i in range(HEIGHT):
            for j in range(WIDTH):
                if pygame.Surface.get_at(window_surface, (j, i)) == (0,0,0):
                    f.write("1")
                else:
                    f.write("0")
            f.write("\n")
    print("Data Saved !")

def output_picture_json():
    global jsDict
    print("Saving Json Data...")
    with open("picture.json","w",encoding="utf-8") as f:
        json.dump(jsDict, f)
    print("Data Saved !")
    return jsDict
jsDict = {"drawing":[]}

if __name__ == '__main__':
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

    # mouse_flag 測試滑鼠是否按住
    mouse_flag = False
    # 事件迴圈監聽事件，進行事件處理
    while True:
        # 偵測按鍵(按住)
        keys_still_pressed = pygame.key.get_pressed()
        # 迭代整個事件迴圈，若有符合事件則對應處理
        for event in pygame.event.get():
            # 當使用者結束視窗，程式也結束
            if event.type == QUIT:
                output_picture_txt()
                output_picture_json()
                pygame.quit()
                sys.exit()


            # 按下空白鍵時
            elif keys_still_pressed[pygame.K_SPACE]:
                
                # 因為while跑得比滑鼠慢，所以要將兩個構圖點之間連結起來防止誤差
                if mouse_flag:
                    try:
                        last_point = new_point
                        new_point = pygame.mouse.get_pos()
                        pygame.draw.line(window_surface , (0,0,0) , last_point, new_point)
                    except:
                        new_point = last_point = pygame.mouse.get_pos()
                    finally:
                        x1,x2=(new_point[0],last_point[0]) if (new_point[0]<last_point[0]) else (last_point[0],new_point[0])
                        y1,y2=(new_point[1],last_point[1]) if (new_point[1]<last_point[1]) else (last_point[1],new_point[1])
                        for i in range(x1,x2+1):
                            for j in range(y1,y2+1):
                                if pygame.Surface.get_at(window_surface,(i,j))==(0,0,0):
                                    jsDict["drawing"].append({"x":WIDTH - i , "y":HEIGHT - j})
                else:
                    new_point=pygame.mouse.get_pos()
                    x,y=new_point
                    jsDict["drawing"].append({"x":WIDTH - x , "y":HEIGHT - y})
                # 紀錄按下空白鍵的瞬間，滑鼠所在的點
                if mouse_flag == False:
                    first_click = pygame.mouse.get_pos()
                # 將滑鼠所在位置設成黑點
                window_surface.set_at(new_point, (0,0,0))
                pygame.display.update()
                # 已經按下空白鍵
                mouse_flag = True
            elif not keys_still_pressed[pygame.K_SPACE] and mouse_flag:
                mouse_flag=False
        
        
