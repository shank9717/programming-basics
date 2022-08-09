package org.shashank.basics.structural_patterns.facade.messaging_library;

public class MessageHolder {
    int messageType;

    byte[] message;

    public MessageHolder(int messageType, byte[] message) {
        this.messageType = messageType;
        this.message = message;
    }

    public int getMessageType() {
        return messageType;
    }

    public void setMessageType(int messageType) {
        this.messageType = messageType;
    }

    public byte[] getMessage() {
        return message;
    }

    public void setMessage(byte[] message) {
        this.message = message;
    }

}
