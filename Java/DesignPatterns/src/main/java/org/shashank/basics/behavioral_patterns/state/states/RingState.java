package org.shashank.basics.behavioral_patterns.state.states;

import org.shashank.basics.behavioral_patterns.state.mobile.Mobile;

public class RingState extends State {

    public RingState(Mobile mobile) {
        super(mobile);
    }

    @Override
    public void ring() {
        this.mobile.ringNotify();
    }
}