import os
import hashlib
import shutil
import random
import string

# 定义原始文件夹路径和目标文件夹路径
source_folder = os.path.join(os.path.dirname(__file__), '待转')
target_folder = os.path.join(os.path.dirname(__file__), '转化后')

# 检测运行目录下是否存在'待转''转化后'文件夹，如果不存在则创建
if not os.path.exists(source_folder):
    os.makedirs(source_folder)
if not os.path.exists(target_folder):
    os.makedirs(target_folder)

# 遍历原始文件夹中的所有文件
for root, dirs, files in os.walk(source_folder):
    for filename in files:
        # 获取每个文件的绝对路径
        source_file_path = os.path.join(root, filename)

        # 计算原始文件的MD5值
        with open(source_file_path, 'rb') as f:
            md5 = hashlib.md5(f.read()).hexdigest()

        # 在目标文件夹中创建一个新文件
        target_file_path = os.path.join(target_folder, filename)

        # 如果目标文件夹中已经存在同名文件，则删除该文件
        if os.path.exists(target_file_path):
            os.remove(target_file_path)

        # 打开原始图片文件和目标文件
        with open(source_file_path, 'rb') as source_file, open(target_file_path, 'wb') as target_file:
            # 从原始图片文件中读取二进制数据，并写入目标文件中
            binary_data = source_file.read()
            target_file.write(binary_data)

            # 生成一段随机字符串并将其写入目标文件中
            random_str = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
            random_str_binary = random_str.encode('utf-8')
            target_file.seek(0, os.SEEK_END)
            target_file.write(random_str_binary)

        # 计算新文件的MD5值
        with open(target_file_path, 'rb') as f:
            new_md5 = hashlib.md5(f.read()).hexdigest()

        # 输出文件的名称和原始MD5值、新的MD5值
        print(f'{filename} 的原始 MD5 值为: {md5}')
        print(f'{filename} 的新的随机 MD5 值为：{new_md5}')
        print('-' * 50)

print(f'已将所有文件复制到目标文件夹 {target_folder} 中')

# 等待用户输入，保持窗口打开界面
input("处理完成，按任意键退出")
