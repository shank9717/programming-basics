package org.shashank.basics.structural_patterns.bridge.settings;

public interface Settings {
    void setVolume(int volume);

    void connectBluetooth();

    void disconnectBluetooth();

    void turnOnMobileData();

    void turnOffMobileData();

    void connectWifi();

    void disconnectWifi();
}
