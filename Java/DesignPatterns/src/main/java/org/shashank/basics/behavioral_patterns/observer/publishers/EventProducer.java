package org.shashank.basics.behavioral_patterns.observer.publishers;

import org.shashank.basics.behavioral_patterns.observer.listeners.EventListener;
import org.shashank.basics.behavioral_patterns.observer.server.EventType;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class EventProducer {
    Map<String, List<EventListener>> eventListeners = new HashMap<>();


    public EventProducer(EventType... events) {
        for (EventType eventType : events) {
            this.eventListeners.put(eventType.getType(), new ArrayList<>());
        }
    }

    public void subscribe(String eventType, EventListener listener) {
        List<EventListener> listeners = this.eventListeners.getOrDefault(eventType, new ArrayList<>());
        listeners.add(listener);
        this.eventListeners.put(eventType, listeners);
    }

    public void notify(String eventType, String chatName) {
        System.out.println("Event triggered: " + eventType);
        List<EventListener> listeners = eventListeners.get(eventType);
        for (EventListener listener : listeners) {
            listener.notify(eventType, chatName);
        }
    }
}
