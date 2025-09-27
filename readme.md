# 项目文件结构
```
项目目录/
│
├── time_zone_conversion.py       # 时区转换程序
├── photo_compress.py             # 照片压缩程序
├── puzzle_words.py               # 拼单词解题程序
├── readme.md                     # 使用说明
```

---

## [时区转换程序](time_zone_conversion.py)

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

## [照片压缩程序](photo_compress.py)
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

### 作者
此程序由 Bolun Xu 开发。。