package org.shashank.basics.structural_patterns.decorator;

import org.shashank.basics.structural_patterns.decorator.notifications.*;

public class Main {
    public static void main(String[] args) {
        String notification1 = "e-mail password updation required";
        String notification2 = "New features available";

        // Sending notification only via mail
        NotificationDecorator notifier = new EMailNotificationDecorator(
                new SimpleNotifier(), "shank9717@gmail.com"
        );
        notifier.notify(notification1);

        System.out.println("-------------------------------------------");

        // Sending notification via both discord and reddit
        notifier = new DiscordNotificationDecorator(
                new RedditNotificationDecorator(
                        new SimpleNotifier(), "shank9717"
                ), 90110
        );
        notifier.notify(notification2);
    }
}
