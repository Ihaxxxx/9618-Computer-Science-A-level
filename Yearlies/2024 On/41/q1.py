def ReadData():
    DataArray = []
    try:
        myFile = open('Yearlies/2024 MJ/43/Data.txt','r')
        info = myFile.readline().strip()
        while info != "" :
            DataArray.append(info)
            info = myFile.readline().strip()
        myFile.close()    
        return DataArray      
    except:
        print("No file found")  

def FormatArray(array):
    string = ""
    for item in array:
        string += item + " "
    return string

x = ReadData()
# print(FormatArray(x))   


def CompareString(str1,str2):
    found = False
    index = 0
    while found == False:
        if str1[index] < str2[index]:
            return 1
        elif str1[index] > str2[index]:
            return 2 
        else:
            index += 1

def bubble(array):
    for x in range(len(array)-1):
        for y in range(len(array)-1-x):
            result = CompareString(array[y],array[y+1])
            if result == 2 :
                temp = array[y]
                array[y] = array[y+1]
                array[y+1] = temp
    return array



sortedarray = bubble(x) 
print(FormatArray(sortedarray))           