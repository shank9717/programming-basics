package org.shashank.basics.behavioral_patterns.strategy.apps;

public class ChromeApp implements AndroidApp {

    @Override
    public void openHyperLink(String url) {
        System.out.println("Opening " + url + " on Google Chrome");
    }

    public String getAppName() {
        return "Chrome";
    }
}
