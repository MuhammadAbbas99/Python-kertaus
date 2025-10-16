#17.09.2025 Vero laskuri

#Verotettava tulo € 
#veroprosentti( %) 
# 10000             0% 
# 10000 - 20000     10%  
# > 20000           20% 

def värö(t):
    ver = 0
    if  0 < t <= 10000:
        ver = 0*t
        return ver
    if  10000 < t <= 20000:
        ver = 0.1 * ( t - 10000)
        return ver
    if  20000 < t:
        ver_1 = 0.1 * 10000
        ver_2 = 0.2 * ( t - 20000)
        ver = ver_1 + ver_2
        return ver
    else:
        return 0

a = int(input('Olka hyvä ja laitakaa vuosi tuolt: '))
vero = värö(a)
print(vero)