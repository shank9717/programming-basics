package org.shashank.basics.creational_patterns.abstract_factory;

import org.shashank.basics.creational_patterns.abstract_factory.apps.App;
import org.shashank.basics.creational_patterns.abstract_factory.menus.Menu;
import org.shashank.basics.creational_patterns.abstract_factory.mobiles.MobileFactory;
import org.shashank.basics.creational_patterns.abstract_factory.settings.Settings;

public class Mobile {
    private final Menu menu;
    private final Settings settings;
    private final App app;

    public Mobile(MobileFactory factory) {
        app = factory.createApp();
        menu = factory.createMenu();
        settings = factory.createSettings();
    }

    public void start() {
        System.out.println("Turning on mobile...");
    }

    public void openApp() {
        settings.configureSettings();
        menu.openMenu();
        app.runApp();
    }

}
