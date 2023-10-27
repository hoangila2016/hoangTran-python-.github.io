##tinh tong cac day so n 
##ham nhap vao so luong n so muon nhap va cac so
def NhapLieu(n,listN):
    for i in range(1,n+1):
        print("nhap so thu {0}".format(i))
        so=int(input(""))
        listN.append(so)
    print(listN)
##ham tinh tong cac so n
def Tong(listN):
    so_Tong=0
    for i in range(len(listN)):
        so_Tong+=listN[i]
    return so_Tong

listN=[]
NhapLieu(3,listN)
print( Tong(listN))