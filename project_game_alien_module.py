
'''
count=0
list_alien_first=[]
for i in range(0,30):
    dict_alien={"color":"green","point":5,"speed":"slow"}
    list_alien_first.append(dict_alien)
#以上是对包含字典的列表的创建
'''
'''
for i in range(0,30):
    print("\n")
    print(list_alien_first[i])
    count=count+1
print("\nThe total number is {0}".format(count))
'''
'''
#以上是对包含所有字典的完整列表的输出
for alien in list_alien_first[:3]:
    alien["color"]="yellow"
    alien["point"]="10"
    alien["speed"]="medium"
for alien in list_alien_first[:3]:
    print("\n")
    print(alien)
print("是否全面升级？(Y/N)")
judge=input()
if ((judge=='Y')or(judge=='y')):
    for alien in list_alien_first:
        if  "green"==alien["color"]:
            alien["color"]="yellow"
            alien["point"]="10"
            alien["speed"]="medium"
        elif "yellow"==alien["color"]:
            alien["color"]="red"
            alien["point"]="15"
            alien["speed"]="quick"
#以上是对列表中部分字典的单独修改
for i in range(0,30):
    print("\n")
    print(list_alien_first[i])
'''
############################################
#以上是对外星人的字典列表的初步创建，及升级程序#
############################################
