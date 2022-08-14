package org.shashank.basics.behavioral_patterns.observer.listeners;

public class ChatClient implements EventListener {

    @Override
    public void notify(String eventType, String chatName) {
        if (eventType.equals("UpdateMessages")) {
            System.out.println("ChatClient - Fetching messages in chat: " + chatName);
            // Fetch messages.
        } else if (eventType.equals("NumberChange")) {
            System.out.println("ChatClient - Contact number changed for contact: " + chatName);
            // Display new number
        }
    }
}
