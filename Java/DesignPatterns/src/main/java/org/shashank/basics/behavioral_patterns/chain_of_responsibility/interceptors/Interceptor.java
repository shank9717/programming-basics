package org.shashank.basics.behavioral_patterns.chain_of_responsibility.interceptors;

public abstract class Interceptor {
    private Interceptor next;

    public static Interceptor link(Interceptor first, Interceptor... chain) {
        Interceptor head = first;
        Interceptor nextInterceptor = head;
        for (Interceptor nextInChain: chain) {
            nextInterceptor.next = nextInChain;
            nextInterceptor = nextInChain;
        }
        return head;
    }

    public abstract boolean validate(String username, String password);

    protected boolean validateNext(String username, String password) {
        if (next == null) {
            return true;
        }
        return next.validate(username, password);
    }

}
