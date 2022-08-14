package org.shashank.basics.behavioral_patterns.visitor;

import org.shashank.basics.behavioral_patterns.visitor.chats.BroadcastChat;
import org.shashank.basics.behavioral_patterns.visitor.chats.GroupChat;
import org.shashank.basics.behavioral_patterns.visitor.chats.PersonalChat;
import org.shashank.basics.behavioral_patterns.visitor.visitors.ExportChatVisitor;

import java.util.Arrays;

public class Main {

    public static void main(String[] args) {
        MessagingApplication app = new MessagingApplication();
        PersonalChat shashank = new PersonalChat("Shashank");
        PersonalChat john = new PersonalChat("John");

        GroupChat tempGroup = new GroupChat(Arrays.asList("Shashank", "Melanie"), "TempGroup");
        GroupChat anonymous = new GroupChat(Arrays.asList("Jane", "Doe"), "Anonymous");

        BroadcastChat broadcastChat = new BroadcastChat(john, tempGroup, anonymous);

        shashank.sendMessage("Hey Shashank");
        john.addReceivedMessage("Hey, John here");
        tempGroup.sendMessage("What is this group?");
        anonymous.sendMessage("Redacted message");

        app.loadChats(
                shashank,
                john,
                tempGroup,
                anonymous,
                broadcastChat
        );

        ExportChatVisitor visitor = new ExportChatVisitor();
        String exportedXml = visitor.exportAll(app.getAllChats());
        System.out.println("Exported XML: \n" + exportedXml);
    }
}
