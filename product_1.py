class product:
    def __init__(self,id,name,price,qty):
        self.__id=id
        self.__name=name
        self.__price=price
        self.__qty=qty

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price

    @property
    def qty(self):
        return self.__qty

    @id.setter
    def  id(self, id):
        self.__id=id

    @name.setter
    def name(self,name):
        self.__name=name

    @price.setter
    def price(self,price):
        self.__price=price

    @qty.setter
    def qty(self,qty):
        self.__qty=qty