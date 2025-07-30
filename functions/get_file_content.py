import os
def get_file_content(working_directory, file_path):
    
    new_path = os.path.join(working_directory, file_path)
    
    working_directory_abs=os.path.abspath(working_directory)
    new_path_abs=os.path.abspath(new_path)

    # Check if the resulting path stays within working_directory
    if os.path.commonpath([working_directory_abs]) != os.path.commonpath([working_directory_abs, new_path_abs]):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

    if not os.path.isfile(new_path):
        print('try')
        print(new_path_abs)
        return f'Error: File not found or is not a regular file: "{file_path}"'
    
    MAX_CHARS = 10000

    try:

        with open(new_path_abs, "r") as f:
            file_content_string = f.read(MAX_CHARS) + f'[...File "{file_path}" truncated at 10000 characters]'
        return file_content_string
    except:
        return 'Error: something went wrong when we tried to open the file'
