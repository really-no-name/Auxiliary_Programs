# PDF压缩
# 作者：徐浡伦
# Version: 2.0

import argparse
import os
import subprocess
import sys


def compress_pdf(input_file, output_file, quality='screen'):
    """
    压缩 PDF 文件的函数。

    参数:
        input_file (str): 需要压缩的 PDF 文件路径。
        output_file (str): 输出的压缩后 PDF 文件路径。
        quality (str): 压缩质量，可选值为 'screen', 'ebook', 'printer', 'prepress'。
    """
    # 检查输入文件是否存在
    if not os.path.exists(input_file):
        print(f"错误: 输入文件不存在: {input_file}")
        return False

    # 检查输入文件是否为PDF
    if not input_file.lower().endswith('.pdf'):
        print(f"警告: 输入文件可能不是PDF格式: {input_file}")

    # 检查输出目录是否存在，如果不存在则创建
    output_dir = os.path.dirname(output_file)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir, exist_ok=True)
        print(f"已创建输出目录: {output_dir}")

    quality_options = ['screen', 'ebook', 'printer', 'prepress']

    if quality not in quality_options:
        print(f"无效的质量选项，使用默认 'screen' 压缩。")
        quality = 'screen'

    print(f"开始压缩 PDF 文件...")
    print(f"输入文件: {input_file}")
    print(f"输出文件: {output_file}")
    print(f"压缩质量: {quality}")

    # 获取原始文件大小
    original_size = os.path.getsize(input_file)

    command = [
        'gs', '-sDEVICE=pdfwrite',
        '-dCompatibilityLevel=1.4',
        f'-dPDFSETTINGS=/{quality}',
        '-dNOPAUSE', '-dQUIET', '-dBATCH',
        '-dDetectDuplicateImages=true',
        '-dColorImageDownsampleType=/Bicubic',
        '-dColorImageResolution=150',
        '-dGrayImageDownsampleType=/Bicubic',
        '-dGrayImageResolution=150',
        '-dMonoImageDownsampleType=/Bicubic',
        '-dMonoImageResolution=150',
        f'-sOutputFile={output_file}',
        input_file
    ]

    try:
        print("正在执行 Ghostscript 压缩...")
        result = subprocess.run(command, check=True, capture_output=True, text=True)

        # 检查输出文件是否生成
        if os.path.exists(output_file):
            compressed_size = os.path.getsize(output_file)
            compression_ratio = (1 - compressed_size / original_size) * 100

            print(f"\n✓ PDF 压缩成功！")
            print(f"原始文件大小: {original_size / 1024:.2f} KB")
            print(f"压缩后大小: {compressed_size / 1024:.2f} KB")
            print(f"压缩率: {compression_ratio:.1f}%")
            print(f"输出文件: {output_file}")
            return True
        else:
            print("错误: 输出文件未生成")
            return False

    except subprocess.CalledProcessError as e:
        print(f"压缩失败: {e}")
        if e.stderr:
            print(f"错误详情: {e.stderr}")
        return False
    except FileNotFoundError:
        print("错误: Ghostscript 未安装或未找到。")
        print("请安装 Ghostscript:")
        print("  - Windows: 下载并安装 https://www.ghostscript.com/")
        print("  - macOS: brew install ghostscript")
        print("  - Linux: sudo apt-get install ghostscript")
        return False
    except Exception as e:
        print(f"发生未知错误: {e}")
        return False


def main():
    parser = argparse.ArgumentParser(
        description="PDF 文件压缩工具 - 使用 Ghostscript 进行高质量压缩",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
压缩质量说明:
  screen    - 最低质量, 最小文件大小 (72 dpi)
  ebook     - 中等质量, 适合电子书 (150 dpi)  
  printer   - 高质量, 适合打印 (300 dpi)
  prepress  - 最高质量, 适合印刷 (300 dpi, 保留所有信息)

使用示例:
  # 基本用法
  python pdf_compress.py input.pdf output.pdf

  # 指定压缩质量
  python pdf_compress.py input.pdf output.pdf -q ebook

  # 使用最高质量压缩
  python pdf_compress.py document.pdf compressed.pdf -q prepress

  # 压缩当前目录下所有PDF文件
  for pdf in *.pdf; do python pdf_compress.py "$pdf" "compressed_$pdf"; done
        """
    )

    parser.add_argument(
        "input_file",
        help="需要压缩的PDF文件路径"
    )

    parser.add_argument(
        "output_file",
        help="压缩后的PDF文件输出路径"
    )

    parser.add_argument(
        "-q", "--quality",
        choices=["screen", "ebook", "printer", "prepress"],
        default="screen",
        help="压缩质量 (默认: screen)"
    )

    parser.add_argument(
        "-v", "--version",
        action="version",
        version="PDF压缩工具 v2.0 (使用Ghostscript)"
    )

    # 添加静默模式选项
    parser.add_argument(
        "--silent",
        action="store_true",
        help="静默模式，仅输出错误信息"
    )

    args = parser.parse_args()

    # 执行压缩
    success = compress_pdf(args.input_file, args.output_file, args.quality)

    if success:
        if not args.silent:
            print("🎉 操作完成！")
        sys.exit(0)
    else:
        if not args.silent:
            print("❌ 操作失败！")
        sys.exit(1)


if __name__ == "__main__":
    main()
