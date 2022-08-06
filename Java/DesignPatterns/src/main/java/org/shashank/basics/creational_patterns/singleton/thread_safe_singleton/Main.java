package org.shashank.basics.creational_patterns.singleton.thread_safe_singleton;

import org.shashank.basics.creational_patterns.singleton.thread_safe_singleton.singleton.PostgresConnector;

public class Main {
    public static void main(String[] args) {
        testMultiThread();
    }

    private static void testMultiThread() {
        Thread threadFoo = new Thread(new ThreadFoo());
        Thread threadBar = new Thread(new ThreadBar());
        threadFoo.start();
        threadBar.start();
    }

    static class ThreadFoo implements Runnable {
        @Override
        public void run() {
            PostgresConnector db1 = PostgresConnector.getInstance("foo", "foo", "foo");
            System.out.println("Multi threaded, db1 URL: " + db1.url);
        }
    }

    static class ThreadBar implements Runnable {
        @Override
        public void run() {
            PostgresConnector db2 = PostgresConnector.getInstance("bar", "var", "bar");
            System.out.println("Multi threaded, db2 URL: " + db2.url);
        }
    }
}



