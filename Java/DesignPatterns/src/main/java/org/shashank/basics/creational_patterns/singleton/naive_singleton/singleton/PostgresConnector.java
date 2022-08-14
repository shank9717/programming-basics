package org.shashank.basics.creational_patterns.singleton.naive_singleton.singleton;

public final class PostgresConnector {
    private static PostgresConnector instance;
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

    public void connect() {
        System.out.println("Connected to DB with URL: " + this.url);
    }

    public static PostgresConnector getInstance(String username, String password, String url) {
        if (instance == null) {
            instance = new PostgresConnector(username, password, url);
        }
        return instance;
    }
}