package org.shashank.basics.behavioral_patterns.mediator;

import org.shashank.basics.behavioral_patterns.mediator.servers.ChatServer;
import org.shashank.basics.behavioral_patterns.mediator.servers.PrivateChatServer;
import org.shashank.basics.behavioral_patterns.mediator.users.UserA;
import org.shashank.basics.behavioral_patterns.mediator.users.UserB;

public class Main {
    public static void main(String[] args) {
        ChatServer server = new PrivateChatServer();
        UserA userA = new UserA("Shashank", server);
        UserB userB = new UserB("John", server);

        userA.sendMessage("Hello !");
        userB.sendMessage("Hey there!");
    }
}
