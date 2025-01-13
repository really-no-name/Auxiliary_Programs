# PDF压缩
# 作者：徐浡伦

import os
import subprocess


def compress_pdf(input_file, output_file, quality='screen'):
    """
    压缩 PDF 文件的函数。

    参数:
        input_file (str): 需要压缩的 PDF 文件路径。
        output_file (str): 输出的压缩后 PDF 文件路径。
        quality (str): 压缩质量，可选值为 'screen', 'ebook', 'printer', 'prepress'。
    """
    quality_options = ['screen', 'ebook', 'printer', 'prepress']

    if quality not in quality_options:
        print(f"无效的质量选项，使用默认 'screen' 压缩。")
        quality = 'screen'

    command = [
        'gs', '-sDEVICE=pdfwrite',
        '-dCompatibilityLevel=1.4',
        f'-dPDFSETTINGS=/{quality}',
        '-dNOPAUSE', '-dQUIET', '-dBATCH',
        f'-sOutputFile={output_file}', input_file
    ]

    try:
        subprocess.run(command, check=True)
        print(f"PDF 压缩成功，输出文件：{output_file}")
    except subprocess.CalledProcessError as e:
        print("压缩失败:", e)
    except FileNotFoundError:
        print("Ghostscript 未安装或未找到。请确保已安装 ghostscript。")


if __name__ == "__main__":
    input_pdf = "1.pdf"  # 替换为你的 PDF 文件路径
    output_pdf = "compressed_1.pdf"  # 输出压缩后的文件路径
    quality = "printer"  # 可选 'screen', 'ebook', 'printer', 'prepress'

    compress_pdf(input_pdf, output_pdf, quality)