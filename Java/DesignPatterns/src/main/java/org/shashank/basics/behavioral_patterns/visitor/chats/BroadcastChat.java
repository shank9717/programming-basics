package org.shashank.basics.behavioral_patterns.visitor.chats;

import org.shashank.basics.behavioral_patterns.visitor.visitors.Visitor;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Date;
import java.util.List;

public class BroadcastChat implements Chat {

    private final List<Chat> childrenChats = new ArrayList<>();

    List<String> allMessages = new ArrayList<>();

    public BroadcastChat(Chat... chats) {
        this.childrenChats.addAll(Arrays.asList(chats));
    }

    @Override
    public Date getLastMessageTime() {
        Date lastMessageTime = null;
        Date chatMessageTime;
        for (Chat chat: childrenChats) {
            chatMessageTime = chat.getLastMessageTime();
            if (lastMessageTime == null || chatMessageTime.after(lastMessageTime)) {
                lastMessageTime = chatMessageTime;
            }
        }
        return lastMessageTime;
    }

    @Override
    public void sendMessage(String message) {
        for (Chat chat: childrenChats) {
            chat.sendMessage(message);
        }
    }

    @Override
    public List<String> getAllMessages() {
        List<String> allMessages = new ArrayList<>();
        for (Chat chat: childrenChats) {
            allMessages.addAll(chat.getAllMessages());
        }
        return allMessages;
    }

    @Override
    public String accept(Visitor visitor) {
        return visitor.exportBroadcastChat(this);
    }

    @Override
    public String toString() {
        return "Broadcast chat having - " + childrenChats;
    }

    public List<Chat> getChildrenChats() {
        return childrenChats;
    }
}
