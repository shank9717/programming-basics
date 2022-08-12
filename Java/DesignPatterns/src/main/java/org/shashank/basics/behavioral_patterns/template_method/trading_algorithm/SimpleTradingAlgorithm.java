package org.shashank.basics.behavioral_patterns.template_method.trading_algorithm;

import java.util.LinkedList;
import java.util.Queue;

public class SimpleTradingAlgorithm extends TradingAlgorithm {

    @Override
    boolean getBuyOrSell(Integer currentPrice, LinkedList<Integer> lastFivePrices) {
        assert lastFivePrices.size() == 5;
        boolean buy = currentPrice > lastFivePrices.getLast();
        System.out.println("Current price is " + (buy ? "greater" : "less") + " than previous price");
        return buy;
    }

    @Override
    public String getAlgorithmName() {
        return "Simple Algorithm";
    }
}
