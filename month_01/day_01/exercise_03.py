'''
    汇率转换
    １美元　＝　７．１３６３
    １人民币　＝　０．１４０１
'''

type = input('请输入要转换的货币USD|RMB:')
if type in ['USD', 'RMB']:
    money = float(input('请输入货币数值：'))
    if type == 'USD':
        print('%.2f美元　＝　%.2f人民币' % (money, money * 7.1363))
    else:
        print('%.2f人民币元　＝　%.2f美元' % (money, money * 0.1401))
else:
    print('error')
