package org.shashank.basics.behavioral_patterns.strategy.apps;

public class YoutubeMusicApp implements AndroidApp {

    @Override
    public void openHyperLink(String url) {
        System.out.println("Opening " + url + " on YTMusic");
    }

    public String getAppName() {
        return "YT Music";
    }
}
