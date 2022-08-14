package org.shashank.basics.behavioral_patterns.template_method;

import org.shashank.basics.behavioral_patterns.template_method.trading_algorithm.*;

import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        List<TradingAlgorithm> algorithms = new ArrayList<>();
        algorithms.add(new SimpleTradingAlgorithm());
        algorithms.add(new ThreeCandleAverageAlgorithm());
        algorithms.add(new FiveCandleAverageAlgorithm());
        algorithms.add(new ComplexAlgorithm());
        for (TradingAlgorithm algorithm: algorithms) {
            System.out.println("Executing algorithm: " + algorithm.getAlgorithmName() + "\n");
            algorithm.placeOrder();
            System.out.println("\n");
        }
    }
}
