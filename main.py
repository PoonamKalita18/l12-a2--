class Computer:
    def __init__(self):
        self.__maxprice = 900
    def sell(self):
        print('selling price is : {}'.format(self.__maxprice))
    def setMaxPrice(self,Price):
        self.__maxprice = Price
c = Computer()
c.sell()
c.__maxprice = 1000
c.sell()
c.setMaxPrice(1000)
c.sell()
