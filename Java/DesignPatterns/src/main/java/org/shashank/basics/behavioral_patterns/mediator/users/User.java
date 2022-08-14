package org.shashank.basics.behavioral_patterns.mediator.users;

public abstract class User {
    String name;

    User(String name) {
        this.name = name;
    }

    public abstract String getName();

    public abstract void sendMessage(String message);
}
