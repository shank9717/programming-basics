package org.shashank.basics.behavioral_patterns.iterator.iterators;

import org.shashank.basics.behavioral_patterns.iterator.app.Application;
import org.shashank.basics.behavioral_patterns.iterator.mobiles.AndroidMobile;

import java.util.ArrayList;
import java.util.List;

public class AndroidAppIterator implements AppIterator {
    private final AndroidMobile mobile;
    private int idx = 0;
    private final List<String> appNames = new ArrayList<>();
    private final List<Application> applications = new ArrayList<>();

    public AndroidAppIterator(AndroidMobile mobile) {
        this.mobile = mobile;
    }

    private void lazyLoadDetails() {
        if (appNames.size() == 0) {
            List<String> appNames = mobile.getAppNames();
            for (String appName : appNames) {
                this.appNames.add(appName);
                this.applications.add(null);
            }
        }
    }

    @Override
    public boolean hasNext() {
        lazyLoadDetails();
        return idx < appNames.size();
    }

    @Override
    public Application getNext() {
        if (!hasNext()) {
            return null;
        }

        Application application = mobile.getApp(appNames.get(idx));
        applications.set(idx, application);
        idx++;
        return application;
    }

    @Override
    public void reset() {
        idx = 0;
    }
}