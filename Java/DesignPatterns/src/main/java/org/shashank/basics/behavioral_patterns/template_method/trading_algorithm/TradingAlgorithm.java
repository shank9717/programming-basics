package org.shashank.basics.behavioral_patterns.template_method.trading_algorithm;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

public abstract class TradingAlgorithm {

    LinkedList<Integer> lastFivePrices;

    protected TradingAlgorithm() {
        getPriceHistory();
    }

    private void getPriceHistory() {
        lastFivePrices = new LinkedList<>();
        lastFivePrices.add(80);
        lastFivePrices.add(81);
        lastFivePrices.add(90);
        lastFivePrices.add(92);
        lastFivePrices.add(91);
    }

    private int getCurrentPrice() {
        return 87;
    }

    // Main algorithm
    public void placeOrder() {
        System.out.println("Last 5 prices: 80, 81, 90, 92, 91");
        // Get price
        Integer currentPrice = getCurrentPrice();
        System.out.println("Current price: " + currentPrice);

        // Check which type of order to place
        boolean buyOrder = getBuyOrSell(currentPrice, lastFivePrices);

        placeOrder(buyOrder);
    }

    private void placeOrder(boolean buyOrder) {
        if (buyOrder) {
            System.out.println("Placing buy order...");
        } else {
            System.out.println("Placing sell order...");
        }
    }

    abstract boolean getBuyOrSell(Integer currentPrice, LinkedList<Integer> lastFivePrices);

    public abstract String getAlgorithmName();
}
