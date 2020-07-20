# 三个骰子摇出的组合
# 请排列出3个色子可以组合的所有数字
# 每个色子数字1—6，可以使用range(1,7)表示

dice = [(r, c, thr) for r in range(1, 7) for c in range(1, 7) for thr in range(1, 7)]
print(dice)

# list_three_dice = [(fir, sen, thir) for fir in range(1, 7) for sen in range(1, 7) for thir in range(1, 7)]
# print(list_three_dice)
