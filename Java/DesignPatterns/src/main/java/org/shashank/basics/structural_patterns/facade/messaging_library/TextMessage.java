package org.shashank.basics.structural_patterns.facade.messaging_library;

import org.shashank.basics.structural_patterns.facade.chats.Chat;

public class TextMessage implements Messaging {
    public void sendMessage(Chat chat, byte[] message) {
        System.out.println("Sending text message to chat: " + chat.getChatId());
    }
}