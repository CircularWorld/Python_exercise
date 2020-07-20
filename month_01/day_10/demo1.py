# 返回比较某项元素返回最大对象
def get_max_value(*_list,):
    max_vlaue = _list[0]
    for i in range(1,len(_list)):
        if max_vlaue.price < _list[i].price:
            max_vlaue = _list[i]
    return max_vlaue