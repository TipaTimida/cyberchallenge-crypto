import math

# calcola i coefficienti di bezout ax + by = mcd(a,b)
# restituisce una tupla (x, y ,mcd(a,b))
def bezout(a,b):
    x = [1,0]
    y = [0,1]
    i = 2
    while (b != 0):
        q = a//b
        x.append(x[i-2] - q * x[i-1])
        y.append(y[i-2] - q * y[i-1])
        a,b = b,a%b
        i += 1
    return (x[-2], y[-2], a)    
        
# calcola l'inverso modulo n utilizzando la funzione bezout()        
def inverse(a, n):
    if math.gcd(a, n) != 1:
        raise Exception(f"L'inverso di {a} mod {n} non esiste!")
    else:
        return bezout(a, n)[0] 
            
# risolve il sistema di congruenze x ≡ a[i] (mod n[i])
# utilizzando il teorema cinese del resto            
def cinese(a, n):
    if (len(a) != len(n)):
        raise Exception(f"Le due list {a} e {n} non hanno la stessa dimensione")
    x = 0
    N = math.prod(n)
    for i in range(0,len(n)):
        Ni = N//n[i]
        x += (a[i]*Ni*inverse(Ni, n[i])) % N
    return x % N