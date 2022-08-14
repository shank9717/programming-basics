package org.shashank.basics.creational_patterns.prototype.vehicles;

public abstract class Vehicle {
    public String color;
    public int wheels;

    Vehicle() {
    }

    Vehicle(Vehicle vehicle) {
        if (vehicle != null) {
            this.color = vehicle.color;
            this.wheels = vehicle.wheels;
        }
    }

    public abstract Vehicle clone();

    @Override
    public boolean equals(Object object2) {
        if (!(object2 instanceof Vehicle)) return false;
        Vehicle vehicle2 = (Vehicle) object2;
        return vehicle2.color.equals(this.color) && (vehicle2.wheels == this.wheels);
    }
}
