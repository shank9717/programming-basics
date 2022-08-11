package org.shashank.basics.behavioral_patterns.observer.server;

public enum EventType {
    NUMBER_CHANGE("NumberChange"), UPDATE_MESSAGES("UpdateMessages");

    private final String type;

    EventType(String type) {
        this.type = type;
    }

    public String getType() {
        return type;
    }
}
