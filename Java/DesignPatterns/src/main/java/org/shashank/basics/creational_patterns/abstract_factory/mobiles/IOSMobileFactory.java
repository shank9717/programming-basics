/*
    This is a concrete implementation of base factory class
 */
package org.shashank.basics.creational_patterns.abstract_factory.mobiles;

import org.shashank.basics.creational_patterns.abstract_factory.menus.IOSMenu;
import org.shashank.basics.creational_patterns.abstract_factory.menus.Menu;
import org.shashank.basics.creational_patterns.abstract_factory.settings.IOSSettings;
import org.shashank.basics.creational_patterns.abstract_factory.settings.Settings;
import org.shashank.basics.creational_patterns.abstract_factory.apps.App;
import org.shashank.basics.creational_patterns.abstract_factory.apps.IOSApp;

public class IOSMobileFactory extends MobileFactory {
    @Override
    public App createApp() {
        return new IOSApp();
    }

    @Override
    public Menu createMenu() {
        return new IOSMenu();
    }

    @Override
    public Settings createSettings() {
        return new IOSSettings();
    }
}
