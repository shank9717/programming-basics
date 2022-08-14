/*
    This is a concrete implementation of base factory class
 */
package org.shashank.basics.creational_patterns.abstract_factory.mobiles;

import org.shashank.basics.creational_patterns.abstract_factory.apps.App;
import org.shashank.basics.creational_patterns.abstract_factory.menus.AndroidMenu;
import org.shashank.basics.creational_patterns.abstract_factory.menus.Menu;
import org.shashank.basics.creational_patterns.abstract_factory.settings.AndroidSettings;
import org.shashank.basics.creational_patterns.abstract_factory.settings.Settings;
import org.shashank.basics.creational_patterns.abstract_factory.apps.AndroidApp;

public class AndroidMobileFactory extends MobileFactory {
    @Override
    public App createApp() {
        return new AndroidApp();
    }

    @Override
    public Menu createMenu() {
        return new AndroidMenu();
    }

    @Override
    public Settings createSettings() {
        return new AndroidSettings();
    }
}
