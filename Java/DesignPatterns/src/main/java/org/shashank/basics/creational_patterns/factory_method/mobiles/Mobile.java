/*
    This is the base factory class
 */
package org.shashank.basics.creational_patterns.factory_method.mobiles;

import org.shashank.basics.creational_patterns.factory_method.apps.App;

public abstract class Mobile {
    public void start() {
        System.out.println("Turning on mobile...");
    }

    public abstract App createApp();
}
