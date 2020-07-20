'''
3. 一家公司有如下岗位：
   经理 ："曹操","刘备","孙权"
   技术 ："曹操","刘备","张飞","关羽"
    1. 使用集合存储以上信息.
    2. 是经理也是技术的都有谁?
    3. 是经理不是技术的都有谁?
    4. 不是经理是技术的都有谁?
    5. 身兼一职的都有谁?
    6. 公司总共有多少人数?
'''
set_manager = {"曹操", "刘备", "孙权"}
set_technology = {"曹操", "刘备", "张飞", "关羽"}
# 2.是经理也是技术的都有谁?
print(f"是经理也是技术的是 {' '.join(set_manager&set_technology)}")
# 3.是经理不是技术的都有谁?
print(f"是经理不是技术的是 {' '.join(set_manager-set_technology)}")
# 4.不是经理是技术的都有谁?
print(f"是技术不是经理的是 {' '.join(set_technology-set_manager)}")
# 5.身兼一职的都有谁?
print(f"身兼一职的是 {' '.join(set_technology^set_manager)}")
# 6.公司总共有多少人数?
print(f"公司总共有 {len(set_technology|set_manager)}人")