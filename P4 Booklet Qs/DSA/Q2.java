public class Q2 {
    static String[] Animals = new String[10];        
    public static void main(String[] args) {
        Animals[0] = "horse";
        Animals[1] = "lion";
        Animals[2] = "rabbit";
        Animals[3] = "mouse";
        Animals[4] = "bird";
        Animals[5] = "deer";
        Animals[6] = "whale";
        Animals[7] = "elephant";
        Animals[8] = "kangaroo";
        Animals[9] = "tiger";

        SortDescending();

        for (String string : Animals) {
            System.out.println(string);
        }
    }

    public static void SortDescending(){
        Integer ArrayLength ;
        String Temp ;
        ArrayLength = Animals.length ;
        for (int x = 0; x < ArrayLength - 1; x++) {
            for (int y = 0; y < ArrayLength-  2 ; y++) {
                if (Animals[y].charAt(0) < (Animals[y + 1].charAt(0))) {
                    Temp = Animals[y];
                    Animals[y] = Animals[y+1];
                    Animals[y+1] = Temp ;
                }        
           }
        }
    }
}
