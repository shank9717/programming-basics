package org.shashank.basics.structural_patterns.composite.chats;

import java.util.Date;
import java.util.List;

public interface Chat {
    Date getLastMessageTime();

    void sendMessage(String message);

    List<String> getAllMessages();

}
