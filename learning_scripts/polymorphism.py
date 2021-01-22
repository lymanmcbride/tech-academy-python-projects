class Client: #Parent Class
    def __init__(self, name, email):  #properties that all clients will have
        self.name = name
        self.email = email

    def make_purchase(self):
        print("Thank you for your purchase {}!".format(self.name)) #method for making a purchase
    
    def get_info(self):
        print("Name: {} \nEmail: {}".format(self.name, self.email))  #get info polymorphs in all of them because it will need to display any extra info.

class Company(Client):  #child class, company as sub class of client
    def __init__(self, name, email, rep_number, rep_name):
        super().__init__(name, email)   #invoking the properties of the parent class, because if you re-state __init__ it overrides the parent class
        self.rep_number = rep_number
        self.rep_name = rep_name

    
    def get_info(self):
        print("Name: {} \nEmail: {}\n Representative Number: {}".format(self.name, self.email, self.rep_number)) #polymorphed get_info method

class Individual(Client): #child class
    def __init__(self, name, email, recent_purchases, username, password):
        super().__init__(name, email)
        self.recent_purchases = recent_purchases  #could be used to give new offers since they bought something recently to incentivize more buying
        self.username = username
        self.password = password
    def make_purchase(self):
        self.recent_purchases = True  #polymorph of parent class method
        print("Thank you for your purchase {}!".format(self.name))
    def get_info(self):
        print("Name: {} \nEmail: {}\n Has made a recent purchase? {}".format(self.name, self.email, self.recent_purchases))  #polymorph of parent class method



jason = Individual("Jason Mraz", "jmz@singer.com", False, "jmz", "I L0ve mu$ic")
exon = Company("Exon Mobile", "em@emobile.com", "719-650-4565", "Jeff Flake")
jason.get_info()
jason.make_purchase()
jason.get_info()
exon.get_info()
exon.make_purchase()