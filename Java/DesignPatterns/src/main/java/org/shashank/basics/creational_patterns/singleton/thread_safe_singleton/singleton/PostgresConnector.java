package org.shashank.basics.creational_patterns.singleton.thread_safe_singleton.singleton;

public class PostgresConnector {
    // Volatile is used here to ensure double-checking lock works fine.
    private static volatile PostgresConnector instance;

    public String username;
    public String password;
    public String url;

    private PostgresConnector(String username, String password, String url) {
        try {
            Thread.sleep(1000);
        } catch (InterruptedException ex) {
            ex.printStackTrace();
        }
        this.username = username;
        this.password = password;
        this.url = url;
    }

    public static PostgresConnector getInstance(String username, String password, String url) {
        // Although result variable may seem useless, it is mandatory in the double-checked lock
        PostgresConnector result = instance;
        if (result != null) {
            return result;
        }
        synchronized(PostgresConnector.class) {
            if (instance == null) {
                instance = new PostgresConnector(username, password, url);
            }
            return instance;
        }
    }
}
