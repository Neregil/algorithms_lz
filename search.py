from random import randint as ri

lp=0
bp=0
st=[]
for i in range(0,100):
    st.append(ri(0,1000000))
ss=sorted(st)
print(ss)
el=int(input("Введите заданный элемент: "))
print()
for i in range(len(ss)):
    lp+=1
    if ss[i]==el:
        break

ft=0
lt=len(ss)-1
j=-1
while (ft<=lt) and (j==-1):
    m=(ft+lt)//2
    bp+=1
    if ss[m]==el:
        j=m
    else:
        bp+=1
        if el<ss[m]:
            lt=m-1
        else:
            ft=m+1
if(ss[i]==el):
    print(f"Его индекс: {i}")
    print(f"Количество сравнений, сделанных во время линейного поиска: {lp}, бинарного: {bp}")
else:print("Элемент не найден ни в одном из методов")