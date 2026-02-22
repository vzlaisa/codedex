import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Enter text to encrypt: ");
        String inputText = scanner.nextLine();

        System.out.println("Enter shift key (0-25): ");
        int shiftKey = scanner.nextInt();

        CaesarCipher caesarCipher = new CaesarCipher();
        String encrypted = caesarCipher.encrypt(inputText, shiftKey);
        System.out.println("Encrypted text: " + encrypted);

        scanner.close();
    }
}
