package org.shashank.basics.behavioral_patterns.strategy;

import org.shashank.basics.behavioral_patterns.strategy.apps.AndroidApp;
import org.shashank.basics.behavioral_patterns.strategy.apps.ChromeApp;
import org.shashank.basics.behavioral_patterns.strategy.apps.YoutubeApp;
import org.shashank.basics.behavioral_patterns.strategy.apps.YoutubeMusicApp;
import org.shashank.basics.behavioral_patterns.strategy.mobile.AndroidMobile;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class Main {
    private static final BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));

    public static void main(String[] args) throws IOException {
        String url1 = "https://music.youtube.com/watch?v=BG05dUhFeKM&list=RDAMVMBG05dUhFeKM";
        String url2 = "https://www.youtube.com/watch?v=opeETnB8m8w";

        visit(url1);
        visit(url2);
    }

    private static void visit(String url) throws IOException {
        AndroidMobile mobile = new AndroidMobile();
        List<AndroidApp> apps = getPossibleLinkVisitStrategies(url);
        String prompt = getOpenPrompt(apps, url);
        System.out.print(prompt);
        int choice = Integer.parseInt(reader.readLine());
        if (choice >= 1 && choice <= apps.size()) {
            AndroidApp app = apps.get(choice - 1);
            mobile.setApp(app);
            mobile.openHyperlink(url);
        }
    }

    private static String getOpenPrompt(List<AndroidApp> apps, String url) {
        StringBuilder prompt = new StringBuilder("\nPlease, select an app to open URL: " + url + "\n");
        int appIndex = 1;
        for (AndroidApp app: apps) {
            prompt.append(appIndex++).append(" - ").append(app.getAppName()).append("\n");
        }
        prompt.append("\nEnter number input: ");
        return prompt.toString();
    }

    private static List<AndroidApp> getPossibleLinkVisitStrategies(String url) {
        List<AndroidApp> apps = new ArrayList<>();
        apps.add(new ChromeApp());
        if (url.contains("youtube.com")) {
            apps.add(new YoutubeApp());
        }
        if (url.contains("music.youtube.com")) {
            apps.add(new YoutubeMusicApp());
        }
        return apps;
    }
}
