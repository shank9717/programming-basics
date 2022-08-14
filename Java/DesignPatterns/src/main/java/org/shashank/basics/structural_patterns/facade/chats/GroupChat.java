package org.shashank.basics.structural_patterns.facade.chats;

import java.util.ArrayList;
import java.util.List;

public class GroupChat extends BasicChat {

    public GroupChat(int chatId, String chatName, List<String> participants) {
        this.chatId = chatId;
        this.chatName = chatName;
        this.participants = participants;
    }
}
