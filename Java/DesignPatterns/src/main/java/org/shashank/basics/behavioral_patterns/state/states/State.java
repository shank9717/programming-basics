package org.shashank.basics.behavioral_patterns.state.states;

import org.shashank.basics.behavioral_patterns.state.mobile.Mobile;

public abstract class State {
    final Mobile mobile;

    State(Mobile mobile) {
        this.mobile = mobile;
    }

    public abstract void ring();
}
