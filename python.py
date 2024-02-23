import os 
import shutil
from collections import defaultdict 

check_presence = defaultdict(None)
root_directory = os.getcwd()

def rename_file(file_info, directory, file_path): 
    i = 1
    
    while True:
        new_name = file_info[0] + "1" + "." + file_info[1]
        
        if new_name in check_presence:   
            i += 1
        else: 
            os.rename(file_path, directory + "/" + new_name)
            return new_name 
    return 
     
def get_file_extension(file_name): 
    file_info = file_name.rsplit('.', 1)
    return (file_info[0], file_info[1])

def depth_first_search(current_directory):
    contents = os.listdir(current_directory)
    
    for content in contents: 
        tmp_path = current_directory + "/" +  content
        
        if os.path.isdir(tmp_path): 
            depth_first_search(tmp_path)
        else: 
            file_info = get_file_extension(content)
            
            file_name = content
            # Check for the file's existance: 
            if content in check_presence: 
                file_name = rename_file(file_info, current_directory, tmp_path)
                
            if file_info[1] not in check_presence:  
               print(file_info[1])
               os.mkdir(root_directory + "/" + file_info[1])
               check_presence[file_info[1]] = 1
                    
            shutil.move(current_directory + "/" + file_name, root_directory + "/" + file_info[1])     
                    

                

depth_first_search(root_directory)


# 1. Make folders.
# 2. 
