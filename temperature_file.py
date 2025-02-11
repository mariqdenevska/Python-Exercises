
import re
import os

#file_path = input("Enter a file path: ")
#file_name = input("Enter a file name: ")
file_path = r"C:\Users\Mariya.Karpacheva\OneDrive - Adastra, s.r.o\Documents\Python course"
file_name = r"temperature.txt"
path = file_path + "\\" + file_name 
new_file_path = file_path + r"\new_result.txt"


def convert_to_farenheit(temperature):
    converted_value = (temperature * 9/5) + 32
    return round(converted_value, 3)

#Truncate the new file if exist
if os.path.exists(new_file_path):
    with open(new_file_path, 'w') as clear_file:
        clear_file.write('')

with open(path,'r',encoding="utf-8") as file:   
    for row in file.readlines() :
        
        if re.search(r'C', row, re.IGNORECASE):
            value = re.sub(r'[a-zA-Z]', '', row)
            converted_value=convert_to_farenheit(float(value))
            f_value = str(converted_value) + 'F'
            print(f"Temperature: {f_value}")
            with open(new_file_path, 'a', encoding="utf-8") as new_file:
                new_file.write(f_value + "\n")

        else:
            with open(new_file_path, 'a', encoding="utf-8") as new_file:
                new_file.write(row + "\n")






