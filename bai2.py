tu_Dien={"if":"neu"}
tu_Tra_Cuu=""
tieng_Viet=""
tieng_Anh=""
tu_Cap_Nhat=""
cap_Nhat=""
tu_Xoa=""
print("1.Them tu vung\n2.tra cu\n3.cap nhat\n4.xoa tu vung\n5.xoa toan bo\n6.ket thuc")
while True:
    lua_chon=int(input("Nhap lua chon: "))
    if lua_chon==1:
        ##them
        tieng_Anh=input("Nhap tieng anh: ")
        if tieng_Anh in tu_Dien:
            print("Tu nay da co trong tu dien!")
        else:
            tieng_Viet=input("Nhap tieng viet: ")
            tu_Dien[tieng_Anh]=tieng_Viet
            print(tu_Dien)
    if lua_chon==2:
        ##tra cuu
        tu_Tra_Cuu=input("Nhap tu ban muon tra cuu: ")
        if tu_Tra_Cuu in tu_Dien:
            print ("nghia cua \"{0}\" la: \"{1}\"".format(tu_Tra_Cuu,tu_Dien[tu_Tra_Cuu]))
        else:
            print("Tu nay khong co trong tu dien cua chung toi!")
    if lua_chon==3:
        ##Cap nhat y nghia tu vung 
        tu_Cap_Nhat=input("Nhap tu can cap nhat: ")
        if tu_Cap_Nhat in tu_Dien:
            cap_Nhat=input("Nghia ma ban muon cap nhat: ")
            tu_Dien[tu_Cap_Nhat]=cap_Nhat
            print(tu_Dien)
        else:
            print("Tu nay khong co trong tu dien cua chung toi!")  
    if lua_chon==4:
        ##xoa tu vung
        tu_Xoa=input("Nhap tu ban muon xoa: ")
        if tu_Xoa in tu_Dien:
            del tu_Dien[tu_Xoa]
            print(tu_Dien)
    if lua_chon==5:
        ##xoa toan bo tu vung
        tu_Dien.clear()
        print(tu_Dien)
    if lua_chon==6:
        ##ket thuc 
        break





