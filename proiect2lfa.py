def recursiv(stare,cuvant,final,dict,lmax):
    global listacuv,staretrecuta
    if cuvant not in listacuv and len(cuvant)<=lmax and stare in final:
            listacuv.append(cuvant)
            print("SCRIS",stare,cuvant)

    if len(cuvant)>lmax:
        return None
    copie=cuvant


    for tuplu in dict[stare]:
        #copie = cuvant
        if tuplu[0]!="-":
            cuvant=copie+tuplu[0]

        print(cuvant)
        print(tuplu[1])
        recursiv(tuplu[1],cuvant,final,dict,lmax)

def generare(fisier,final,initial,lmax):
    dict={}
    f=open(fisier)
    L=f.readlines()
    for linie in L: #construirea dictionarului
        sursa,simbol,destinatie=linie.strip().split()

        if sursa in dict.keys():
            dict[sursa].append((simbol,destinatie))
        else:
            dict[sursa]=[(simbol,destinatie)]

    print(dict)
    recursiv(initial,"",final,dict,lmax)
    listacuv.sort()
    print(listacuv)

listacuv=[]
staretrecuta=""

#inpuf
final=["q0","q2"]
initial="q0"
fisier="exempluGen"

print(generare(fisier,final,initial,2))
print("Numarul de cuvinte acceptate este ",len(listacuv))