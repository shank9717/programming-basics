package org.shashank.basics.creational_patterns.prototype;

import org.shashank.basics.creational_patterns.prototype.vehicles.Bike;
import org.shashank.basics.creational_patterns.prototype.vehicles.Car;
import org.shashank.basics.creational_patterns.prototype.vehicles.Vehicle;

import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        List<Vehicle> vehicles = new ArrayList<>();
        List<Vehicle> vehiclesCopy = new ArrayList<>();

        Bike bike = new Bike();
        bike.color = "Blue";
        bike.bikeType = "Road bike";

        Car car = new Car();
        car.color = "Red";
        car.carType = "Sedan";

        Car car2 = new Car();
        car2.color = "Black";
        car2.carType = "Hatchback";

        vehicles.add(bike);
        vehicles.add(car);
        vehicles.add(car2);

        cloneVehicles(vehicles, vehiclesCopy);

        compareVehicles(vehicles, vehiclesCopy);
    }

    private static void compareVehicles(List<Vehicle> vehicles, List<Vehicle> vehiclesCopy) {
        for (int i = 0; i < vehicles.size(); i++) {
            if (vehicles.get(i) == vehiclesCopy.get(i)) {
                System.out.println("Vehicles are same objects");
            } else {
                System.out.println("Vehicles are not same objects");
            }
            if (vehicles.get(i).equals(vehiclesCopy.get(i))) {
                System.out.println("Vehicles are similar objects, with same properties");
                System.out.println("Vehicle 1: " + vehicles.get(i).toString());
                System.out.println("Vehicle 2: " + vehiclesCopy.get(i).toString());
            } else {
                System.out.println("Vehicles have different properties");
                System.out.println("Vehicle 1: " + vehicles.get(i).toString());
                System.out.println("Vehicle 2: " + vehiclesCopy.get(i).toString());
            }
        }
    }

    private static void cloneVehicles(List<Vehicle> vehicles, List<Vehicle> vehiclesCopy) {
        for (Vehicle vehicle: vehicles) {
            vehiclesCopy.add(vehicle.clone());
        }
    }
}
