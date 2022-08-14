package org.shashank.basics.behavioral_patterns.visitor.visitors;

import org.shashank.basics.behavioral_patterns.visitor.chats.BroadcastChat;
import org.shashank.basics.behavioral_patterns.visitor.chats.GroupChat;
import org.shashank.basics.behavioral_patterns.visitor.chats.PersonalChat;

public interface Visitor {
    String exportPersonalChat(PersonalChat chat);

    String exportGroupChat(GroupChat chat);

    String exportBroadcastChat(BroadcastChat chat);
}
