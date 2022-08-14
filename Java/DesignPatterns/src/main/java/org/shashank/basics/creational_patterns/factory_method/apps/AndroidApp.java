package org.shashank.basics.creational_patterns.factory_method.apps;

public class AndroidApp implements App {
    public AndroidApp() {
        System.out.println("Created Android App !");
    }

    @Override
    public void runApp() {
        System.out.println("Running Android App !");
    }
}
