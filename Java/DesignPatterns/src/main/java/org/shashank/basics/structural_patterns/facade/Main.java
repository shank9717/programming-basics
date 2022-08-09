package org.shashank.basics.structural_patterns.facade;

import org.shashank.basics.structural_patterns.facade.chats.Chat;
import org.shashank.basics.structural_patterns.facade.chats.ChatRepository;
import org.shashank.basics.structural_patterns.facade.chats.PersonalChat;
import org.shashank.basics.structural_patterns.facade.message_facade.MessageFacade;
import org.shashank.basics.structural_patterns.facade.messaging_library.MessageHolder;

import java.nio.charset.StandardCharsets;

public class Main {
    public static void main(String[] args) {
        ChatRepository.addChat(new PersonalChat(31, "Shashank"));
        MessageFacade messager = new MessageFacade();
        messager.sendMessage(31, new MessageHolder(1, "imageBytes".getBytes()));
    }
}
