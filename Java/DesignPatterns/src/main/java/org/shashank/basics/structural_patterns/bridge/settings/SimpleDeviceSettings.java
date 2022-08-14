package org.shashank.basics.structural_patterns.bridge.settings;

import org.shashank.basics.structural_patterns.bridge.mobiles.Mobile;

import java.util.Set;

public class SimpleDeviceSettings implements Settings {
    Mobile mobile;
    public SimpleDeviceSettings() {

    }
    public SimpleDeviceSettings(Mobile mobile) {
        System.out.println("Created simple settings for mobile type: " + mobile.getMobileType());
        this.mobile = mobile;
    }

    @Override
    public void setVolume(int volume) {
        this.mobile.setVolume(volume);
    }

    @Override
    public void connectBluetooth() {
        this.mobile.setConnectedToBluetooth(true);
        System.out.println("Bluetooth connected");
    }

    @Override
    public void disconnectBluetooth() {
        this.mobile.setConnectedToBluetooth(false);
        System.out.println("Bluetooth disconnected");
    }

    @Override
    public void turnOnMobileData() {
        this.mobile.setMobileDataOn(true);
        System.out.println("Mobile data turned on");
    }

    @Override
    public void turnOffMobileData() {
        this.mobile.setMobileDataOn(false);
        System.out.println("Mobile data turned off");
    }

    @Override
    public void connectWifi() {
        this.mobile.setConnectedToWifi(true);
        System.out.println("Connected to WiFi");
    }

    @Override
    public void disconnectWifi() {
        this.mobile.setConnectedToWifi(false);
        System.out.println("Disconnected from WiFi");
    }
}
