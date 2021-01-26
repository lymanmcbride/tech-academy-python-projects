class using_private: 
    def __init__(self):
        self._firstName = 'Lyman' #Protected variable
        self.__lastName = 'McBride' #private variable

    def getLastname(self):
        print(self.__lastName) #accessing the private variable via method
    
    def changeLname(self, change):
        self.__lastName = change #changing the private variable using a method

me = using_private() 
me.getLastname()
me.changeLname('Sandholtz') #using the method to change the last name
print(me._firstName) #accessing the protected variable
me._firstName = 'Lemon' #changing the protected variable
print(me._firstName)
me.getLastname()