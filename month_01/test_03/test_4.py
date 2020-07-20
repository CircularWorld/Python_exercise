"""
根据值，对字典进行升序排列。
输入：{"张无忌":201,"赵敏":101,"小昭":105,"周芷若":302}
输出：[('赵敏', 101), ('小昭', 105), ('张无忌', 201), ('周芷若', 302)]
"""


def sort_dict_by_num(dict_people):
    list_target = sort_list_increase(list(dict_people.values()))
    dict_people = change_dict_value_key(dict_people)
    for num in list_target:
        list_people.append((dict_people[num],num))


def change_dict_value_key(dict_people):
    return {v:k for k,v in dict_people.items()}


def sort_list_increase(list_target):
    for r in range(len(list_target) - 1):
        for c in range(r + 1, len(list_target)):
            if list_target[r] > list_target[c]:
                list_target[r], list_target[c] = list_target[c], list_target[r]
    return list_target

dict_people = {"张无忌": 201, "赵敏": 101, "小昭": 105, "周芷若": 302}

list_people = []
sort_dict_by_num(dict_people)
print(list_people)
print(dict_people)


