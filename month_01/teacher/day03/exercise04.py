# 练习:在终端中获取性别,
# 打印"您好先生" "您好女士" "性别未知"
dict_sex = {"男":"先生","女":"女士"}
sex = input("请输入性别：")
if sex in  dict_sex:
    print(dict_sex[sex])
else:
    print("性别未知")

