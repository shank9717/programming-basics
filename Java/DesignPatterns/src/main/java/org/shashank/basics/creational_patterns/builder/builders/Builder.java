package org.shashank.basics.creational_patterns.builder.builders;

import org.shashank.basics.creational_patterns.builder.robots.RobotType;

public interface Builder {
    Builder setRobotType(RobotType type);

    Builder setRobotName(String name);

    Builder setSensorCount(int sensorCount);
}
