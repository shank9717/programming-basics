package org.shashank.basics.behavioral_patterns.template_method.trading_algorithm;

import java.util.LinkedList;
import java.util.Queue;

public class ComplexAlgorithm extends TradingAlgorithm {
    @Override
    boolean getBuyOrSell(Integer currentPrice, LinkedList<Integer> lastFivePrices) {
        boolean indicator = getIndicator(currentPrice, lastFivePrices);
        System.out.println("Indicator generated: " + indicator);
        return indicator;
    }

    private boolean getIndicator(Integer currentPrice, LinkedList<Integer> lastFivePrices) {
        // Some code to generate indicator based on historic data
        assert lastFivePrices.size() == 5;
        int lastPrice = lastFivePrices.peek();
        return Math.random() > (lastPrice - currentPrice) / 10d;
    }

    @Override
    public String getAlgorithmName() {
        return "Complex Algorithm";
    }
}
