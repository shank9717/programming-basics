package org.shashank.basics.behavioral_patterns.iterator;

import org.shashank.basics.behavioral_patterns.iterator.app.Application;
import org.shashank.basics.behavioral_patterns.iterator.iterators.AppIterator;
import org.shashank.basics.behavioral_patterns.iterator.mobiles.AndroidMobile;
import org.shashank.basics.behavioral_patterns.iterator.mobiles.Mobile;

import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        AndroidMobile mobile = new AndroidMobile();
        setup(mobile);

        iterateApplication(mobile);
    }

    private static void iterateApplication(AndroidMobile mobile) {
        AppIterator iterator = mobile.getIterator();
        while (iterator.hasNext()) {
            Application app = iterator.getNext();
            System.out.println("Found app: " + app.getAppName() + " occupying " + app.getAppSize() + " MB");
        }
    }

    private static void setup(AndroidMobile androidMobile) {
        List<Application> apps = getApplications();
        for (Application app: apps) {
            androidMobile.installApplication(app);
        }
    }

    private static List<Application> getApplications() {
        List<Application> apps = new ArrayList<>();
        apps.add(new Application("Insta", 566));
        apps.add(new Application("Wikipedia", 30));
        apps.add(new Application("Facebook", 900));
        apps.add(new Application("CoD", 3000));
        return apps;
    }
}
