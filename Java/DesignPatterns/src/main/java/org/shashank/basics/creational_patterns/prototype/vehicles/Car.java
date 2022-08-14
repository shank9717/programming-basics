package org.shashank.basics.creational_patterns.prototype.vehicles;

public class Car extends Vehicle {
    public String carType;

    public Car() {
        this.wheels = 4;
    }

    Car(Car car) {
        super(car);
        this.carType = car.carType;
    }

    @Override
    public Vehicle clone() {
        return new Car(this);
    }

    @Override
    public boolean equals(Object object2) {
        if (!(object2 instanceof Car) || !(super.equals(object2))) {
            return false;
        }
        Car car2 = (Car) object2;
        return car2.carType.equals(this.carType);
    }

    @Override
    public String toString() {
        return "Car{" +
                "carType='" + carType + '\'' +
                ", color='" + color + '\'' +
                ", wheels=" + wheels +
                '}';
    }
}
