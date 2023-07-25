package stepDefinition;

import org.junit.runner.RunWith;
import io.cucumber.junit.Cucumber;
import io.cucumber.junit.CucumberOptions;

@RunWith(Cucumber.class)
@CucumberOptions(
        features = "C:\\Users\\00850Z744\\IdeaProjects\\M1-May23-M3-Cucumber\\features",
        glue = {"stepDefinitions"},
        tags = "@activity1"
        // tags = "@activity2"
        //tags = "@activity3"
        //tags = "@activity4"
        //tags = "@activity5"
        /* tags = "@SmokeTest",
         plugin = {"pretty"},
         monochrome = true */
        /*tags = "@SmokeTest",
        plugin = {"html: test-reports"},
        monochrome = true */
        /*tags = "@SimpleAlert",
    plugin = {"pretty"},
    monochrome = true*/
        /*tags = "@SimpleAlert",
        plugin = {"json: test-reports/json-report.json"},
        monochrome = true*/
)

public class ActivitiesRunner {
}
