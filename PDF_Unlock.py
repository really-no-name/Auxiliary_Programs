# pdf 解锁
# 作者：徐浡伦

from PyPDF2 import PdfReader, PdfWriter

input_pdf = "硕士成绩.pdf"
output_pdf = "1.pdf"

reader = PdfReader(input_pdf)
writer = PdfWriter()

if reader.is_encrypted:
    try:
        reader.decrypt("")  # 尝试空密码或您知道的密码
        for page in reader.pages:
            writer.add_page(page)
        with open(output_pdf, "wb") as output_file:
            writer.write(output_file)
        print("解锁成功！")
    except Exception as e:
        print(f"解锁失败：{e}")
else:
    print("文件未加密。")
