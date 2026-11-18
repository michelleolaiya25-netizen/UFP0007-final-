class Ticket:
    def __init__(self,name,base_price):
        self.__name = name
        self.base_price =vbase_price

    def get_name(self):
        return self.__name
    
    def price(self):
        return self.base_price 


class StudentTicket(Ticket):
    def price(self):
        return super().price()*0.5
