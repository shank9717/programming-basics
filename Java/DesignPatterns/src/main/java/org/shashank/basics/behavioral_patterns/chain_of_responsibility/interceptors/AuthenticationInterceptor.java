package org.shashank.basics.behavioral_patterns.chain_of_responsibility.interceptors;

import org.shashank.basics.behavioral_patterns.chain_of_responsibility.users.UserRepository;

public class AuthenticationInterceptor extends Interceptor {
    private final UserRepository user;

    public AuthenticationInterceptor(UserRepository user) {
        this.user = user;
    }

    @Override
    public boolean validate(String username, String password) {
        if (!user.containsUsername(username)) {
            System.out.println("Username does not exist");
            return false;
        }
        if (!user.validatePassword(username, password)) {
            System.out.println("Wrong password!");
            return false;
        }
        return validateNext(username, password);
    }

}
