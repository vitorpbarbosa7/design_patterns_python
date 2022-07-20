from abc import ABC, abstractmethod 

# base class with function which will be called many times
class Notification(ABC):
    @abstractmethod
    def notify(self, message, email):
        pass

class Email(Notification):
    # same inputs as before
    def notify(self, message, email):
        print(f'Send {message} to {email}')

class SMS(Notification):
    # bad implementation because phone is another input
    def notify(self, message, phone):
        print(f'Send {message} to {phone}')

if __name__ == '__main__':
    notification = SMS()
    notification.notify('Hello','john@test.com')
