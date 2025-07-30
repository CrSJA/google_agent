import os

def get_files_info(working_directory, directory="."):
    # Compute path from working_directory and relative directory
    new_path = os.path.join(working_directory, directory)

    working_directory_abs=os.path.abspath(working_directory)
    new_path_abs=os.path.abspath(new_path)

    # Check if the resulting path stays within working_directory
    if os.path.commonpath([working_directory_abs]) != os.path.commonpath([working_directory_abs, new_path_abs]):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    # Check if it’s a real directory
    if not os.path.isdir(new_path):
        return f'Error: "{directory}" is not a directory'

    
    contents=os.listdir(new_path)

    temp= f'results for {directory}: \n'

    for element in contents:
        
        path_to_element=os.path.join(new_path,element)

        size_of_element=os.path.getsize(path_to_element)

        is_dir=os.path.isdir(path_to_element)

        result=f'- {element}: file_size={size_of_element} bytes, is_dir={is_dir}'
        temp+=result+'\n'


    return temp

