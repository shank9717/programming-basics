/*
    This is the base factory class
 */
package org.shashank.basics.structural_patterns.bridge.mobiles;

import org.shashank.basics.creational_patterns.abstract_factory.apps.App;
import org.shashank.basics.creational_patterns.abstract_factory.menus.Menu;
import org.shashank.basics.creational_patterns.abstract_factory.settings.Settings;

public interface Mobile {
    boolean isConnectedToWifi();

    void setConnectedToWifi(boolean connected);

    boolean isConnectedToBluetooth();

    void setConnectedToBluetooth(boolean connected);

    int getVolume();

    void setVolume(int volume);

    boolean isMobileDataOn();

    void setMobileDataOn(boolean status);

    String getMobileType();

    void setDeveloperMode(boolean developer);

    boolean getDeveloperMode();

    String getSettings();

}
