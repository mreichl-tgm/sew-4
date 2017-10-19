package encryption;

public class Encryptor {
    private static String alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    private static String key = "BCDEFGHIJKLMNOPQRSTUVWXYZA";

    public static String encrypt(String message) {
        String encrypted = "";

        message = message.toUpperCase();

        for (int i = 0; i < message.length(); i++){
            char c = message.charAt(i);

            if (alphabet.indexOf(c) > -1) {
                encrypted += key.charAt(alphabet.indexOf(c));
            } else {
                encrypted += c;
            }
        }

        return encrypted;
    }

    public static String decrypt(String message) {
        String decrypted = "";

        message = message.toUpperCase();

        for (int i = 0; i < message.length(); i++){
            char c = message.charAt(i);

            if (key.indexOf(c) > -1) {
                decrypted += alphabet.charAt(key.indexOf(c));
            } else {
                decrypted += c;
            }
        }

        return decrypted;
    }
}
