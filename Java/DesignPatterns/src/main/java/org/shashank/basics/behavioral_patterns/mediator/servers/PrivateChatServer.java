package org.shashank.basics.behavioral_patterns.mediator.servers;

import org.shashank.basics.behavioral_patterns.mediator.users.User;

import java.text.DateFormat;
import java.text.SimpleDateFormat;
import java.util.Date;

public class PrivateChatServer implements ChatServer {

    @Override
    public void printMessage(String msg, User user) {
        DateFormat dateFormat = new SimpleDateFormat("E dd-MM-yyyy hh:mm a");
        Date currentDateTime = new Date();
        System.out.println("[" + dateFormat.format(currentDateTime) + "] - "
                + user.getName() + ": "  + msg);
    }
}
