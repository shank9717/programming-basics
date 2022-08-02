/*
    Factory method is a creational design pattern which solves the problem of creating product objects
    without specifying their concrete classes.
 */
package org.shashank.basics.creational_patterns.factory_method;

import org.shashank.basics.creational_patterns.factory_method.apps.App;
import org.shashank.basics.creational_patterns.factory_method.mobiles.AndroidMobile;
import org.shashank.basics.creational_patterns.factory_method.mobiles.IOSMobile;
import org.shashank.basics.creational_patterns.factory_method.mobiles.Mobile;

public class Main {
    static Mobile mobile;

    public static void main(String[] args) {
        configure();
        App app = createApplication();
        runApplication(app);
    }


    static void configure() {
        String osType = System.getProperty("os.type");
        if (osType != null && osType.equals("Android")) {
            mobile = new AndroidMobile();
        } else {
            mobile = new IOSMobile();
        }
        mobile.start();
    }

    private static App createApplication() {
        return mobile.createApp();
    }

    private static void runApplication(App app) {
        app.runApp();
    }
}
