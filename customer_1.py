class customer:
    def __init__(self,custid,cname,mobno,prod,add):#u can add address..
        self.__custid=custid
        self.__cname=cname
        self.__mobno=mobno
        self.__prod=prod
        self.__add=add

    @property
    def custid(self):
        return self.__custid
    @property
    def cname(self):
        return self.__cname
    @property
    def mobno(self):
        return self.__mobno
    @property
    def prod(self):
        return self.__prod
    @property
    def add(self):
        return self.__add


    @custid.setter
    def custid(self,custid):
        self.__custid=custid
    @cname.setter
    def cname(self,cname):
        self.__cname=cname
    @mobno.setter
    def mobno(self,mobno):
        self.__mobno=mobno
    @prod.setter
    def prod(self,prod):
        self.__prod=prod
    @add.setter
    def add(self,add):
        self.__add=add
