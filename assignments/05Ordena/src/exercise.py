def main():
    # Escribe el código adecuado para completar el programa
    #Ordena 3 números

a=int(input("give me the first number: "))
b=int(input("give me the second number: "))
c=int(input("give me the third number: "))

if a<b and b<c:
    print(c)
    print(b)
    print(a)
elif b<a and a<c:
    print(c)
    print(a)
    print(b)
elif c<b and b<a:
    print(a)
    print(b)
    print(c)
elif b<c and c<a:
    print(a)
    print(c)
    print(b)
elif a<c and c<b:
    print(b)
    print(c)
    print(a)
elif c<a and a<b:
    print(b)
    print(a)
    print(c)
    pass


if __name__=='__main__':
    main()
