"""
定义函数,计算孩子身高.
    father_height = float(input("请输入父亲的身高（厘米）:"))
    mother_height = float(input("请输入母亲的身高（厘米）:"))
    son_height = (father_height + mother_height) * 0.54
    print("预测儿子的身高是:" + str(son_height) + "厘米")
"""
def by_f_mother_calculate_son_height(father_height,mother_height):
    """
    通过父母身高，计算孩子身高
    :param father_height: 父亲身高
    :param mother_height: 母亲身高
    :return: 儿子身高
    """
    son_height = (father_height + mother_height) * 0.54
    return son_height

father_height = float(input("请输入父亲的身高（厘米）:"))
mother_height = float(input("请输入母亲的身高（厘米）:"))
son_height = by_f_mother_calculate_son_height(father_height,mother_height)
print(f"预测儿子的身高是:{son_height}厘米")