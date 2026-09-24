# viết hàm copy file

import shutil
import os

def copy_func(source_dir, des_dir):
    list_name = os.listdir(source_dir) # lấy các file trong thư mục gốc
    for file_name in list_name:
        shutil.copy(os.path.join(source_dir, file_name), os.path.join(des_dir, file_name)) # copy các file từ thư mục gốc sang 

# đường dẫn thư mục
source_dir = "source_dir"
des_dir = "des_dir"
copy_func(source_dir, des_dir)