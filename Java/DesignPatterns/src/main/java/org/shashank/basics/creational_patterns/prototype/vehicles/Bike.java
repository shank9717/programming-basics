package org.shashank.basics.creational_patterns.prototype.vehicles;

public class Bike extends Vehicle {
    public String bikeType;

    public Bike() {
        this.wheels = 2;
    }

    Bike(Bike bike) {
        super(bike);
        this.bikeType = bike.bikeType;
    }

    @Override
    public Vehicle clone() {
        return new Bike(this);
    }

    @Override
    public boolean equals(Object object2) {
        if (!(object2 instanceof Bike) || !(super.equals(object2))) {
            return false;
        }
        Bike bike2 = (Bike) object2;
        return bike2.bikeType.equals(this.bikeType);
    }

    @Override
    public String toString() {
        return "Bike{" +
                "bikeType='" + bikeType + '\'' +
                ", color='" + color + '\'' +
                ", wheels=" + wheels +
                '}';
    }
}
