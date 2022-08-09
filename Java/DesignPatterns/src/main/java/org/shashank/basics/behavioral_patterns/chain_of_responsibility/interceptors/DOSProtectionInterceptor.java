package org.shashank.basics.behavioral_patterns.chain_of_responsibility.interceptors;

public class DOSProtectionInterceptor extends Interceptor {
    private final int maxRequestsPerSecond;
    private int request;

    private long lastRequestTime = -1;

    public DOSProtectionInterceptor(int maxRequestsPerSecond) {
        this.maxRequestsPerSecond = maxRequestsPerSecond;
    }

    public boolean validate(String username, String password) {
        if (lastRequestTime == -1 ||
                System.currentTimeMillis() > lastRequestTime + 1000) {
            request = 0;
            lastRequestTime = System.currentTimeMillis();
        }

        request++;

        if (request > maxRequestsPerSecond) {
            System.out.println("Too many requests, wait for some time");
            return false;
        }
        return validateNext(username, password);
    }
}
