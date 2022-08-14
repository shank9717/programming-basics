package org.shashank.basics.behavioral_patterns.observer.server;

import org.shashank.basics.behavioral_patterns.observer.publishers.EventProducer;

public class ChatServer {

    private final EventProducer events;

    public ChatServer() {
        this.events = new EventProducer(EventType.NUMBER_CHANGE, EventType.UPDATE_MESSAGES);
    }

    public void changeContactNumber(String chatName) {
        this.events.notify("NumberChange", chatName);
    }

    public void updateMessages(String chatName) {
        this.events.notify("UpdateMessages", chatName);
    }

    public EventProducer getEvents() {
        return events;
    }

}

