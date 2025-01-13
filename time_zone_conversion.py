# 时区转换
# 作者：徐浡伦

from datetime import datetime
import pytz

def time_conversion(target_city, source_city, source_hour):
    try:
        # 设置时区
        target_timezone = pytz.timezone(target_city)
        source_timezone = pytz.timezone(source_city)

        # 创建源时间对象，并正确绑定时区
        source_time_obj = source_timezone.localize(
            datetime.strptime(f"{source_hour}:00", "%H:%M")
        )

        # 转换到目标时区
        target_time_obj = source_time_obj.astimezone(target_timezone)

        # 返回转换后的时间
        return target_time_obj.strftime('%Y-%m-%d %H:%M:%S')
    except Exception as e:
        return f"发生错误: {e}"

# 主程序
if __name__ == "__main__":
    # 北京时间的目标时区
    target_city = "Asia/Shanghai"  # 北京

    # 用户输入
    source_city = input("请输入源城市时区（例如：Atlantic/Reykjavik 表示冰岛）：").strip()
    source_hour = input("请输入源时间（24小时制小时）：").strip()

    try:
        # 将输入的小时转换为整数
        source_hour = int(source_hour)

        # 调用转换函数
        result = time_conversion(target_city, source_city, source_hour)
        print(f"目标时间（{target_city}）：{result}")
    except ValueError:
        print("请输入有效的小时数（整数）！")

