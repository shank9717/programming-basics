package org.shashank.basics.behavioral_patterns.chain_of_responsibility.server;

import org.shashank.basics.behavioral_patterns.chain_of_responsibility.interceptors.Interceptor;

public class Server {

    private Interceptor interceptor;

    public void setInterceptor(Interceptor interceptor) {
        this.interceptor = interceptor;
    }

    public boolean login(String username, String password) {
        if (interceptor.validate(username, password)) {
            System.out.println("Logged in as user: " + username);
            return true;
        }
        return false;
    }
}
