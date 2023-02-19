from __future__ import annotations
from abc import ABC, abstractmethod


class Notifier(ABC):

    @abstractmethod
    def notify(self, notification: str):
        """Notify about notification."""
        return notification


class EmailNotifier(Notifier):

    def notify(self, notification: str):
        """Notify on Email about notification."""
        return f"Email: {notification}"


class SMSNotifier(Notifier):

    def notify(self, notification: str):
        """Notify on SMS about notification."""
        return f"SMS: {notification}"


class FacebookNotifier(Notifier):

    def notify(self, notification: str):
        """Notify on Facebook about notification."""
        return f"Facebook: {notification}"


class SlackNotifier(Notifier):

    def notify(self, notification: str):
        """Notify on Slack about notification."""
        return f"Slack: {notification}"


class NotifierDecorator(Notifier):

    def __init__(self, notifier: Notifier = None):
        self.__notifier = notifier

    def get_notifier(self):
        """Get the current notifier"""
        return self.__notifier

    def notify(self, notification: str):
        """Notify via given notifier"""
        return self.__notifier.notify(notification)


class EmailNotifierDecorator(NotifierDecorator):

    def notify(self, notification: str):
        """Decorated Email Notifier"""
        return f"Email: {self.get_notifier().notify(notification)}"


class SMSNotifierDecorator(NotifierDecorator):

    def notify(self, notification: str):
        """Decorated SMS Notifier"""
        return f"SMS: {self.get_notifier().notify(notification)}"


class FacebookNotifierDecorator(NotifierDecorator):

    def notify(self, notification: str):
        """Decorated Facebook Notifier"""
        return f"Facebook: {self.get_notifier().notify(notification)}"


class SlackNotifierDecorator(NotifierDecorator):

    def notify(self, notification: str):
        """Decorated Slack Notifier"""
        return f"Slack: {self.get_notifier().notify(notification)}"


if __name__ == "__main__":

    # Simple Notifiers
    email_notifier = EmailNotifier()
    print(email_notifier.notify("Notified!"))

    sms_notifier = SMSNotifier()
    print(sms_notifier.notify("Notified!"))

    facebook_notifier = FacebookNotifier()
    print(facebook_notifier.notify("Notified!"))

    slack_notifier = SlackNotifier()
    print(slack_notifier.notify("Notified!"))

    # Decorated Notifiers
    sms_and_slack_notifier = SlackNotifierDecorator(sms_notifier)
    print(sms_and_slack_notifier.notify("Notified!"))

    sms_and_facebook_notifier = FacebookNotifierDecorator(sms_notifier)
    print(sms_and_facebook_notifier.notify("Notified!"))

    facebook_and_slack_notifier = FacebookNotifierDecorator(slack_notifier)
    print(facebook_and_slack_notifier.notify("Notified!"))

    facebook_sms_slack_notifier = FacebookNotifierDecorator(
        sms_and_slack_notifier)
    print(facebook_sms_slack_notifier.notify("Notified!"))

    # Furthermore, Image is added in images folder,
    # for pictorial view of current Example
