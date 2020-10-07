#Se introduc de la tastatură trei cifre. Afişaţi pe aceeaşi linie 5 numere formate cu
#aceste cifre luate o singură dată.

n1=int(input("dați a="))
n2=int(input("dați b="))
n3=int(input("dați c="))
print(n1,n2,n3, sep="")
print(n1,n3,n2, sep="")
print(n2,n1,n3, sep="")
print(n2,n3,n1, sep="")
print(n3,n2,n1, sep="")
print(n3,n1,n2, sep="")