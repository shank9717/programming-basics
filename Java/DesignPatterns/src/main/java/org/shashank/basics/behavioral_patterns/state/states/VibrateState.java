package org.shashank.basics.behavioral_patterns.state.states;

import org.shashank.basics.behavioral_patterns.state.mobile.Mobile;

public class VibrateState extends State {

    public VibrateState(Mobile mobile) {
        super(mobile);
    }

    @Override
    public void ring() {
        this.mobile.vibrationNotify();
    }
}