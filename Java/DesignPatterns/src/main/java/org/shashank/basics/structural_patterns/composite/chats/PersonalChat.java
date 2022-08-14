package org.shashank.basics.structural_patterns.composite.chats;

import java.util.ArrayList;
import java.util.Date;
import java.util.List;

public class PersonalChat implements Chat {

    private final String userName;
    private Date lastMessageTime;

    List<String> allMessages = new ArrayList<>();

    public PersonalChat(String userName) {
        this.userName = userName;
    }

    @Override
    public Date getLastMessageTime() {
        return lastMessageTime;
    }

    public void setLastMessageTime(Date messageTime) {
        this.lastMessageTime = messageTime;
    }

    @Override
    public void sendMessage(String message) {
        this.allMessages.add(message);
        this.lastMessageTime = new Date();
        System.out.println("Sending message to " + userName + " - " + message);
    }

    @Override
    public List<String> getAllMessages() {
        return allMessages;
    }

    public void addReceivedMessage(String message) {
        this.allMessages.add(message);
        this.lastMessageTime = new Date();
        System.out.println("Received message from " + userName + " - " + message);
    }

    @Override
    public String toString() {
        return "Personal chat (" + userName +")";
    }
}
