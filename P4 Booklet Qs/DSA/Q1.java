import java.util.Scanner;
public class Q1 {
    static Integer[] arrayData = new Integer[10] ;
    public static void main(String[] args) {
        
        Scanner scanner = new Scanner(System.in);

        arrayData[0] = 10;
        arrayData[1] = 5;
        arrayData[2] = 6;
        arrayData[3] = 7;
        arrayData[4] = 1;
        arrayData[5] = 12;
        arrayData[6] = 13;
        arrayData[7] = 15;
        arrayData[8] = 21;
        arrayData[9] = 8;
        
        // System.out.println(linearSearch(15));
        // Integer userInput ;
        // System.out.print("Enter a value to find : ");
        // userInput = scanner.nextInt();
        // scanner.nextLine();
        
        // if (linearSearch(userInput)) {
        //     System.out.printf("The value %d is present in the array",userInput);
        // }else{
        //     System.out.printf("The value %d is not present in the array",userInput);

        // }
        bubbleSort();

        // for (Integer numbInteger : arrayData) {
        //     System.out.println(numbInteger);
        // }


        



        scanner.close();
    }
    
    
    public static boolean linearSearch(Integer valueToFind){
        for (int i = 0; i < arrayData.length; i++) {
            if (arrayData[i].equals(valueToFind)) {
                return true ;
            }
        }
        return false ;
    }

    public static void bubbleSort(){
        Integer temp ;
        for (int i = 0; i < 10; i++) {
            for (int j = 0; j < 9 ; j++) {
                if (arrayData[j] > arrayData[j+1]) {
                    temp = arrayData[j];
                    arrayData[j] = arrayData[j+1];
                    arrayData[j+1] = temp;
                }
            }
        }
    }
}