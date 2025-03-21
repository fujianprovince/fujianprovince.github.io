print("陈郑逸领域-文本重复器")
print("BY fujianprovince.github.io")
print()
print("该文本重复器用于重复输出任意次你输入的任意文本，以避免需要手动复制多次文本时的繁琐。")
print()
while True:
    text=input("请输入你欲重复的文本：")
    time=input("请输入你欲重复的次数：")
    try:
        print("输出："+text*int(time))
    except:
        print("你输入的次数不合理，请重新输入！")