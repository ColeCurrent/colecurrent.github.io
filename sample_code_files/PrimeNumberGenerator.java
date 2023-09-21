import java.util.ArrayList;
/**
 * Outputs all prime numbers within a given range
 *
 * @author Cole Current
 * @version 5/12/2020
 */
public class PrimeNumberGenerator{
    public static ArrayList<Integer> findPrimes(int low, int high){
        ArrayList<Integer> primes = new ArrayList<Integer>();
        
        //Loops through entire range of given numbers
        for(int i = low; i < high; i++){
           boolean prime = true;
        
           int j = 2;
           while(j <= i/2){
                //Checks if current index is a prime number
                if(i % j == 0){
                    prime = false;
                    j += i;
                }
                j++;
            } 
            //If number is prime add to array of prime numbers
            if(prime) 
            {
                primes.add(i);
            }
        }
        //Return full array of prime numbers
        return primes;
    }
}
