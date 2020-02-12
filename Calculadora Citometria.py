#Code para calculos de citometría 
import sys
print("BIENVENIDO A LA CALCULADORA DE CITOMETRÍA\nComencemos:")
#Anticuerpos
print ("1.Preguntas sobre los Anticuerpos que vas a utilizar:\n(Al finalizar de enumerar los anticuerpos escribe 'ok')")
Lista_de_anticuerpos=[]
while True :
    num = input("Que anticuerpos vas a usar?(Escribe nombre-color): ")
    if num == "ok":
        if len(Lista_de_anticuerpos) == 0:
            print("No has declarado Anticuerpos.\nIntentalo de nuevo")
            continue
        else:
            break
    elif num == "quit":
        sys.exit(0) # salir del programa durante bug
    else: 
        Lista_de_anticuerpos.append(num)
        n=0
        n=n+1
        continue

#print (Lista_de_anticuerpos)
numdab=len(Lista_de_anticuerpos)
print("Has declarado que vas a usar",numdab, "anticuerpos.")

#Declaracion de Muestras

print ("\n2.Preguntas sobre las muestras: ")

datos=[]
while True:
    muestras=input('num de muestras problema (no considerar los controles negativo o simple positivos):')
    try: 
        m=float(muestras)
        datos.append(m)
        break
    except:
        type(muestras) == str
        print("Error, por favor ingrese el número de muestras")
        continue
   

while True:
    vol=input('vol de Mix por muestra (ul):')
    try:
        v=float(vol)
        datos.append(v)
        voltot=datos[0]*datos[1]
        print("El Volumen total de la mix será de: ", voltot, "ul.")
        break
    except:
        type(vol) == str
        print("Error, por favor ingrese el volumen con números")
        continue   

#voltot=datos[0]*datos[1]
#print("El Volumen total de la mix será de: ", voltot, "ul.")

#dilucion de Ab

print ("\n3.Preguntas sobre las diluciones de los anticuerpos: ")
dil=[]
n = 0
while n<len(Lista_de_anticuerpos) :
    print(str(n+1)+"."+Lista_de_anticuerpos[n])
    dilsug=input("Ingresa la dilución sugerida del Ab expresada como n/100:")
    try:
        ds=float(dilsug)
        dil.append(ds)
        n = n + 1
    except:
        type(dilsug) == str
        print("Error, por favor ingrese la dilución sugerida con números")
        continue
   
#print (dil)
#print(Lista_de_anticuerpos, datos,dil)

#Calculos de cuanto debo usar de cada anticuerpo
h = 0
dul=[]
while h<len(Lista_de_anticuerpos):
    ul=voltot*dil[h]/100  
    dul.append(ul)
    h= h + 1


print("\nFinalmente, para realizar la Mix de anticuerpos para tu tinción debes:")
y=0
tot = 0
while y<len(dul):
        print("Tomar",dul[y],"ul del anticuerpo",Lista_de_anticuerpos[y])
        tot = tot + dul[y]
        y = y + 1

sb=voltot-tot
print ("en un volumen de ",sb,"ul de Staining Buffer. (volumen final ",voltot, "ul).")

#Calculos de los Simple positivos

while True:
    sp=len(Lista_de_anticuerpos) 
    if sp == 1:
        print("\nNo es necesario hacer control simple positivo ya que solo tiene un Anticuerpo.")
        break
    elif sp > 1:
        print("\nNo se olvide que debe hacer", sp, "controles simple positivo. Uno por cada anticuerpo que decidió usar:")
        y=0
        lulsp=[]
        while y<len(Lista_de_anticuerpos):
            ulsp=datos[1]*dil[y]/100
            lulsp.append(ulsp)
            vfsp=datos[1]-lulsp[y]  
            print("Para el simple positivo de",Lista_de_anticuerpos[y],", Ud. debe tomar", lulsp[y], "ul."  )
            print ("en un volumen de",vfsp,"ul de Staining Buffer. (volumen final ",datos[1], "ul).")
            y = y + 1
        break

print("\nRecuerde que necesitás al menos 1 tubo control negativo.")
print ("¡Mucha suerte en su Citometría!")






