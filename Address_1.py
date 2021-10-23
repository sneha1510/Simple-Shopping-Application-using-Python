class address:
    def __init__(self,ct,st,pin):
        self.__ct=ct
        self.__st=st
        self.__pin=pin

    @property
    def ct(self):
        return self.__ct
    @property
    def st(self):
        return self.__st
    @property
    def pin(self):
        return self.__pin

    @ct.setter
    def ct(self,ct):
        self.__ct=ct

    @st.setter
    def st(self,st):
        self.__st=st

    @pin.setter
    def pin(self,pin):
        self.__pin=pin