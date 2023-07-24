import io.github.bonigarcia.wdm.WebDriverManager;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.firefox.FirefoxDriver;

    public class HelloSelenium {


        public void main(String[] args) {
            //Disable Driver logging
            System.setProperty(FirefoxDriver.SystemProperty.BROWSER_LOGFILE, "/dev/null");
            // Set up the Firefox driver(GeckoDriver)
            WebDriverManager.firefoxdriver().setup();

            // Create a new instance of the Firefox driver
            WebDriver driver = new FirefoxDriver();

            // Open the browser
            driver.get("https://training-support.net");

            // Perform testing and asser
            driver.quit();
        }
}
