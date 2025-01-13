# 时区转换
# 作者：徐浡伦

from datetime import datetime
import pytz


def time_conversion(target_city, source_city, source_hour):
    try:
        # 调试信息
        # print(f"[调试] 目标城市时区: {target_city}")
        # print(f"[调试] 源城市时区: {source_city}")
        # print(f"[调试] 源时间（小时）: {source_hour}")

        # 设置目标时区和源时区
        target_timezone = pytz.timezone(target_city)
        source_timezone = pytz.timezone(source_city)

        # 调试时区对象
        # print(f"[调试] 目标时区对象: {target_timezone}")
        # print(f"[调试] 源时区对象: {source_timezone}")

        # 当前日期的基础上创建时间
        current_date = datetime.now().date()  # 获取当前日期
        source_time_str = f"{current_date} {source_hour}:00:00"
        source_time_obj = datetime.strptime(source_time_str, "%Y-%m-%d %H:%M:%S")

        # 绑定时区
        source_time_with_tz = source_timezone.localize(source_time_obj)
        # print(f"[调试] 源时间对象（绑定时区后）: {source_time_with_tz}")

        # 转换到目标时区
        target_time_obj = source_time_with_tz.astimezone(target_timezone)
        # print(f"[调试] 转换后的目标时间对象: {target_time_obj}")

        # 返回结果
        return target_time_obj.strftime('%Y-%m-%d %H:%M:%S')
    except Exception as e:
        # 捕获异常并打印调试信息
        # print(f"[调试] 异常发生: {e}")
        return f"发生错误: {e}"


# 主程序
if __name__ == "__main__":
    # 目标城市时区（固定为北京时间）
    target_city = "Asia/Shanghai"

    # 用户输入
    source_city = input("请输入源城市时区（例如：Atlantic/Reykjavik 表示冰岛）：").strip()
    source_hour = input("请输入源时间（24小时制小时）：").strip()

    try:
        # 转换用户输入为整数
        source_hour = int(source_hour)

        # 调用转换函数
        result = time_conversion(target_city, source_city, source_hour)
        print(f"目标时间（{target_city}）：{result}")
    except ValueError:
        print("请输入有效的小时数（整数）！")
