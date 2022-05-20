from math import pi,cos,sin,sqrt,atan2

def dft(x):
    X = []
    N = len(x)

    for k in range(N):
        com = complex(0)
        for n in range(N):
            phi = (2 * pi * k * n) / N
            com += x[n] * (cos(phi) - sin(phi)*1j)

        com /= N
        freq = k
        amp = sqrt( com.imag**2 + com.real**2)
        phase = atan2( com.imag , com.real )

        X.append( {"com":com , "freq":freq , "amp":amp , "phase":phase} )
        X=sorted(X,key=lambda x:x['amp'],reverse=True)
    return X