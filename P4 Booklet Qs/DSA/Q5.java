public class Q5 {
    public static Integer[][] Jobs = new Integer[100][2];
    public static Integer NumberOfJobs;

    public static void main(String[] args) {
        Initialise();
        AddJob(12, 10);
        AddJob(526, 9);
        AddJob(33, 8);
        AddJob(12, 9);
        AddJob(78, 1);

        // for (Integer[] Jobs : Jobs) {
        // for (Integer Job : Jobs) {
        // System.out.println(Job);
        // }
        // }

        InsertionSort();
        PrintArray();
    }

    public static void Initialise() {
        NumberOfJobs = 0;

        for (int i = 0; i < Jobs.length; i++) {
            for (int j = 0; j < 2; j++) {
                Jobs[i][j] = -1;
            }
        }
    }

    public static void AddJob(int JobNumber, int priority) {
        boolean inserted = false;
        for (int i = 0; i < Jobs.length; i++) {
            if (Jobs[i][0] == -1) {
                Jobs[i][0] = JobNumber;
                Jobs[i][1] = priority;
                inserted = true;
                NumberOfJobs = NumberOfJobs + 1;
                break;
            }
        }

        if (inserted) {
            System.out.println("Added");
        } else {
            System.out.println("Not Added");
        }
    }

    public static void InsertionSort() {
        Integer DataToInsertPriority;
        Integer DataToInsertJobNumber;
        Integer NextValue;
        for (int count = 1; count < NumberOfJobs; count++) {
            DataToInsertPriority = Jobs[count][1];
            DataToInsertJobNumber = Jobs[count][0];
            NextValue = count - 1;
            while (NextValue >= 0 && Jobs[NextValue][1] > DataToInsertPriority) {
                Jobs[NextValue + 1][1] = Jobs[NextValue][1];
                Jobs[NextValue + 1][0] = Jobs[NextValue][0];

                NextValue = NextValue - 1;
            }

            Jobs[NextValue + 1][1] = DataToInsertPriority;
            Jobs[NextValue + 1][0] = DataToInsertJobNumber;
        }
    }

    public static void PrintArray() {
        for (int i = 0; i < NumberOfJobs; i++) {
            System.out.printf("%d Priority %d \n", Jobs[i][0], Jobs[i][1]);
        }
    }
}
