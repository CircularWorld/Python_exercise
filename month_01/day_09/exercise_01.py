"""
转换时间为秒
"""
def change_to_seconds(hours=0,minute =0,seconds = 0):

    all_second = hours*60*60+ minute*60 +seconds
    return all_second

print(change_to_seconds(1, 2, 6))
print(change_to_seconds(minute=2, seconds=6))
print(change_to_seconds(1, minute=2))
print(change_to_seconds(minute=2))