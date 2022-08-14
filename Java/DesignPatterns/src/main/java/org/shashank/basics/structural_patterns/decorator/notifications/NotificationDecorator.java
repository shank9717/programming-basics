package org.shashank.basics.structural_patterns.decorator.notifications;

public class NotificationDecorator implements Notifier {
    Notifier notifier;

    NotificationDecorator(Notifier notifier) {
        this.notifier = notifier;
    }


    @Override
    public void notify(String message) {
        notifier.notify(message);
    }
}
