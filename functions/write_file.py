import os

def write_file(working_directory, file_path, content):
    
    new_path = os.path.join(working_directory, file_path)
    
    working_directory_abs=os.path.abspath(working_directory)
    new_path_abs=os.path.abspath(new_path)

    # Check if the resulting path stays within working_directory
    if os.path.commonpath([working_directory_abs]) != os.path.commonpath([working_directory_abs, new_path_abs]):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

    if not os.path.isfile(new_path):
        if os.path.exists(new_path):
            return f'Error: The path: "{file_path}" exist but is not a file'
    
    with open(new_path, "w") as f:
        f.write(content)
    return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'


