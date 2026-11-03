from random import randint as ri

srb=0
srv=0
st=[]
for i in range(0,100):
    st.append(ri(0,1000000))
print(st)
print()

sotb=st.copy()
g=1
while g==1:
    g=0
    for i in range(0,len(sotb)-1):
        if sotb[i]<sotb[i+1]:
            s=sotb[i]
            sotb[i]=sotb[i+1]
            sotb[i+1]=s
            g=True
            print(sotb)
            print()
            print()
            srb+=1

print(sotb)
print("Конец пузырька")
ul = st.copy()
sotv = []

while len(ul)>0:
    min=ul[0]
    for i in range(0,len(ul)):
        if ul[i]>min:
            min=ul[i]
        srv+=1
    sotv.append(min)
    ul.remove(min)
    print(ul)
    print()
    print(sotv)
    print()
    print()

print(sotv)
print("Конец выборки")
print(f"Кол-во сравнений сортировкой пузырька: {srb} Сортировкой выборки: {srv}")