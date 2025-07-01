import pandas as pd
import subprocess
import os
import time

# 文件路径
excel_path = r"C:\Users\monica\Downloads\3.3_条码_LTZ.xlsx"
btw_template_path = r"C:\Users\monica\Desktop\提示.btw"
temp_excel = r"C:\Users\monica\Downloads\current_row.xlsx"

# 打开 Excel
df = pd.read_excel(excel_path)

# 添加“处理状态”列（如不存在）
if "处理状态" not in df.columns:
    df["处理状态"] = ""
    
# 找出第一条未处理的记录
row_to_process = df[(df["是否要打印"] == "要打印") & (df["处理状态"] == "")]

if not row_to_process.empty:
    index = row_to_process.index[0]
    row_data = df.loc[[index]]  # 注意要用双中括号保留为 DataFrame

    # 删除“处理状态”列
    row_data = row_data.drop(columns=["处理状态"])

    # 保存当前行到临时文件（不带“处理状态”列）
    row_data.to_excel(temp_excel, index=False)

    # BarTender 命令构造
    cmd = (
        f'"C:\\Program Files\\BarTender 11\\bartend.exe" '
        f'/F="{btw_template_path}" '
        f'/D="{temp_excel}" '
        '/P /X'
    )

    # 执行打印命令
    print(f"打印第 {index + 2} 行...")  # Excel 中从第2行开始是数据
    try:
        subprocess.run(cmd, shell=True, check=True)
        print("打印完成。")

        # 标记为已处理
        df.at[index, "处理状态"] = "已处理"
        df.to_excel(excel_path, index=False)
        print("Excel 已更新，下一次将打印下一行。")

    except subprocess.CalledProcessError as e:
        print(f"打印失败：{e}")
else:
    print("没有待打印的数据了。")

