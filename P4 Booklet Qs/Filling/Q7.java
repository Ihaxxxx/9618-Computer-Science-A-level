import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.Scanner;

public class Q7 {
    public static Integer[] DataArray = new Integer[100] ; 
    static Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {

        
        ReadFile();
        // for (Integer lineString : DataArray) {
        //     System.out.println(lineString);
        // }
        System.out.printf("The number 61 is found %d times" , FindValues(61));
    }

    public static void ReadFile(){
        String filePath = "P4 Booklet Qs/Filling/Text Files - P4/IntegerData.txt" ;
        Integer Counter = 0 ;
        try (BufferedReader reader = new BufferedReader(new FileReader(filePath))){
            String line ;
            while ((line = reader.readLine()) != null) {
                DataArray[Counter] = Integer.parseInt(line) ;
                Counter++ ;
            }
        } catch (FileNotFoundException e) {
            System.out.println("File not found");
        }catch (IOException e){
            System.out.println("Something Went Wrong");
        }
    }

    public static Integer FindValues(Integer ValueToFInd){
        Integer userInputIInteger ;
        System.out.print("Enter a number between 0 and 100 inclusive : ");
        userInputIInteger = scanner.nextInt();

        while (userInputIInteger < 0 && userInputIInteger > 100) {
            System.out.println("The Number input is incorrect pls re enter a number btw 0 and 100 : ");
            System.out.print("Enter a number between 0 and 100 inclusive : ");
            userInputIInteger = scanner.nextInt();
        }
        Integer TimesFound = 0 ;
        for (Integer integer : DataArray) {
            if (integer == ValueToFInd) {
                TimesFound++ ;
            }
        }

        return TimesFound ;
    }
}
