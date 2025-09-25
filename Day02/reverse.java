public class reverse {
  public static void main(String[] args) {
    int num = 789796;
    while (num != 0) {
      System.out.print(num % 10);
      num = num / 10;
    }
  }
}