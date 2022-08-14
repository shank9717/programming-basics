package org.shashank.basics.structural_patterns.facade.messaging_library;

import org.shashank.basics.structural_patterns.facade.chats.Chat;

public interface Messaging {
    void sendMessage(Chat chat, byte[] message);
}
