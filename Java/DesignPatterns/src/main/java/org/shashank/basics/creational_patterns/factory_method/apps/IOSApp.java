package org.shashank.basics.creational_patterns.factory_method.apps;

public class IOSApp implements App {
    public IOSApp() {
        System.out.println("Created IOS App !");
    }

    @Override
    public void runApp() {
        System.out.println("Running IOS App !");
    }
}
