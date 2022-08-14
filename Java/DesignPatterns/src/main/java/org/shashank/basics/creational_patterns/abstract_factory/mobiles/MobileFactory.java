/*
    This is the base factory class
 */
package org.shashank.basics.creational_patterns.abstract_factory.mobiles;

import org.shashank.basics.creational_patterns.abstract_factory.menus.Menu;
import org.shashank.basics.creational_patterns.abstract_factory.settings.Settings;
import org.shashank.basics.creational_patterns.abstract_factory.apps.App;

public abstract class MobileFactory {
    public abstract App createApp();

    public abstract Menu createMenu();

    public abstract Settings createSettings();
}
