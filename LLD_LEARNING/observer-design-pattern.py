from abc import ABC, abstractmethod
# it consists of two main interfaces observable interface and observer interface
class Observable(ABC):
    def __init__(self) -> None:
        self.observer_list = []

    @abstractmethod
    def add():
        pass

    @abstractmethod
    def remove():
        pass

    @abstractmethod
    def notify():
        pass
class Observer(ABC):

    @abstractmethod
    def update():
        pass

# Let us implement the notify me action from ecommerce apps

class ProductNotifyMe(Observable):
    def add(self,obj):
        self.observer_list.append(obj)
    
    def remove(self,obj):
        self.observer_list.remove(obj)
    
    def notify(self,msg):
        for i in self.observer_list:
            i.update(msg)

class User1(Observer):
    def update(self,msg):
        print('USER1 RECIEVED THE MESSAGE:'+str(msg))
    
class User2(Observer):
    def update(self,msg):
        print('USER2 RECIEVED THE MESSAGE:'+str(msg))

class User3(Observer):
    def update(self,msg):
        print('USER2 RECIEVED THE MESSAGE:'+str(msg))

class Main:
    def __init__(self) -> None:
        self.product_observable = ProductNotifyMe()
        self.user1 =User1()
        self.user2 = User2()
        self.user3 = User3()
        self.main()
    
    def main(self):
        # user1 presses notify me 
        self.product_observable.add(self.user1)
        # we notify the user that he has been added 
        self.product_observable.notify('Product is unavailbale')
        # user2 presses notify me
        self.product_observable.add(self.user2)
        # we notify both the users that the product might be available tomorrow
        self.product_observable.notify('Product might be available tomorrow')
        # user2 is not intreseted anymore
        self.product_observable.remove(self.user2)
        # user3 presses notify me
        self.product_observable.add(self.user3)
        # notify users that it is availble
        self.product_observable.notify('Product is available.')
Main()


