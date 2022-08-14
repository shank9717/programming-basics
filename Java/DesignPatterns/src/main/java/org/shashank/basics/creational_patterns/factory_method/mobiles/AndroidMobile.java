/*
    This is a concrete implementation of base factory class
 */
package org.shashank.basics.creational_patterns.factory_method.mobiles;

import org.shashank.basics.creational_patterns.factory_method.apps.App;
import org.shashank.basics.creational_patterns.factory_method.apps.AndroidApp;

public class AndroidMobile extends Mobile {
    @Override
    public App createApp() {
        return new AndroidApp();
    }
}
