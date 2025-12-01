# 项目文件结构
```
项目目录/
│
├── PDF_compress.py               # PDF压缩
├── PDF_Unlock.py                 # PDF解锁
├── photo_compress.py             # 照片压缩程序
├── puzzle_words.py               # 拼单词解题程序
├── sequence_variation.py         # 宝洁在线测评题型1——水管翻转题
├── solve_equ.py                  # 宝洁在线测评题型2——数字运算题
├── text_compare.py               # 文字差异对比
├── time_zone_conversion.py       # 时区转换程序
│
│
├── readme.md                     # 使用说明
```

---
## [PDF压缩](Code/PDF_compress.py)
用于压缩较大的PDF文件

建议使用绝对路径

### 基本用法：
```bash
# 压缩单个PDF文件
python pdf_compress.py input.pdf output.pdf
```

### 指定压缩质量
```bash
# 使用ebook质量（适合电子书阅读）
python pdf_compress.py document.pdf compressed.pdf -q ebook

# 使用printer质量（适合打印）
python pdf_compress.py document.pdf compressed.pdf -q printer

# 使用prepress质量（最高质量，适合印刷）
python pdf_compress.py document.pdf compressed.pdf -q prepress
```


### 批量压缩脚本示例
创建`batch_compress.sh`脚本
```bash
#!/bin/bash
# 批量压缩当前目录下所有PDF文件

for pdf_file in *.pdf; do
    if [ -f "$pdf_file" ]; then
        output_file="compressed_${pdf_file}"
        echo "正在压缩: $pdf_file -> $output_file"
        python pdf_compress.py "$pdf_file" "$output_file" -q ebook
        echo "----------------------------------------"
    fi
done
```

### Windows 批量处理
创建`batch_compress.bat`脚本
```bash
@echo off
for %%i in (*.pdf) do (
    echo 正在压缩: %%i
    python pdf_compress.py "%%i" "compressed_%%i" -q ebook
    echo ----------------------------------------
)
pause
```


### 静默模式（适合脚本调用）
```bash
python pdf_compress.py large.pdf small.pdf -q screen --silent
```


---
## [PDF解锁](Code/PDF_Unlock.py)
用于解锁需要密码的PDF文件

请使用绝对路径

### 基本用法（使用空密码）

```bash
# 尝试用空密码解锁
python pdf_Unlock.py encrypted.pdf unlocked.pdf
```



### 使用已知密码

```bash
# 使用已知密码解锁
python pdf_unlock.py encrypted.pdf unlocked.pdf -p "mypassword"

# 或使用长选项
python pdf_unlock.py encrypted.pdf unlocked.pdf --password "mypassword"
```

## [时区转换程序](Code/time_zone_conversion.py)

### 简介
本程序是一个基于 Python 的时区转换工具，用于将一个城市的时间转换为另一个城市的时间。例如，输入冰岛的时间（例如早上 8 点），程序将计算并返回对应的北京时间。

---

### 功能
- 支持全球任意时区的时间转换。
- 用户可自定义源城市时区和时间，目标城市固定为北京时间（Asia/Shanghai）。
- 支持 24 小时制输入，返回标准格式化时间。

---

### 环境要求
- **Python 版本：** 3.7 或更高
- **依赖库：**
  - `pytz`
  - `datetime`

如未安装 `pytz`，可使用以下命令安装：
```bash
pip install pytz
```

---

### 使用说明

1. **运行程序**  
   使用终端或命令行运行程序：
   ```bash
   python 时区转换程序.py
   ```

2. **输入参数**  
   程序运行后，用户需输入以下参数：
   - **源城市时区**：IANA 时区名称，例如：
     - 北京：`Asia/Shanghai`
     - 冰岛：`Atlantic/Reykjavik`
   - **源时间**：整数格式，表示 24 小时制的小时数，例如 `8`。

3. **输出结果**  
   程序将输出目标城市（默认北京）的时间，格式为：
   ```
   目标时间（Asia/Shanghai）：2025-01-13 16:00:00
   ```

---

### 示例
#### 输入
```
请输入源城市时区（例如：Atlantic/Reykjavik 表示冰岛）：Atlantic/Reykjavik
请输入源时间（24小时制小时）：8
```

#### 输出
```
目标时间（Asia/Shanghai）：2025-01-13 16:00:00
```

---

### 注意事项
1. **时区名称格式**  
   输入的时区名称必须符合 [IANA 时区数据库](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones)，例如：
   - 正确：`Asia/Shanghai`、`Atlantic/Reykjavik`
   - 错误：`Beijing`、`Iceland`
   
2. **时间格式**  
   输入时间为整数（小时部分，24 小时制），例如：
   - 正确：`8`、`14`
   - 错误：`8:00`、`08`

3. **依赖库**  
   确保在运行程序前已安装 `pytz`。

---



### 未来改进
1. 支持用户自定义目标时区。
2. 增加输入格式的灵活性（支持分和秒）。
3. 提供 GUI 界面，方便用户操作。

---

## [照片压缩程序](Code/photo_compress.py)
是一个简单的 Python 程序，用于压缩照片的大小。它使用了 `Pillow` 库（Python Imaging Library 的分支）来处理图像压缩。你可以指定目标尺寸或通过调整图像质量来压缩文件大小。

### 使用说明

1. **安装依赖**：
   运行以下命令安装 `Pillow` 库：
   ```bash
   pip install pillow
   ```

2. **运行程序**：
   将程序保存为 `compress_image.py`，然后使用终端运行。确保替换代码中 `input_image_path` 和 `output_image_path` 为你自己的图片路径。

3. **参数说明**：
   - `quality`：控制输出图像的质量（1-100）。值越低，压缩越强，文件越小。
   - `max_size`：用于限制图片的最大宽高（例如 `(800, 800)` 表示限制图片的最大宽和高为 800 像素）。

4. **输出文件**：
   压缩后的图片会保存在指定的 `output_image_path` 路径下。

---

## [文档对比](Code/text_compare.py)

用于对比两个txt文本文件中的文字内容是否一致。

PS： 不考虑所有非文字字符、空格、换行等。




### 作者
此程序由 Bolun Xu 开发。。