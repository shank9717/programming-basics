package org.shashank.basics.creational_patterns.abstract_factory.settings;

public class IOSSettings implements Settings {

    @Override
    public void configureSettings() {
        System.out.println("Configuring IOS settings !");
    }
}
