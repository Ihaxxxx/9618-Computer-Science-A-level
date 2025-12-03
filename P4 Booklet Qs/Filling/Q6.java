import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;

public class Q6 {
    public static Integer[] DataArray = new Integer[25] ; 
    public static void main(String[] args) {
        Integer Counter = 0 ;

        String filePath = "P4 Booklet Qs/Filling/Text Files - P4/Data.txt" ;
        
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

        // for (Integer valInteger : DataArray) {
        //     System.out.println(valInteger);
        // }

        // PrintArray();

        System.out.println(LinearSearch(12));
    }

    public static void PrintArray(){
        String data = "" ;
        for (Integer integer : DataArray) {
            data = data + Integer.toString(integer) + " " ;
        }
        System.out.println(data);
    }

    public static Integer LinearSearch(Integer ValueToFInd){
        Integer TimesFound = 0 ;
        for (Integer integer : DataArray) {
            if (integer == ValueToFInd) {
                TimesFound++ ;
            }
        }

        return TimesFound ;
    }
}
