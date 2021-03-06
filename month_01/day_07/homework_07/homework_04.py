# 员工列表(员工编号 部门编号 姓名 工资)
dict_employees = {
    1001: {"did": 9002, "name": "师父", "money": 60000},
    1002: {"did": 9001, "name": "孙悟空", "money": 50000},
    1003: {"did": 9002, "name": "猪八戒", "money": 20000},
    1004: {"did": 9001, "name": "沙僧", "money": 30000},
    1005: {"did": 9001, "name": "小白龙", "money": 15000},
}

# 部门列表
list_departments = [
    {"did": 9001, "title": "教学部"},
    {"did": 9002, "title": "销售部"},
    {"did": 9003, "title": "品保部"},
]
'''
# 1. 打印所有员工信息,
# 格式：xx的员工编号是xx,部门编号是xx,月薪xx元.
# 2. 打印所有月薪大于2w的员工信息,
# 格式：xx的员工编号是xx,部门编号是xx,月薪xx元.
# 3. 在部门列表中查找编号最小的部门
# 4. 根据部门编号对部门列表降序排列
'''

# 1. 打印所有员工信息,
# 格式：xx的员工编号是xx,部门编号是xx,月薪xx元.
# 2. 打印所有月薪大于2w的员工信息,
# 格式：xx的员工编号是xx,部门编号是xx,月薪xx元.
# 3. 在部门列表中查找编号最小的部门
# 4. 根据部门编号对部门列表降序排列

# 1. 打印所有员工信息,
for code, infor in dict_employees.items():
    print(f'{infor["name"]}的员工编号是{code},部门编号是{infor["did"]},月薪{infor["money"]}元')
# 格式：xx的员工编号是xx,部门编号是xx,月薪xx元.
# 2. 打印所有月薪大于2w的员工信息,
for code, infor in dict_employees.items():
    if infor["money"] > 20000:
        print(f'{infor["name"]}的员工编号是{code},部门编号是{infor["did"]},月薪{infor["money"]}元')
# 格式：xx的员工编号是xx,部门编号是xx,月薪xx元.
# 3. 在部门列表中查找编号最小的部门
# 部门列表
# list_departments = [
#     {"did": 9001, "title": "教学部"},
#     {"did": 9002, "title": "销售部"},
#     {"did": 9003, "title": "品保部"},
# ]
min_departments  = list_departments[0]
for i in range(1,len(list_departments)):
    if min_departments["did"] >list_departments[i]["did"]:
        min_departments = list_departments[i]
print(f"编号最小的部门是{min_departments['did']}-{min_departments['title']}")
# 4. 根据部门编号对部门列表降序排列

for r in range(len(list_departments)-1):
    for c in range(r+1,len(list_departments)):
        if list_departments[r]['did'] < list_departments[c]['did']:
            list_departments[r],list_departments[c] = list_departments[c],list_departments[r]
print(list_departments)

