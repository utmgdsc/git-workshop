from file_actions import calc_sum_of_numbers_in_file
# made some change

# continue asking the user to enter a filename until they 
# terminate the program themselves or type "q".

enter_file_text_prompt = "Please enter the name of a file found in the directory \"./files\": "
file_name = input(enter_file_text_prompt)


while file_name != "q":
    try:
        result = calc_sum_of_numbers_in_file(file_name)
        print("The sum of the numbers in file {} is {}.\n\n".format(file_name, result))
    except Exception:
        print("There was an error opening/reading the file.\n\n")
        
    file_name = input(enter_file_text_prompt)
        
    




