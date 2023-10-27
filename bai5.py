#nhap vao cac phan tu trong list va dem so luong so chan co trong list
listN=[]
#ham dem 
def Dem(listN):
    count=0
    for x in listN:
        if x%2==0:
            count+=1
    return count
#ham nhap
def Nhap(n, listN):
    for i in range (0,n):
        so=int(input("Nhap so thu {0}:".format(i+1)))
        listN.append(so)
Nhap(3,listN)
print(Dem(listN))
    

