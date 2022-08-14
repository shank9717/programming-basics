package org.shashank.basics.behavioral_patterns.visitor.chats;

import org.shashank.basics.behavioral_patterns.visitor.visitors.ExportChatVisitor;
import org.shashank.basics.behavioral_patterns.visitor.visitors.Visitor;

import java.util.Date;
import java.util.List;

public interface Chat {
    Date getLastMessageTime();

    void sendMessage(String message);

    List<String> getAllMessages();

    String accept(Visitor visitor);
}
