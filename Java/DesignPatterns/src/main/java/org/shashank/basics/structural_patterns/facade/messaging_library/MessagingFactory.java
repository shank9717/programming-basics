package org.shashank.basics.structural_patterns.facade.messaging_library;

import org.shashank.basics.structural_patterns.composite.chats.Chat;

public class MessagingFactory {

    public static Messaging getMessaging(MessageHolder messageHolder) {
        if (messageHolder.getMessageType() == 0) {
            return new TextMessage();
        } else {
            return new ImageMessage();
        }
    }
}
