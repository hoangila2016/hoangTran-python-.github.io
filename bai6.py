#test lamda
Tinh_Tong= lambda a,b: a+b
print(Tinh_Tong(6,7))
def HamMu(n):
    return lambda x: x**n
HamMu2 = HamMu(2)
#HamMu2= lambda x: x**2
HamMu3 = HamMu(3)
#HamMu2= lambda x: x**3
print(HamMu2(3))
print(HamMu3(6))
