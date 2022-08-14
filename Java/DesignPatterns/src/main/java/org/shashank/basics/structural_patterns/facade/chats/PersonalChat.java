package org.shashank.basics.structural_patterns.facade.chats;

import java.util.ArrayList;
import java.util.List;

public class PersonalChat extends BasicChat {

    public PersonalChat(int chatId, String participant) {
        this.chatId = chatId;
        this.chatName = participant;
        this.participants = new ArrayList<>();
        this.participants.add(participant);
    }
}
