import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

public class MoodAnalyseTest {

    @Test
    public void ReturnSad() {
        String message="I am sad";
        MoodAnalyse mood = new MoodAnalyse(message);
        String message1= mood.analyseMood();
        Assertions.assertEquals("Sad",message1);
    }

    @Test
    public void ReturnHappy() {
        String message="I am in any mood";
        MoodAnalyse mood = new MoodAnalyse(message);
        String message1= mood.analyseMood();
        Assertions.assertEquals("Happy",message1);
    }
}
