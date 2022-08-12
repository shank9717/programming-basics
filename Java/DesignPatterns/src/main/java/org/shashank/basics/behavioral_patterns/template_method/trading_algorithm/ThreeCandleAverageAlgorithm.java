package org.shashank.basics.behavioral_patterns.template_method.trading_algorithm;

import java.util.Arrays;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

public class ThreeCandleAverageAlgorithm extends TradingAlgorithm {

    @Override
    boolean getBuyOrSell(Integer currentPrice, LinkedList<Integer> lastFivePrices) {
        assert lastFivePrices.size() == 5;
        List<Object> lastThreePrices = Arrays.asList(lastFivePrices.toArray()).subList(2, 5);
        Integer sum = lastThreePrices.parallelStream().map(num -> (Integer) num).reduce(0, Integer::sum);
        Double average = sum / 3d;

        System.out.println("3 candle average is : " + average);

        return currentPrice > average;
    }

    @Override
    public String getAlgorithmName() {
        return "3 Candle Average Algorithm";
    }
}