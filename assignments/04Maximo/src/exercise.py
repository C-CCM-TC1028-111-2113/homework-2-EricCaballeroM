def main():
    #escribe tu código abajo de esta línea
    #El mayor de 3 números

a=int(input("give me the first number: "))
b=int(input("give me the second number: "))
c=int(input("give me the third number: "))

if a>b:
    if a>c:
        print(a)
    else:
        print (c)
elif b>c:
    print(b)
else:
    print(c)

    pass


if __name__=='__main__':
    main()
