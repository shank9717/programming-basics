package org.shashank.basics.behavioral_patterns.strategy.apps;

public class YoutubeApp implements AndroidApp {

    @Override
    public void openHyperLink(String url) {
        System.out.println("Opening " + url + " on Youtube app");
    }

    public String getAppName() {
        return "Youtube";
    }
}
