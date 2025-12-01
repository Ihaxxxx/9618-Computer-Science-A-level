import java.util.Random;

public class Q4 {
    static Integer[][] MyArray = new Integer[10][10];

    public static void main(String[] args) {
        Random random = new Random();

        for (int i = 0; i < 10; i++) {
            for (int j = 0; j < 10; j++) {
                MyArray[i][j] = random.nextInt(100);
            }
        }


        // Integer ArrayLength = 10;

        for (int x = 0; x < args.length - 1; x++) {
            for (int y = 0; y < args.length - 2; y++) {
                for (int z = 0; z < args.length - y - 2; z++) {
                    if (MyArray[x][z] > MyArray[x][z + 1]) {
                        Integer tempValue = MyArray[x][z];
                        MyArray[x][z] = MyArray[x][z + 1];
                        MyArray[x][z + 1] = tempValue;
                    }
                }
            }
        }

        System.out.println();
    }

    public static void PrintArray(Integer[][] theArray){
        String data ;
        for (int x = 0; x < theArray.length; x++) {
            data = "" ;
            for (int y = 0; y < theArray.length; y++) {
                data += theArray[x][y] ;
            }

            System.out.println(data);
        }
    }
}
