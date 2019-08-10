import os
def dir_list(rootp):
    for path in os.listdir(rootp):
        full_path = os.path.join(rootp,path)
        if os.path.isdir(full_path):
            print(full_path)
            dir_list(full_path)

def file_list(rootp):
    for path in os.listdir(rootp):
        full_path = os.path.join(rootp,path)
        if os.path.isfile(full_path):
            print(full_path)
        elif os.path.isdir(full_path):
            file_list(full_path)

if __name__ == '__main__':
    dir_list("../../Project101/old_projects")
    print("*********************")
    file_list("../../Project101/old_projects")