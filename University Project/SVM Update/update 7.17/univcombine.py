import pandas as pd
import numpy as np
import glob,os

def read_all_csv(folder1, folder2):
    folder1 = 'C:/Users/huang/Dropbox/AlexXuRichard/School tests/UR p&h&cs'
    folder2 = 'C:/Users/huang/Dropbox/AlexXuRichard\School tests/UB p&h&cs'
    folder3 = 'C:/Users/huang/Dropbox/AlexXuRichard/School tests/Van p&h&cs'
    folder4 = 'C:/Users/huang/Dropbox/AlexXuRichard/School tests/MIT p&h&cs'
    folder5 = 'C:/Users/huang/Dropbox/AlexXuRichard/School tests/Stan p&h&cs'
    folder_list = [folder1, folder2, folder3, folder4, folder5]
    # the location of the folders might need to change because your domain is different from me.
    list_csv = []
    for f in folder_list:
        dir_list = os.listdir(f)
        print(dir_list)
        for cur_file in dir_list:
            path = os.path.join(f, cur_file)
            # 判断是文件夹还是文件 ( distinguish if the file is a file or directory really)
            if os.path.isfile(path):
                # print("{0} : is file!".format(cur_file))
                dir_files = os.path.join(f, cur_file)
            # 判断是否存在.csv文件，如果存在则获取路径信息写入到list_csv列表中
            # (distinguish if csv file is existed, if it does then put the path into my list)
            if os.path.splitext(path)[1] == '.csv':
                csv_file = os.path.join(f, cur_file)
                # print(os.path.join(f, cur_file))
                # print(csv_file)
                list_csv.append(csv_file)
            if os.path.isdir(path):
                # print(os.path.join(file_dir, cur_file))
                continue
    return list_csv