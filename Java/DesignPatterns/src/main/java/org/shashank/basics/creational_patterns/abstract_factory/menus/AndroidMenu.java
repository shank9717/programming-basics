package org.shashank.basics.creational_patterns.abstract_factory.menus;

public class AndroidMenu implements Menu {

    @Override
    public void configureMenu() {
        System.out.println("Configuring Android menu !");
    }

    @Override
    public void openMenu() {
        System.out.println("Opening Android menu !");
    }
}
