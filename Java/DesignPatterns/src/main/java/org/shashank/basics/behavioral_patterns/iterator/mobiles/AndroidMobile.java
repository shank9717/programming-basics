package org.shashank.basics.behavioral_patterns.iterator.mobiles;


import org.shashank.basics.behavioral_patterns.iterator.app.Application;
import org.shashank.basics.behavioral_patterns.iterator.iterators.AndroidAppIterator;
import org.shashank.basics.behavioral_patterns.iterator.iterators.AppIterator;

import java.util.ArrayList;
import java.util.List;
import java.util.Optional;
import java.util.stream.Collectors;

public class AndroidMobile implements Mobile {
    private final String mobileType;

    List<Application> applications = new ArrayList<>();

    public AndroidMobile() {
        this.mobileType = "Android";
    }

    public void installApplication(Application application) {
        this.applications.add(application);
    }

    @Override
    public List<String> getAppNames() {
        return this.applications.stream().map(Application::getAppName).collect(Collectors.toList());
    }

    @Override
    public Application getApp(String appName) {
        Optional<Application> app = this.applications.stream()
                .filter(application -> application.getAppName().equals(appName))
                .findFirst();
        return app.orElse(null);
    }

    @Override
    public AppIterator getIterator() {
        return new AndroidAppIterator(this);
    }
}
