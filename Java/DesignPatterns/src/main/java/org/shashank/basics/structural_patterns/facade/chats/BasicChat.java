package org.shashank.basics.structural_patterns.facade.chats;

import java.util.List;

public class BasicChat implements Chat {
    List<String> participants;
    int chatId;
    String chatName;

    @Override
    public int getChatId() {
        return this.chatId;
    }

    @Override
    public void setChatId(int chatId) {
        this.chatId = chatId;
    }

    @Override
    public String getChatName() {
        return this.chatName;
    }

    @Override
    public void setChatName(String chatName) {
        this.chatName = chatName;
    }

    @Override
    public List<String> getParticipants() {
        return this.participants;
    }

    @Override
    public void setParticipants(List<String> participants) {
        this.participants = participants;
    }
}
