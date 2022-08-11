package org.shashank.basics.behavioral_patterns.observer;

import org.shashank.basics.behavioral_patterns.observer.listeners.ChatClient;
import org.shashank.basics.behavioral_patterns.observer.listeners.NotificationBarEventListener;
import org.shashank.basics.behavioral_patterns.observer.server.ChatServer;
import org.shashank.basics.behavioral_patterns.observer.server.EventType;

public class Main {
    public static void main(String[] args) {
        ChatServer server = new ChatServer();
        server.getEvents().subscribe(EventType.NUMBER_CHANGE.getType(), new ChatClient());
        server.getEvents().subscribe(EventType.UPDATE_MESSAGES.getType(), new ChatClient());
        server.getEvents().subscribe(EventType.UPDATE_MESSAGES.getType(), new NotificationBarEventListener());

        try {
            server.changeContactNumber("Shashank");
            server.updateMessages("John");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
