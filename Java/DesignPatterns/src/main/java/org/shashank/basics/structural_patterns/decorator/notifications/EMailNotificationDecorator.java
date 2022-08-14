package org.shashank.basics.structural_patterns.decorator.notifications;

public class EMailNotificationDecorator extends NotificationDecorator {

    private final String email;

    public EMailNotificationDecorator(Notifier notifier, String email) {
        super(notifier);
        this.email = email;
    }

    @Override
    public void notify(String message) {
        System.out.println("Sending mail to : " + getEmail() + " - " + message);
        this.notifier.notify(message);
    }

    public String getEmail() {
        return email;
    }
}
