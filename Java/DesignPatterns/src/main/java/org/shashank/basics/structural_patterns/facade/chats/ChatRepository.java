package org.shashank.basics.structural_patterns.facade.chats;

import java.util.ArrayList;
import java.util.List;

public class ChatRepository {
    static List<Chat> chats = new ArrayList<>();

    public static List<Chat> getChats() {
        return chats;
    }

    public static void addChat(Chat chat) {
        ChatRepository.chats.add(chat);
    }

    public static void setChats(List<Chat> chats) {
        ChatRepository.chats = chats;
    }
}
