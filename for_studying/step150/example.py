# 「hello world」と出力
print("hello world")

# greet関数を実装し、「こんんちは」と出力
def greet():
    print("こんにちは")

greet()

# nameを引数にとり、「私の名前は{name}です」と出力するprint_name関数
def print_name(name):
    print(f"私の名前は{name}です")

print_name("ドスター@５８期")

# 「おはようございます」という文字列も戻り値として返すget_greet関数
# 戻り値をprint関数で出力
def get_greet():
    return "おはようございます"

print(get_greet())

# a,bを引数にとり、足し算結果を返すadd関数
# 結果をprint関数で出力
def add(a, b):
    return a + b

print(add(1, 2))

