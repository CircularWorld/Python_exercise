'''
智商IQ = 心理年龄MA 除以 实际年龄CA 乘以 100
天才：140以上（包含）
超常：120-139之间（包含）
聪慧：110-119之间（包含）
正常：90-109之间（包含）
迟钝：80-89之间（包含）
低能：80以下
根据心理年龄与实际年龄，打印智商等级。
'''
actual_age = int(input('请输入实际年龄：'))
Psychological_age = int(input('请输入心理年龄：'))
iq = Psychological_age / actual_age * 100
# IQ = int(input('IQ = '))
print('IQ = %d' % iq)
if iq >= 140:
    print('天才')
elif iq >= 120:
    print('超常')
elif iq >= 110:
    print('聪慧')
elif iq >= 90:
    print('正常')
elif iq >= 80:
    print('迟钝')
else:
    print('低能')
