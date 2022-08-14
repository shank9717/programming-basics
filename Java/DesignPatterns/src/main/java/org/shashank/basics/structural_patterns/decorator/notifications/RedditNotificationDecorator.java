package org.shashank.basics.structural_patterns.decorator.notifications;

public class RedditNotificationDecorator extends NotificationDecorator {

    private final String userName;

    public RedditNotificationDecorator(Notifier notifier, String userName) {
        super(notifier);
        this.userName = userName;
    }

    @Override
    public void notify(String message) {
        System.out.println("Notifying reddit user with username: " + getUserName() + " - " + message);
        this.notifier.notify(message);
    }

    public String getUserName() {
        return userName;
    }
}
