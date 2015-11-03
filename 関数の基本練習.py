def say_aisatsu4(name,aisatsu="Hello"):
    return aisatsu + ", " + name + "!"

print(say_aisatsu4("Taro","Konnichiwa"))

def foo():
    print("I am foo!")
    return
foo()

#

def say_aisatsu(name):
    return "Hello," + name + "!"

print(say_aisatsu("Tanaka"))

#
#引数と戻り値
#

def say_aisatsu2(name,aisatsu):
    return name + ", " + aisatsu + "!"

print(say_aisatsu2("Tadashi","Konnichiwa"))

#
#引数のデフォルト値
#以下の場合はHelloがデフォルトの引数として使用される
#

def say_aisatsu3(name,aisatsu="Hello"):
    return aisatsu + ", " + name + "!"

print(say_aisatsu3("Taro"))


#
#引数にデフォルト値を入れても返り値を指定すれば上書きされる
#

def say_aisatsu3(name,aisatsu="Hello"):
    return aisatsu + ", " + name + "!"

print(say_aisatsu3("Taro","ossu!"))

#
#引数(通常版)
#

def who_have(who,what):
    return who + " have " + what + "."

print(who_have("I","a pen"))

#
#キーワード引数
#

def who_have(who,what):
    return who + " have " + what + "."

print(who_have(who="I",what="a pen"))


#
#キーワード引数とデフォルト値の組み合わせ
#

def f(a="a",b="b",c="c",d="d"):
    print(a,b,c,d)
f(d="D!")
f(c="C!",b="B")
f("A!",d="D!")
f("A!","B!",d="D!")
