package org.shashank.basics.behavioral_patterns.mediator.servers;

import org.shashank.basics.behavioral_patterns.mediator.users.User;

public interface ChatServer {
    void printMessage(String msg, User user);
}
