package org.shashank.basics.behavioral_patterns.state.states;

import org.shashank.basics.behavioral_patterns.state.mobile.Mobile;

public class SilentState extends State {

    public SilentState(Mobile mobile) {
        super(mobile);
    }

    @Override
    public void ring() {
        this.mobile.silentNotify();
    }
}
