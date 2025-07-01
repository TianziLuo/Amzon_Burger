import shutil
import os

# 源文件路径
source_path = r"C:\Frank\3.3_条码.xlsx"

# 目标文件夹路径（当前用户的 Downloads）
downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads")

# 构造目标文件路径
destination_path = os.path.join(downloads_folder, "3.3_条码_LTZ.xlsx")

# 执行复制
shutil.copy2(source_path, destination_path)

print(f"文件已复制到: {destination_path}")
