package org.shashank.basics.structural_patterns.facade.message_facade;

import org.shashank.basics.structural_patterns.facade.chats.Chat;
import org.shashank.basics.structural_patterns.facade.chats.ChatRepository;
import org.shashank.basics.structural_patterns.facade.messaging_library.MessageHolder;
import org.shashank.basics.structural_patterns.facade.messaging_library.Messaging;
import org.shashank.basics.structural_patterns.facade.messaging_library.MessagingFactory;

import java.util.ArrayList;
import java.util.List;
import java.util.Optional;

public class MessageFacade {
    public void sendMessage(int chatId, MessageHolder message) {
        List<Chat> allChats = ChatRepository.getChats();
        Optional<Chat> receipent = allChats.stream()
                .filter(chat -> chat.getChatId() == chatId).findFirst();

        if (!receipent.isPresent()) {
            throw new RuntimeException("No such chat found!");
        }

        Messaging messaging = MessagingFactory.getMessaging(message);
        messaging.sendMessage(receipent.get(), message.getMessage());
    }
}
