# pdf 解锁
# 作者：徐浡伦
# Version: 2.0


import argparse
import os
import sys
from PyPDF2 import PdfReader, PdfWriter
import getpass


def unlock_pdf(input_file, output_file, password=None, silent=False):
    """
    解锁PDF文件的函数。

    参数:
        input_file (str): 需要解锁的PDF文件路径。
        output_file (str): 解锁后的PDF文件输出路径。
        password (str): 解密密码，如果为None则尝试空密码。
        silent (bool): 静默模式，减少输出信息。
    """
    # 检查输入文件是否存在
    if not os.path.exists(input_file):
        if not silent:
            print(f"错误: 输入文件不存在: {input_file}")
        return False

    # 检查输入文件是否为PDF
    if not input_file.lower().endswith('.pdf'):
        if not silent:
            print(f"警告: 输入文件可能不是PDF格式: {input_file}")

    # 检查输出目录是否存在，如果不存在则创建
    output_dir = os.path.dirname(output_file)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir, exist_ok=True)
        if not silent:
            print(f"已创建输出目录: {output_dir}")

    try:
        if not silent:
            print(f"正在读取PDF文件: {input_file}")

        reader = PdfReader(input_file)
        writer = PdfWriter()

        if reader.is_encrypted:
            if not silent:
                print("检测到PDF文件已加密，尝试解锁...")

            # 尝试解密
            decryption_success = False
            attempts = []

            # 首先尝试空密码
            try:
                if reader.decrypt(""):
                    decryption_success = True
                    attempts.append("空密码")
            except:
                pass

            # 如果提供了密码，尝试使用
            if not decryption_success and password:
                try:
                    if reader.decrypt(password):
                        decryption_success = True
                        attempts.append("提供的密码")
                except:
                    pass

            # 如果仍然失败，提示用户输入密码
            if not decryption_success and not silent:
                print("自动解密失败，请手动输入密码（直接回车跳过）:")
                user_password = getpass.getpass("请输入密码: ")
                if user_password:
                    try:
                        if reader.decrypt(user_password):
                            decryption_success = True
                            attempts.append("手动输入密码")
                    except:
                        pass

            if decryption_success:
                if not silent:
                    print(f"✓ 解密成功！使用方式: {', '.join(attempts)}")

                # 复制所有页面到写入器
                for page in reader.pages:
                    writer.add_page(page)

                # 写入输出文件
                with open(output_file, "wb") as f:
                    writer.write(f)

                if not silent:
                    original_size = os.path.getsize(input_file)
                    new_size = os.path.getsize(output_file)
                    print(f"✓ 解锁完成！")
                    print(f"原始文件: {input_file} ({original_size / 1024:.2f} KB)")
                    print(f"解锁文件: {output_file} ({new_size / 1024:.2f} KB)")

                return True
            else:
                if not silent:
                    print("❌ 解密失败：无法找到正确的密码")
                return False
        else:
            if not silent:
                print("文件未加密，直接复制...")

            # 即使未加密也复制文件，保持功能一致性
            for page in reader.pages:
                writer.add_page(page)

            with open(output_file, "wb") as f:
                writer.write(f)

            if not silent:
                print(f"✓ 文件复制完成: {output_file}")
            return True

    except Exception as e:
        if not silent:
            print(f"❌ 处理过程中发生错误: {e}")
        return False


def main():
    parser = argparse.ArgumentParser(
        description="PDF 文件解锁工具 - 移除或绕过PDF密码保护",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
功能说明:
  此工具可以尝试移除PDF文件的密码保护或使用已知密码解密。
  支持多种解密方式：空密码、提供密码、交互式输入密码。

使用示例:
  # 基本用法 - 尝试空密码解密
  python pdf_unlock.py encrypted.pdf unlocked.pdf

  # 使用指定密码解密
  python pdf_unlock.py encrypted.pdf unlocked.pdf -p "mypassword"

  # 静默模式（适合脚本调用）
  python pdf_unlock.py encrypted.pdf unlocked.pdf --silent

  # 批量解锁脚本示例
  for pdf in *.pdf; do python pdf_unlock.py "$pdf" "unlocked_$pdf"; done

注意:
  此工具仅适用于您拥有合法访问权限的文件。
  请遵守相关法律法规和版权要求。
        """
    )

    parser.add_argument(
        "input_file",
        help="需要解锁的PDF文件路径"
    )

    parser.add_argument(
        "output_file",
        help="解锁后的PDF文件输出路径"
    )

    parser.add_argument(
        "-p", "--password",
        help="解密密码（如果文件有密码保护）"
    )

    parser.add_argument(
        "-v", "--version",
        action="version",
        version="PDF解锁工具 v2.0"
    )

    parser.add_argument(
        "--silent",
        action="store_true",
        help="静默模式，仅输出错误信息"
    )

    # 添加交互模式选项
    parser.add_argument(
        "-i", "--interactive",
        action="store_true",
        help="交互模式，总是提示输入密码"
    )

    args = parser.parse_args()

    # 执行解锁
    password = args.password
    if args.interactive and not args.silent:
        print("交互模式：")
        user_password = getpass.getpass("请输入密码（直接回车跳过）: ")
        if user_password:
            password = user_password

    success = unlock_pdf(args.input_file, args.output_file, password, args.silent)

    if success:
        if not args.silent:
            print("🎉 操作完成！")
        sys.exit(0)
    else:
        if not args.silent:
            print("❌ 操作失败！")
        sys.exit(1)


if __name__ == '__main__':
    main()