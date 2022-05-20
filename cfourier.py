from math import pi, e, sqrt, atan2
from json import load

with open('data.json', newline='') as jsonfile:
        data = load(jsonfile)

WIDTH = data["width"]
HEIGHT = data["height"]
REVERSE = bool(data["reverse"])

def cft(data,start,end):
    dataLength = len(data)
    dt = 1/dataLength
    dataList=[]
    
    for n in range(end,start+1):
        c = complex(0)
        for i in range(dataLength):
            x = WIDTH//2 - (data[i]["x"] - WIDTH//2)
            if(REVERSE):
                y = data[i]["y"]
            else:
                y = HEIGHT//2 - (data[i]["y"] - HEIGHT//2)
            ft = x + y*1j
            t = i/dataLength
            c += dt*ft*e**( (-n)*2*pi*t*1j ) 
        radius=sqrt((c.real**2+c.imag**2))
        freq=n+end
        phase=atan2(c.imag,c.real)
        dataList.append({"c":c , "f":freq , "p":phase , "r": radius})
    return dataList