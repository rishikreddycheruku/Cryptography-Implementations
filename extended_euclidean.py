import pandas as pd
def euclidean(a, b):
    if a < b:
        a, b = b, a
    ra = a
    rb = b
    al = []
    bl = []
    ql = []
    rl = []
    while rb != 0:
        al.append(ra)
        bl.append(rb)
        ql.append(ra // rb)
        rl.append(ra % rb)
        ra, rb = rb, ra%rb

    return ra, al, bl, ql, rl

def extendedeuclidean(a, b):
    gcd, al, bl, ql, rl = euclidean(a, b)
    ua = 1
    ub = 0
    va = 0
    vb = 1
    ula = []
    ulb = []
    ur = []
    vla = []
    vlb = []
    vr = []
    for i in range(len(ql)):
        ula.append(ua)
        ulb.append(ub)
        ur.append(ua - (ql[i]*ub))
        vla.append(va)
        vlb.append(vb)
        vr.append(va - (ql[i]*vb))
        ua, ub = ub, ur[-1]
        va, vb = vb, vr[-1]
    ula[-1] = ""
    ulb[-1] = ""
    ur[-1] = ""
    vla[-1] = ""
    vlb[-1] = ""
    vr[-1] = ""
    
    return [gcd, ql, al, bl, rl, ula, ulb, ur, vla, vlb, vr]

if __name__ == "__main__":
    a = int(input("Enter the value of A : "))
    b = int(input("Enter the value of B : "))
    ee = extendedeuclidean(a, b)
    gcd = ee[0]
    print("The GCD of", a, ",", b, "is", gcd)

    data = {
    "q" : ee[1],
    "r(n-1)" : ee[2],
    "r(n)" : ee[3],
    "r(n+1)" : ee[4]
    }

    eedata = {
    "q" : ee[1],
    "r(n-1)" : ee[2],
    "r(n)" : ee[3],
    "r(n+1)" : ee[4],
    "u(n-1)" : ee[5],
    "u(n)" : ee[6],
    "u(n+1)" : ee[7],
    "v(n-1)" : ee[8],
    "v(n)" : ee[9],
    "v(n+1)" : ee[10]
    }

    eetable = pd.DataFrame(eedata, index=range(1, len(data["q"]) + 1))
    print(eetable)
