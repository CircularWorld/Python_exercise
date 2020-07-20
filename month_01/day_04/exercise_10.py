'''
打印每个字的编码值
'''
# text = in



while True:
    code = input('请输入编码值：')
    if code == '':
        break
    print(chr(int(code)))
