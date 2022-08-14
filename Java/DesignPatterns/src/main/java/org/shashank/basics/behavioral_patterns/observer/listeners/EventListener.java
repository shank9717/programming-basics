package org.shashank.basics.behavioral_patterns.observer.listeners;

public interface EventListener {
    void notify(String eventType, String chatName);
}
