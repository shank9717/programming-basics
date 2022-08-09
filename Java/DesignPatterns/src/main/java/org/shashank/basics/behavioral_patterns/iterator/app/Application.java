package org.shashank.basics.behavioral_patterns.iterator.app;

public class Application {
    private final String appName;

    private final float appSize;

    public Application(String appName, float appSize) {
        this.appName = appName;
        this.appSize = appSize;
    }

    public String getAppName() {
        return appName;
    }

    public float getAppSize() {
        return appSize;
    }

}