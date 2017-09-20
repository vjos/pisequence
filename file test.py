import os

#MODES: r is read mode (default), w is write mode, a is append mode, r+ is read and write

directory = os.getcwd()

def save(string):
    directory_list = os.listdir(directory)
    next_free = 0
    number = ''
    
    for i in range(len(directory_list)):
        test_string = directory_list[i]
        for j in range(len(test_string)):
            if(test_string[j].isdigit()):
                number += test_string[j]

        if(number.isdigit()):        
            if(int(number) > next_free):
                next_free = int(number)

        number = ''

    next_free += 1
        
    file_name = ("sequence" + str(next_free) + ".txt")
    F = open(file_name, "w")
    F.write(string)
    F.close() 

def read(number):
    file_name = ("sequence" + str(number) + ".txt")
    F = open(file_name, "r")
    string = F.read()
    F.close()
    return string
    

for i in range(13):
    save("10010010")
