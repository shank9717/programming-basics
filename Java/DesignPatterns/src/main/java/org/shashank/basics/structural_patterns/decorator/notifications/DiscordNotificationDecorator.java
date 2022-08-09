package org.shashank.basics.structural_patterns.decorator.notifications;

public class DiscordNotificationDecorator extends NotificationDecorator {

    private final int userId;

    public DiscordNotificationDecorator(Notifier notifier, int userId) {
        super(notifier);
        this.userId = userId;
    }

    @Override
    public void notify(String message) {
        System.out.println("Notifying discord user with ID: " + getUserId() + " - " + message);
        this.notifier.notify(message);
    }

    public int getUserId() {
        return userId;
    }
}
