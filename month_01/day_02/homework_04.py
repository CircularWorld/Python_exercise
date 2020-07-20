'''
4. 根据父母身高,预测儿子身高.
    步骤:获取父亲身高
        获取母亲身高
        显示儿子身高
    公式:(父亲身高+母亲身高)*0.54
'''

father_hight = float(input('请输入父亲身高：'))
# mather_hight = float(input('请输入母亲身高：'))
son_hight = 172
mather_hight = son_hight/0.54 - father_hight
    # (father_hight + mather_hight) * 0.54
print('儿子身高为：'+str(son_hight)+'cm')
print('母亲身高为：'+str(mather_hight)+'cm')

