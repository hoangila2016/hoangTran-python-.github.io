## xay dung ham uoc so chung lon nhat giua 2 so tu nhien a va b
def UocSoChungLonNhat(a,b):
    while(a!=b):
        if (a>b):
            a=a-b
        if(b>a):
            b=b-a
    return a
print(UocSoChungLonNhat(35,77))
    