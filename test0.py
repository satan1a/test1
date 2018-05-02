#这是test.py文件
'''
def main():
    #string="\nHello"
    #print("We are in %s"%__name__)
    print(__name__)
    print("{name}".format(name="Toky"),end="")
if __name__=="__main__":
    main()
    print("Hello!")
print("This line will be the first")
'''

'''
def fun_animal_print():
    animals=["cat","tiger","dog","shark","godzilla"]
    for animal in animals:
        print(animal.title())
        print("I like {0} so much".format(animal))
        print("But {0} is\' not my favourite\n".format(animal.title()))
        if __name__ == "__main__":
            print("I like python so much!")
if __name__=="__main__":
    #这是利用main调试的代码
    fun_animal_print()
    print("这段文字不会在外部模块调用时出现")
'''
'''
def fun_add(a,b):
    return a+b
if __name__=="__main__":
    print("It will be appear first,and it is containd in other import:")
'''
