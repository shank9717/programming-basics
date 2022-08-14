package org.shashank.basics.behavioral_patterns.strategy.mobile;

import org.shashank.basics.behavioral_patterns.strategy.apps.AndroidApp;

public class AndroidMobile {
    private AndroidApp app;

    public void openHyperlink(String url) {
        this.app.openHyperLink(url);
    }

    public void setApp(AndroidApp app) {
        this.app = app;
    }
}
