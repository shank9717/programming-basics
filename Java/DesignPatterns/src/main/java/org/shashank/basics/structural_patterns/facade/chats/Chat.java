package org.shashank.basics.structural_patterns.facade.chats;

import java.util.List;

public interface Chat {
    int getChatId();

    void setChatId(int chatId);

    String getChatName();

    void setChatName(String chatName);

    List<String> getParticipants();

    void setParticipants(List<String> participants);
}
