/*
    Abstract Factory is a creational design pattern, which solves the problem of creating
    entire product families without specifying their concrete classes.
 */
package org.shashank.basics.creational_patterns.abstract_factory;

import org.shashank.basics.creational_patterns.abstract_factory.mobiles.AndroidMobileFactory;
import org.shashank.basics.creational_patterns.abstract_factory.mobiles.IOSMobileFactory;
import org.shashank.basics.creational_patterns.abstract_factory.mobiles.MobileFactory;

public class Main {

    static MobileFactory factory = null;

    public static void main(String[] args) {
        configure();
        Mobile mobile = getMobile();
        runApplication(mobile);
    }


    static void configure() {
        String osType = System.getProperty("os.type");
        if (osType != null && osType.equals("Android")) {
            factory = new AndroidMobileFactory();
        } else {
            factory = new IOSMobileFactory();
        }
    }

    private static Mobile getMobile() {
        Mobile mobile = new Mobile(factory);
        mobile.start();
        return mobile;
    }

    private static void runApplication(Mobile mobile) {
        mobile.openApp();
    }
}
