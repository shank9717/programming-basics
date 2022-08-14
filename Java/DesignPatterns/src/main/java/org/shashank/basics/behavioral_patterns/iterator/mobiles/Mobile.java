/*
    This is the base factory class
 */
package org.shashank.basics.behavioral_patterns.iterator.mobiles;

import org.shashank.basics.behavioral_patterns.iterator.app.Application;
import org.shashank.basics.behavioral_patterns.iterator.iterators.AppIterator;

import java.util.List;

public interface Mobile {
    List<String> getAppNames();
    Application getApp(String appName);

    AppIterator getIterator();
}
