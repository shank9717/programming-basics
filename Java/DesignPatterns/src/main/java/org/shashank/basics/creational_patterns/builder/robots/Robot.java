package org.shashank.basics.creational_patterns.builder.robots;

public class Robot {
    private final RobotType type;
    private final String name;
    private final int sensorCount;

    public Robot(RobotType type, String name, int sensorCount) {
        this.type = type;
        this.name = name;
        this.sensorCount = sensorCount;
    }

    public RobotType getType() {
        return type;
    }

    public String getName() {
        return name;
    }

    public int getSensorCount() {
        return sensorCount;
    }
}
