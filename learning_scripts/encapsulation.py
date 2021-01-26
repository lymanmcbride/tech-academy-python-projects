class using_private:
    def __init__(self):
        self._firstName = 'Lyman'
        self.__lastName = 'McBride'

    def getLastname(self):
        print(self.__lastName)
    
    def changeLname(self, change):
        self.__lastName = change

me = using_private()
me.getLastname()
me.changeLname('Sandholtz')
print(me._firstName)
me._firstName = 'Lemon'
print(me._firstName)
print(me.getLastname())