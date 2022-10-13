from abc import ABC, abstractclassmethod


class Notifications(ABC):
    @abstractclassmethod
    def notify(self):
        pass


class UserNotifications(Notifications):
    def notify(self):
        print("Email Notified!")


class UserNotificationDecorator(Notifications):
    source = None

    def __init__(self, source):
        self.source = source

    def notify(self):
        self.source.notify()


class ExtraNotification(UserNotificationDecorator):
    def notify(self, notify):
        for i in notify:
            val = i.lower()
            if val == 'facebook':
                self.facebookNotify()
            if val == 'instagram':
                self.instagramNotify()
            if val == 'twitter':
                self.twitterNotify()

    def facebookNotify(self):
        print('Facebook Notified!')

    def instagramNotify(self):
        print('Instagram Notified!')

    def twitterNotify(self):
        print('Twitter Notified!')


# Simple User Notifications
userNotifications = UserNotifications()
userNotifications.notify()

# Extended User Notifications Using Decorators
extraNotification = ExtraNotification(userNotifications)
extraNotification.notify(['facebook'])
# extraNotification.notify(['facebook', 'instagram'])
# extraNotification.notify(['facebook', 'instagram', 'Twitter'])
