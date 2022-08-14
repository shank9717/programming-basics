package org.shashank.basics.behavioral_patterns.state.mobile;

import org.shashank.basics.behavioral_patterns.state.states.RingState;
import org.shashank.basics.behavioral_patterns.state.states.SilentState;
import org.shashank.basics.behavioral_patterns.state.states.State;
import org.shashank.basics.behavioral_patterns.state.states.VibrateState;

public class Mobile {
    private State state;

    public Mobile() {
        this.state = new SilentState(this);
    }

    public void call() {
        System.out.println("Receiving call...");
        this.state.ring();
    }

    public void setSilent() {
        System.out.println("Setting mobile to silent");
        this.state = new SilentState(this);
    }

    public void setVibrate() {
        System.out.println("Setting mobile to vibrate");
        this.state = new VibrateState(this);
    }

    public void setRing() {
        System.out.println("Setting mobile to ring");
        this.state = new RingState(this);
    }

    public void silentNotify() {
        System.out.println("Silently displaying incoming call");
    }

    public void vibrationNotify() {
        System.out.println("Vibrating and displaying incoming call");
    }

    public void ringNotify() {
        System.out.println("Ringing and displaying incoming call");
    }
}
