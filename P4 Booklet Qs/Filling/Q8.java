import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;

public class Q8 {
    public static String[] Name = new String[11] ;
    public static Integer[] Score = new Integer[11] ;

    public static void main(String[] args) {
        ReadHighScores();
        OutputHighScores();
    }

    public static void ReadHighScores(){
        Integer Counter = 0 ;
        String filePath = "P4 Booklet Qs/Filling/Text Files - P4/HighScore.txt" ;

        try (BufferedReader reader = new BufferedReader(new FileReader(filePath))){
            String name ;
            Integer score ;

            while ((name = reader.readLine()) != null && (score = Integer.parseInt(reader.readLine())) != null) {
                Name[Counter] = name ;
                Score[Counter] = score ;
                Counter++ ;
            }            

        } catch (FileNotFoundException e) {
            System.out.println("File not found");
        }catch (IOException e) {
            System.out.println("Something Went Wrong");
        }
    }


    public static void OutputHighScores(){
        for (int i = 0; i < Name.length; i++) {
            System.out.printf("%s %d \n" , Name[i],Score[i]);
        }
    }
}