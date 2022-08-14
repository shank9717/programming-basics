package org.shashank.basics.structural_patterns.decorator.notifications;

public class SimpleNotifier implements Notifier {

    @Override
    public void notify(String message) {
        System.out.println("Notifying to stdout: " + message);
    }
}
