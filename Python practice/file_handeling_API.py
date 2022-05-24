# create a CRUD API for file handling
import os


def file_create(file_path, content):
    with open(file_path, 'w') as file_w_handle:
        file_w_handle.write(content)
def file_update(file_path, content):
    with open(file_path, 'a') as file_w_handle:
        file_w_handle.write(content + "\n")

        while True:
            content = input("Add more content and press enter")
            file_w_handle.write(content + "\n")
            choice_of_input = input("Any more content yes or no")
            if choice_of_input == 'no':
                break
def file_delete(file_path):
    is_file_exist = os.path.exists(file_path)
    if is_file_exist:
        print("file exist and will be deleted?")
        print("warning there is no recycle bin")
        answer = input("Do you really want this")
        if answer:
            os.remove(file_path)
    else:
        print("The file does not exist")
def file_read(file_path):
    try:
        with open(file_path, 'r') as file_w_handle:
            content = file_w_handle.read()
        return content
        
    except FileNotFoundError as fnfe:
        print(f"{fnfe} : The file will be created pls try again")
        file_create(file_path,content="Empty")

def CRUD(operation):
    if operation == "C":
        file_path = input("Enter path to file")
        content = input("Enter file content")
        file_create(file_path, content)
    elif operation == "R":
        file_path = input("Enter path to file")
        
        file_content = file_read(file_path)
        print(file_content)
    elif operation == "U":
        file_path = input("Enter path to file")
        content = input("Enter file content")
        file_update(file_path, content)
    elif operation == "D":
        file_path = input("Enter path to file")
        file_delete(file_path)
    else:
        print("Sorry Operation not yet supported")


# if the case is not import
# if we import __name_ == name of the file
# if we run the file directly __name_ == '__main__'
if __name__ == "__main__":
    operation_input = input("Enter your operation C, R, U, D")
    CRUD(operation_input)
