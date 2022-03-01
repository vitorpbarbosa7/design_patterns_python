from abc import ABC, abstractmethod


# base class for notification, which deals with the message
class Notification(ABC):
    @abstractmethod
    def notify(self, message):
        pass

# any new kind of class will need to be created

class Email(Notification):
    # receives message by default
    def __init__(self, email):
        self.email = email

    def notify(self, message):
        print(f'Send "{message}" to {self.email}')

class SMS(Notification):
    def __init__(self, phone):
        self.phone = phone
        
    def notify(self, message):
        print(f'Send "{message}" to {self.phone}')

class NotificationManager:
    def __init__(self, notification):
        self.notification = notification

    def send(self, message):
        self.notification.notify(message)

class Contact:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

if __name__ == '__main__':
    contact = Contact('John Doe', 'john@test', '(408)-888-9999')

    sms_notification = SMS(contact.phone)
    email_notification = Email(contact.email)

    # receives notification, which can be any class which derives from Notification    
    # Instantiate Notification Manager
    notification_manager = NotificationManager(sms_notification)
    notification_manager.send('Hello John')

    # receives another kind of notification
    notification_manager.notification = email_notification
    notification_manager.send('Hi John')

    # can receive another class inside NotificationManager