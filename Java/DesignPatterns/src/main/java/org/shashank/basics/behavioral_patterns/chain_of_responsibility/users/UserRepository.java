package org.shashank.basics.behavioral_patterns.chain_of_responsibility.users;

import java.util.HashMap;
import java.util.Map;

public class UserRepository {
    private final Map<String, String> users = new HashMap<>();

    public void register(String email, String password) {
        users.put(email, password);
    }

    public boolean containsUsername(String email) {
        return users.containsKey(email);
    }

    public boolean validatePassword(String email, String password) {
        return users.get(email).equals(password);
    }

}
