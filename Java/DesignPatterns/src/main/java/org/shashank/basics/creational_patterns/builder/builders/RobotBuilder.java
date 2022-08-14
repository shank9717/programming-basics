package org.shashank.basics.creational_patterns.builder.builders;

import org.shashank.basics.creational_patterns.builder.robots.Robot;
import org.shashank.basics.creational_patterns.builder.robots.RobotType;

public class RobotBuilder implements Builder {
    private RobotType type;
    private String name;
    private int sensorCount;

    @Override
    public RobotBuilder setRobotType(RobotType type) {
        this.type = type;
        return this;
    }

    @Override
    public RobotBuilder setRobotName(String name) {
        this.name = name;
        return this;
    }

    @Override
    public RobotBuilder setSensorCount(int sensorCount) {
        this.sensorCount = sensorCount;
        return this;
    }

    public Robot get() {
        return new Robot(type, name, sensorCount);
    }
}
