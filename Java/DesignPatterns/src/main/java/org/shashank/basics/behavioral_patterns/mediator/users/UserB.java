package org.shashank.basics.behavioral_patterns.mediator.users;

import org.shashank.basics.behavioral_patterns.mediator.servers.ChatServer;

public class UserB extends User {

    private final ChatServer server;

    public UserB (String name, ChatServer server) {
        super(name);
        this.server = server;
    }

    @Override
    public String getName() {
        return this.name;
    }

    @Override
    public void sendMessage(String message) {
        server.printMessage(message, this);
    }
}