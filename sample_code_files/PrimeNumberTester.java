import java.util.Scanner;
/**
 * Inputs a range of numbers and outputs the range of prime 
 * numbers within that range from PrimeNumberGenerator.java
 * @author Cole Current
 * @version 5/12/2020
 */
public class PrimeNumberTester
{
    public static void main(String[] args)
    {
        //Declare Scanner
        Scanner in = new Scanner(System.in);
        
        //Declare Object
        PrimeNumberGenerator prime = new PrimeNumberGenerator();
        
        //Ask user for lows and highs
        System.out.println("  Welcome to the Prime Number Generator");
        System.out.println("<><><><><><><><><><><><><><><><><><><><><>");
        System.out.println("First you have to enter range of numbers");
        System.out.print("Please enter the low value: ");
        int low = in.nextInt();
        System.out.print("Please enter the high value: ");
        int high = in.nextInt();
        
        //Outputs all prime numbers within range
        System.out.println("All prime numbers between " + low + " and " + high + ".");
        System.out.println(prime.findPrimes(low, high));
        System.out.println("<><><><><><><><><><><><><><><><><><><><><>");
    }
}
