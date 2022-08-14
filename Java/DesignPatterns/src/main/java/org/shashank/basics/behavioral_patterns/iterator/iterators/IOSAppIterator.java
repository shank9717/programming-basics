package org.shashank.basics.behavioral_patterns.iterator.iterators;

import org.shashank.basics.behavioral_patterns.iterator.app.Application;
import org.shashank.basics.behavioral_patterns.iterator.mobiles.IOSMobile;

import java.util.ArrayList;
import java.util.List;

public class IOSAppIterator implements AppIterator {
    private final IOSMobile mobile;
    private int idx = 0;
    private final List<String> appNames = new ArrayList<>();
    private final List<Application> applications = new ArrayList<>();

    public IOSAppIterator(IOSMobile mobile) {
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