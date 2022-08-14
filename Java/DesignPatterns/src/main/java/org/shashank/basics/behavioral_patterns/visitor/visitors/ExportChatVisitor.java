package org.shashank.basics.behavioral_patterns.visitor.visitors;

import org.shashank.basics.behavioral_patterns.visitor.chats.BroadcastChat;
import org.shashank.basics.behavioral_patterns.visitor.chats.Chat;
import org.shashank.basics.behavioral_patterns.visitor.chats.GroupChat;
import org.shashank.basics.behavioral_patterns.visitor.chats.PersonalChat;

import java.util.List;

public class ExportChatVisitor implements Visitor {

    public String exportAll(List<Chat> chats) {
        StringBuilder sb = new StringBuilder();
        sb.append("<?xml version=\"1.0\" encoding=\"utf-8\"?>" + "\n");
        for (Chat chat : chats) {
            sb.append(chat.accept(this)).append("\n");
        }
        return sb.toString();
    }

    @Override
    public String exportPersonalChat(PersonalChat chat) {
        return "<personal-chat>\n" +
                "\t<username>" + chat.getUserName() + "</username>\n" +
                "\t<lastMessageTime>" + chat.getLastMessageTime().toString() + "</lastMessageTime>\n" +
                "\t<messages>" + chat.getAllMessages().toString() + "</messages>\n" +
                "</personal-chat>";
    }

    @Override
    public String exportGroupChat(GroupChat chat) {
        return "<personal-chat>\n" +
                "\t<group-name>" + chat.getGroupName() + "</group-name>\n" +
                "\t<participants>\n" +
                this.getParticipantsExport(chat.getUsers()) +
                "\t</participants>\n" +
                "\t<lastMessageTime>" + chat.getLastMessageTime().toString() + "</lastMessageTime>\n" +
                "\t<messages>" + chat.getAllMessages().toString() + "</messages>\n" +
                "</personal-chat>";
    }

    private String getParticipantsExport(List<String> users) {
        StringBuilder sb = new StringBuilder();
        for (String user: users) {
            sb.append("\t\t<username>").append(user).append("</username>\n");
        }
        return sb.toString();
    }

    @Override
    public String exportBroadcastChat(BroadcastChat chat) {
        StringBuilder sb = new StringBuilder();
        sb.append("<broadcast-chat>\n");
        for (Chat childChat : chat.getChildrenChats()) {
            String chatExport = childChat.accept(this);
            chatExport = "\t" + chatExport.replace("\n", "\n\t") + "\n";
            sb.append(chatExport);
        }
        sb.append("</broadcast-chat>\n");
        return sb.toString();
    }
}
