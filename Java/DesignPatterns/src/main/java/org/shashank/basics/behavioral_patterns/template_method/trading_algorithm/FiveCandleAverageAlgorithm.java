package org.shashank.basics.behavioral_patterns.template_method.trading_algorithm;

import java.util.LinkedList;
import java.util.Queue;

public class FiveCandleAverageAlgorithm extends TradingAlgorithm {

    @Override
    boolean getBuyOrSell(Integer currentPrice, LinkedList<Integer> lastFivePrices) {
        assert lastFivePrices.size() == 5;
        Integer sum = lastFivePrices.parallelStream().reduce(0, Integer::sum);
        Double average = sum / 5d;

        System.out.println("5 candle average is : " + average);

        return currentPrice > average;
    }

    @Override
    public String getAlgorithmName() {
        return "5 Candle Average Algorithm";
    }
}
