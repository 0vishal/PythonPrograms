

public class MoodAnalyse {

    private String message;

    public MoodAnalyse(String message) {
        this.message = message;
    }

    public String analyseMood() {
        try {

            if (message.contains("sad")) {
                return "Sad";
            } else {
                return "Happy";
            }
        } catch (NullPointerException e) {
            System.out.println("incorrect input" + e);
        }

    }
}
