# ref doc - https://refactoring.guru/design-patterns/factory-method
# ref video - https://www.youtube.com/watch?v=4McdC4EtXKw


from abc import ABC, abstractmethod

class Notification(ABC):
    @abstractmethod
    def send(self, message: str):
        pass
    
class EmailNotification(Notification):
    def send(self, message: str):
        print(f"Sending Email: {message}")
        
class SMSNotification(Notification):
    def send(self, message: str):
        print(f"Sending SMS: {message}")
    
class PushNotification(Notification):
    def send(self, message: str):
        print(f"Sending push notification: {message}")
        
class SlackNotification(Notification):
    def send(self, message: str):
        print(f"Sending Slack message: {message}")
            
class NotificationFactory:
    def create_nofication(self, notification_type: str) -> Notification:
        if notification_type == "email":
            return EmailNotification()
        elif notification_type == "sms":
            return SMSNotification() 
        elif notification_type == "push":
            return PushNotification()
        elif notification_type == "slack":
            return SlackNotification()    
        else:
            raise ValueError(f"Unknown notification type: {notification_type}")
        
# Client Code Using the Factory
def send_notification(notification_type: str, message: str):
    factory = NotificationFactory()
    notification = factory.create_nofication(notification_type)
    notification.send(message)
    
# Example usage
send_notification("email", "Hello via Email!")
send_notification("sms", "Hello via SMS!")
send_notification("push", "Hello via Push Notification!")
send_notification("slack", "Hello via Slack!")
