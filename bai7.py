##test OOP python
##Excercise: Creating a Ngay Class have atributes: ngay, thang, nam. 
##Method: Figuring total day from Ngay object in a year, total day in a month 
class Ngay:
    ##constructor
    def __init__(self,ngay,thang,nam):
        self.ngay,self.thang,self.nam=ngay,thang,nam
        self.soNgayTrongThang=[0,31,28,31,30,31,30,31,31,30,31,30,31]
    ##printme
    def printMe(self):
        print("Ngay: {0}/{1}/{2}".format(self.ngay,self.thang,self.nam))
    ## count day in one year
    def NgayTrongNam(self):
        ngayTrongNam=0
        if(self.nam%400==0 or (self.nam%4==0 and self.nam%100!=0)):
            self.soNgayTrongThang[2]=29
        for i in range (0,self.thang):
            ngayTrongNam+=self.soNgayTrongThang[i]
        return ngayTrongNam+self.ngay
    ## static method show total days in a month
    @staticmethod
    def NgayTrongThang(thang): 
        danhSachNgayTrongThang=[0,31,28,31,30,31,30,31,31,30,31,30,31]
        if (thang%400==0 or (thang%4==0 and thang%100!=0)):
            danhSachNgayTrongThang[2]=29
        return danhSachNgayTrongThang[thang]

## bat dau su dung class
## khoi tao class
ngayThangNam=Ngay(1,3,2003)
ngayThangNam.printMe()
print(ngayThangNam.NgayTrongNam())

