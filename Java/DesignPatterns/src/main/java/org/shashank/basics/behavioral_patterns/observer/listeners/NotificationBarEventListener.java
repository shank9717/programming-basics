package org.shashank.basics.behavioral_patterns.observer.listeners;

public class NotificationBarEventListener implements EventListener {

    @Override
    public void notify(String eventType, String chatName) {
        System.out.println("Notification bar - Possible new messages in chat: " + chatName);
    }
}
