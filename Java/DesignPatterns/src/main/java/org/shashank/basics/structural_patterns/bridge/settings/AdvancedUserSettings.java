package org.shashank.basics.structural_patterns.bridge.settings;

import org.shashank.basics.structural_patterns.bridge.mobiles.Mobile;

public class AdvancedUserSettings extends SimpleDeviceSettings {
    public AdvancedUserSettings() {
        super();
    }

    public AdvancedUserSettings (Mobile mobile) {
        super(mobile);
    }

    public void turnOnDeveloperMode() {
        this.mobile.setDeveloperMode(true);
    }

    public void turnOffDeveloperMode() {
        this.mobile.setDeveloperMode(false);
    }
}
