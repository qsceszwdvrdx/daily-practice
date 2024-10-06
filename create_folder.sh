#!/bin/bash

# 取得今天的日期 (YYYYMMDD)
today=$(date +"%Y%m%d")
echo "今天的日期是: $today"

# 指定儲存的目錄路徑 (這裡可以是當前目錄，也可以指定具體路徑)
directory="$(pwd)"
echo "當前工作目錄是: $directory"

# 組合資料夾名稱
foldername="${today}-leetcode"
folderpath="${directory}/${foldername}"

# 檢查資料夾是否已經存在
if [ ! -d "$folderpath" ]; then
    # 創建資料夾
    mkdir "$folderpath"
    echo "$folderpath 已創建。"
else
    echo "$folderpath 已經存在。"
fi

# 檔案名稱
ipynb_filename="${folderpath}/${today}-leetcode.ipynb"
py_filename="${folderpath}/${today}-leetcode.py"
readme_filename="${folderpath}/README.md"

# 檢查 ipynb 檔案是否已經存在
if [ ! -f "$ipynb_filename" ]; then
    # 創建空的 .ipynb 檔案
    echo '{"cells": [], "metadata": {}, "nbformat": 4, "nbformat_minor": 5}' > "$ipynb_filename"
    echo "$ipynb_filename 已創建。"
else
    echo "$ipynb_filename 已經存在。"
fi

# 檢查 py 檔案是否已經存在
if [ ! -f "$py_filename" ]; then
    # 創建空的 .py 檔案
    echo "# Python script for LeetCode problems" > "$py_filename"
    echo "$py_filename 已創建。"
else
    echo "$py_filename 已經存在。"
fi

# 檢查 README.md 檔案是否已經存在
if [ ! -f "$readme_filename" ]; then
    # 創建 README.md 檔案
    echo "# LeetCode Problems\n\nThis folder contains solutions to LeetCode problems." > "$readme_filename"
    echo "$readme_filename 已創建。"
else
    echo "$readme_filename 已經存在。"
fi
