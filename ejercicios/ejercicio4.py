# Cree un programa que calcule el IMC (Indice de masa corporal). Formula --> IMC=Peso/Altura2 (Peso sobre altura al cuadrado)
# El usuario debera ingresar su peso y su altura (su nombre si quieren y despues imprimirlo concatenado) y el programa ademas de 
# calcular el IMC debera decir en que clasificacion se encuentra.
# La clasificacion la encontraran el archivo de imagen: IMC_clasificacion.jpg

peso = float(input("Ingrese su peso corporal en KG: "))
altura = float(input("Ingrese su altura en metros: "))

IMC = peso / (altura ** 2)
print(f"Tu IMC es de: {IMC}")

if IMC < 18.5:
    print("Tienes: Bajo peso")
elif IMC >= 18.5 and IMC <= 24.9:
    print("Tienes: Peso adecuado")
elif IMC >= 25.0 and IMC <= 29.9:
    print("Tienes: Sobrepeso")
elif IMC >= 30.0 and IMC <= 34.9:
    print("Tienes: Obesidad grado 1")
elif IMC >= 35.0 and IMC <= 39.9:
    print("Tienes: Obesidad grado 2")
else:
    print("Tienes: Obesidad grado 3")


