public class Q3 {
    static Integer[] TheData = new Integer[9];

    public static void main(String[] args) {
        TheData[0] = 20;
        TheData[1] = 3;
        TheData[2] = 4;
        TheData[3] = 8;
        TheData[4] = 12;
        TheData[5] = 99;
        TheData[6] = 4;
        TheData[7] = 26;
        TheData[8] = 4;

        System.out.println("Before Sorting");
        PrintArray(TheData);
        InsertionSort(TheData);
        System.out.println("After Sorting");
        PrintArray(TheData);
    }



    public static void InsertionSort(Integer TheData[]){
        for (int count = 1 ; count < TheData.length; count++) {
            Integer DataToInsert = TheData[count];
            Integer Inserted = 0;
            Integer NextValue = count - 1 ;
            while (NextValue >= 0 && Inserted != 1) {
                if (DataToInsert < TheData[NextValue]) {
                    TheData[NextValue + 1] = TheData[NextValue];
                    NextValue = NextValue - 1;
                    TheData[NextValue + 1] = DataToInsert ;
                }else{
                    Inserted = 1 ;
                }
            }
        }
    }

    public static void PrintArray(Integer TheData[]){
        for (Integer integers : TheData) {
            System.out.println(integers);
        }
    }
}
