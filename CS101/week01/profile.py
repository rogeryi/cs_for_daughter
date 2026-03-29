# 我的个人信息
# 使用变量来存储和展示个人资料

# === 变量定义 ===
# 姓名（字符串）
from CS101.week01.hello import age_str


name = "Amos"

# 年龄（整数）
age = 16

# 爱好（字符串）
hobby = "玩游戏"

# === 输出信息 ===
print("====== 个人信息卡片 ======")
print("姓名:", name)
print("年龄:", age, "岁")
print("爱好:", hobby)
print("=========================")

# 试试用多个爱好（列表）
hobbies = ["玩游戏", "编程", "画画"]
print("\n我的爱好列表:")
print("1.", hobbies[0])
print("2.", hobbies[1])
print("3.", hobbies[2])

print(type(age))
print(type(age_str))
