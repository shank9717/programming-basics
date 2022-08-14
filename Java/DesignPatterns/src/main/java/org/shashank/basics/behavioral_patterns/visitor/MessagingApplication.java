package org.shashank.basics.behavioral_patterns.visitor;

import org.shashank.basics.behavioral_patterns.visitor.chats.Chat;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class MessagingApplication {
    private final List<Chat> allChats = new ArrayList<>();

    public void loadChats(Chat... chats) {
        for (Chat chat: chats) {
            System.out.println("Loaded chat: " + chat);
        }
        allChats.addAll(Arrays.asList(chats));
    }
}
