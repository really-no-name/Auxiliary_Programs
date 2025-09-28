# pdf 解锁
# 作者：徐浡伦

from PyPDF2 import PdfReader, PdfWriter

# 建议使用绝对路径
input_pdf = "/Users/Personal_File/Auxiliary_Programs/3205内部审计师指南.pdf"
output_pdf = "/Users/Personal_File/Auxiliary_Programs/1.pdf"

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
