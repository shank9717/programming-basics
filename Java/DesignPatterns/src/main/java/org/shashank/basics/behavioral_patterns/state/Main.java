package org.shashank.basics.behavioral_patterns.state;

import org.shashank.basics.behavioral_patterns.state.mobile.Mobile;

public class Main {
    public static void main(String[] args) {
        Mobile mobile = new Mobile();
        mobile.call();
        System.out.println();

        mobile.setRing();
        mobile.call();
        System.out.println();

        mobile.setVibrate();
        mobile.call();
        System.out.println();

        mobile.setSilent();
        mobile.call();
        System.out.println();
    }
}
