/*
    Director directs how various parameters are set in builders.
    It can control building different types of objects using the same builder
 */
package org.shashank.basics.creational_patterns.builder.director;

import org.shashank.basics.creational_patterns.builder.builders.Builder;
import org.shashank.basics.creational_patterns.builder.robots.RobotType;

public class RobotBuildingDirector {

    public void createSimpleRobot(Builder builder) {
        builder.setRobotType(RobotType.COMPUTER)
                .setRobotName("Computer")
                .setSensorCount(0);
    }

    public void createMechanicalRobot(Builder builder) {
        builder.setRobotType(RobotType.MECHANICAL)
                .setRobotName("FactoryRobot")
                .setSensorCount(3);
    }

    public void createHumanoidRobot(Builder builder) {
        builder.setRobotType(RobotType.HUMANOID)
                .setRobotName("Alex")
                .setSensorCount(8);
    }
}
