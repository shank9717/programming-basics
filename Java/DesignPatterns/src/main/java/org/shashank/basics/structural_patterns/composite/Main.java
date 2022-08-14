package org.shashank.basics.structural_patterns.composite;

import org.shashank.basics.structural_patterns.composite.chats.BroadcastChat;
import org.shashank.basics.structural_patterns.composite.chats.GroupChat;
import org.shashank.basics.structural_patterns.composite.chats.PersonalChat;
import org.shashank.basics.structural_patterns.composite.messaging_app.MessagingApplication;

import java.util.ArrayList;
import java.util.Arrays;

public class Main {

    public static void main(String[] args) {
        MessagingApplication app = new MessagingApplication();
        PersonalChat shashank = new PersonalChat("Shashank");
        PersonalChat john = new PersonalChat("John");

        GroupChat tempGroup = new GroupChat(Arrays.asList("Shashank", "Melanie"), "TempGroup");
        GroupChat anonymous = new GroupChat(Arrays.asList("Jane", "Doe"), "Anonymous");

        BroadcastChat broadcastChat = new BroadcastChat(john, tempGroup, anonymous);

        app.loadChats(
                shashank,
                john,
                tempGroup,
                anonymous,
                broadcastChat
        );

        broadcastChat.sendMessage("Hello to all");

    }
}
