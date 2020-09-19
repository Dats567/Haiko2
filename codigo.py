numeros=[]
numP=[]
numI=[]
total=0
resta=0
cantidad=int(input("Digite la cantidad de numeros que quiere almacenar: "))

for i in range(cantidad):
    numeros.append(int(input("ingrese los numeros que quiera almacenar: ")))

op=int(input("Que quiere hacer con estos numeros:\nEscriba 1 si quiere sumarlos\nEscriba 2 si quiere sumar las posiciones pares del arreglo\nEscriba 3 si quiere sumar las posiciones impares del arreglo\nEscriba 4 si quiere sumar elinial y el final\nEscriba 5 si quiere imprimir solo los numeros pares\nEscriba 6 si quiere imprimir los numeros impares\nEscriba 7 si quiere restar los numeros del arreglo\nEscriba 8 si quiere Separar los numeros pares e impares\nEscriba 9 si quiere potenciar el primero numero con el ultimo\nEscriba su respuesta: "))

if op==1:
     for i in numeros:
          total=total+i
     print("La suma de los numeros del arreglo es: ",total)
if op==2:
     for i in range(0,len(numeros),2):
          total=total+numeros[i]
     print("La suma de las posiciones pares del arreglo es :",total)
if op==3:
     for i in range(1,len(numeros),2):
          total=total+numeros[i]
     print("La suma de las posiciones impares del arreglo es: ",total)
if op==4:
     tam=int(len(numeros)/2)
     for i in range(tam):
          numI.append(numeros[i]+numeros[-1-i])
     print("La suma de las posiciones iniciales y finales del arreglo es: ",numI)
if op==5:
     for i in range(len(numeros)):
          if(numeros[i] % 2 == 0):
               numP.append(numeros[i])
     print("Los numeros pares del arreglo son: ",numP)
if op==6:
     for i in range(len(numeros)):
          if (numeros[i] %2>0):
               numI.append(numeros[i])
     print("Los numeros impares del arreglo son: ",numI)
if op==7:
     for i in range (1,len(numeros)):
          total=total+numeros[i]
     print("La resta de los numeros del arreglo es: ",numeros[0]-total)
if op==8:
     for i in range(len(numeros)):
          if (numeros[i] % 2 == 0):
               numP.append(numeros[i])
          else:
               numI.append(numeros[i])
     print(numeros)
     print("Los numeros ",numP,"son pares")
     print("Los numeros ",numI,"son impares")
if op==9:
     tam=int(len(numeros)/2)
     for i in range(tam):
          numP.append(numeros[i]**numeros[-1-i])
          numP.append(numeros[-1-i]**numeros[i])
     print("La suma de las posiciones iniciales y finales del arreglo es: ",numP)
if op<1:
     print("No ha elegido nungina opcio :(\nIntentelo nuevamente")
if op>9:
     print("No ha elegido nungina opcio :(\nIntentelo nuevamente")
