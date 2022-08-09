package org.shashank.basics.behavioral_patterns.chain_of_responsibility;

import org.shashank.basics.behavioral_patterns.chain_of_responsibility.interceptors.AuthenticationInterceptor;
import org.shashank.basics.behavioral_patterns.chain_of_responsibility.interceptors.DOSProtectionInterceptor;
import org.shashank.basics.behavioral_patterns.chain_of_responsibility.interceptors.Interceptor;
import org.shashank.basics.behavioral_patterns.chain_of_responsibility.server.Server;
import org.shashank.basics.behavioral_patterns.chain_of_responsibility.users.UserRepository;

import java.util.HashMap;
import java.util.LinkedHashMap;
import java.util.Map;

public class Main {
    public static void main(String[] args) throws InterruptedException {
        UserRepository users = new UserRepository();
        users.register("shank9717@gmail.com", "test123");
        users.register("adminUser@gmail.com", "admin123");
        users.register("johndoe@gmail.com", "john123");

        Interceptor interceptor = Interceptor.link(new DOSProtectionInterceptor(3), new AuthenticationInterceptor(users));

        Server server = new Server();

        server.setInterceptor(interceptor);

        Map<String, String> loginTrials = new LinkedHashMap<>();
        loginTrials.put("abc", "def");
        loginTrials.put("shank9717@gmail.com", "test123");
        loginTrials.put("johndoe@gmail.com", "test123");
        loginTrials.put("adminUser@gmail.com", "admin123");
        for (Map.Entry<String, String> logins: loginTrials.entrySet()) {
            System.out.println("Attempting to log in as user: " + logins.getKey());
            if (server.login(logins.getKey(), logins.getValue())) {
                System.out.println("Successful!");
            } else {
                System.out.println("Failed");
            }
        }

        System.out.println("Sleeping for 1 second and retrying...");
        Thread.sleep(1000);

        System.out.println("Attempting to log in as user: adminUser@gmail.com");

        if (server.login("adminUser@gmail.com", "admin123")) {
            System.out.println("Successful!");
        } else {
            System.out.println("Failed");
        }
    }
}
