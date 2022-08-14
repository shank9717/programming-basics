package org.shashank.basics.structural_patterns.bridge;

import org.shashank.basics.structural_patterns.bridge.mobiles.AndroidMobile;
import org.shashank.basics.structural_patterns.bridge.mobiles.IOSMobile;
import org.shashank.basics.structural_patterns.bridge.mobiles.Mobile;
import org.shashank.basics.structural_patterns.bridge.settings.AdvancedUserSettings;
import org.shashank.basics.structural_patterns.bridge.settings.SimpleDeviceSettings;

public class Main {
    public static void main(String[] args) {
        Mobile androidMobile = new AndroidMobile();
        Mobile iosMobile = new IOSMobile();
        SimpleDeviceSettings androidSettings = new SimpleDeviceSettings(androidMobile);
        AdvancedUserSettings iosSettings = new AdvancedUserSettings(iosMobile);

        androidSettings.setVolume(90);
        androidSettings.connectWifi();
        androidSettings.turnOffMobileData();
        androidSettings.disconnectBluetooth();

        iosSettings.turnOnDeveloperMode();
        iosSettings.connectBluetooth();
        iosSettings.disconnectWifi();
        iosSettings.turnOnMobileData();

        System.out.println(androidMobile.getSettings());
        System.out.println(iosMobile.getSettings());
    }
}
