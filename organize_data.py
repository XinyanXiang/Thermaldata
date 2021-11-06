import os

current_path = os.getcwd()
channel_folder_list = os.listdir(current_path)
for folder in channel_folder_list:
    if folder.startswith('geo'): 
        file_path = current_path + "/{0}".format(folder)

        for fname in os.listdir(file_path):
            if fname.startswith("all"):
                os.remove(os.path.join(file_path, fname))
        