/*
    This is a concrete implementation of base factory class
 */
package org.shashank.basics.structural_patterns.bridge.mobiles;


public class AndroidMobile implements Mobile {
    private final String mobileType;

    public boolean connectedToWifi;
    public boolean connectedToBluetooth;
    public boolean mobileDataStatus;

    public int volume = 50;
    private boolean developerMode = false;

    public AndroidMobile() {
        this.mobileType = "Android";
    }

    @Override
    public boolean isConnectedToWifi() {
        return this.connectedToWifi;
    }

    @Override
    public void setConnectedToWifi(boolean connected) {
        this.connectedToWifi = connected;
    }

    @Override
    public boolean isConnectedToBluetooth() {
        return this.connectedToBluetooth;
    }

    @Override
    public void setConnectedToBluetooth(boolean connected) {
        this.connectedToBluetooth = connected;
    }

    @Override
    public boolean isMobileDataOn() {
        return this.mobileDataStatus;
    }

    @Override
    public void setMobileDataOn(boolean status) {
        this.mobileDataStatus = status;
    }

    @Override
    public int getVolume() {
        return this.volume;
    }

    @Override
    public void setVolume(int volume) {
        if (volume >= 100) {
            this.volume = 100;
        } else {
            this.volume = Math.max(volume, 0);
        }
    }

    @Override
    public String getMobileType() {
        return mobileType;
    }

    @Override
    public void setDeveloperMode(boolean developer) {
        this.developerMode = developer;
    }

    @Override
    public boolean getDeveloperMode() {
        return this.developerMode;
    }

    public String getSettings() {
        return "Mobile Type: " + getMobileType() + "\n" +
                "Mobile volume: " + getVolume() + "\n" +
                "Connected to Wifi: " + isConnectedToWifi() + "\n" +
                "Connected to Bluetooth: " + isConnectedToBluetooth() + "\n" +
                "Mobile Data Status: " + isMobileDataOn() + "\n" +
                "Developer Mode: " + getDeveloperMode() + "\n";
    }

}
