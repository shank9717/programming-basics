package org.shashank.basics.creational_patterns.abstract_factory.menus;

public class IOSMenu implements Menu {

    @Override
    public void configureMenu() {
        System.out.println("Configuring IOS menu !");
    }

    @Override
    public void openMenu() {
        System.out.println("Opening IOS menu !");
    }
}
