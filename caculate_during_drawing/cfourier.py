from math import cos, sin , pi, e, sqrt, atan2

def cft(data,n,start,end):
    dataLength = len(data)
    dt = 1/dataLength
    
    c = complex(0)
    for i in range(dataLength):
        x = data[i]["x"]
        y = data[i]["y"]
        ft = x + y*1j
        t = i/dataLength
        c += dt*ft*e**( (-n)*2*pi*t*1j ) 
    
    radius=sqrt((c.real**2+c.imag**2))
    freq=n+end
    phase=atan2(c.imag,c.real)

    return {"c":c , "f":freq , "p":phase , "r": radius}


