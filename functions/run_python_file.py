import os
'''
in terms of saifty this is not safe, this program is my personal 
project use to learn the basics do not use this seriously it 
could destroy your compuer, but if you are doing simple tasks
it shuld be fine solong as it stays confine
'''

def run_python_file(working_directory, file_path, args=[]):
   
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

