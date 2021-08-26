def main():
    #escribe tu código abajo de esta línea
    #Índice de masa corporal

a=float(input("give me the weight in kilograms: "))
b=float(input("give me the height in meters: "))

if a==0 or b==0:
    print("check your data, something is wrong")

BMI=a/float(b**2)

if BMI<20:
    print("Low weight")
elif BMI>=20 and BMI<25:
    print("normal weight")
elif BMI>=25 and BMI<30:
    print("Overweight")
elif BMI>=30 and BMI<40:
    print("Obesity")
else:
    print("Morbid obesity")
    pass
if __name__=='__main__':
    main()
