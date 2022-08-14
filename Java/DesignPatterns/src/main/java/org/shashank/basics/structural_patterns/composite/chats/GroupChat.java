package org.shashank.basics.structural_patterns.composite.chats;

import java.util.ArrayList;
import java.util.Date;
import java.util.List;

public class GroupChat implements Chat {

    private final List<String> userNames;
    private final String groupName;
    private Date lastMessageTime;

    List<String> allMessages = new ArrayList<>();

    public GroupChat(List<String> userNames, String groupName) {
        this.userNames = userNames;
        this.groupName = groupName;
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
        System.out.println("Sending message in group chat " + groupName + " - " + message);
    }

    @Override
    public List<String> getAllMessages() {
        return allMessages;
    }


    public void addReceivedMessage(String message) {
        this.allMessages.add(message);
        this.lastMessageTime = new Date();
    }

    public void addReceivedMessage(String message, String userName) {
        System.out.println("Received message in group chat " + groupName
                + " from user " + userName + "- " + message);
        addReceivedMessage(message);
    }

    @Override
    public String toString() {
        return "Group chat (" + groupName +")";
    }
}
