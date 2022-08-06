package org.shashank.basics.creational_patterns.singleton.naive_singleton;

import org.shashank.basics.creational_patterns.singleton.naive_singleton.singleton.PostgresConnector;


public class Main {
    public static void main(String[] args) {
        testMultiThread();
        testSingleThread();
    }

    private static void testMultiThread() {
        Thread threadFoo = new Thread(new ThreadFoo());
        Thread threadBar = new Thread(new ThreadBar());
        threadFoo.start();
        threadBar.start();
    }

    private static void testSingleThread() {
        PostgresConnector db1 = PostgresConnector.getInstance("foo", "foo", "foo");
        PostgresConnector db2 = PostgresConnector.getInstance("bar", "bar", "bar");
        System.out.println("Single threaded, db1 URL: " + db1.url);
        System.out.println("Single threaded, db2 URL: " + db2.url);
    }

    static class ThreadFoo implements Runnable {
        @Override
        public void run() {
            // Due to delay in init, getInstance will fetch new object
            PostgresConnector db1 = PostgresConnector.getInstance("foo", "foo", "foo");
            System.out.println("Multi threaded, db1 URL: " + db1.url);
        }
    }

    static class ThreadBar implements Runnable {
        @Override
        public void run() {
            // Due to delay in init, getInstance will fetch new object
            PostgresConnector db2 = PostgresConnector.getInstance("bar", "var", "bar");
            System.out.println("Multi threaded, db2 URL: " + db2.url);
        }
    }
}


