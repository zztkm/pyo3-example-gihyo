import strcounter

# 文字列を引数として英字、数値、その他の文字の数を返す関数
def count_chars(text: str):
    # カウント用の変数を初期化
    alphabet = 0
    digit = 0
    other = 0

    for c in text:
        if c.isalpha() and c.isascii():
            alphabet += 1
        elif c.isdigit():
            digit += 1
        else:
            other += 1
    return alphabet, digit, other


if __name__ == "__main__":
    text = "Python Monthly Topics: 2023年7月"
    alphabet, digit, other = strcounter.count_chars(text)
    print(f"アルファベット: {alphabet}")
    print(f"数値: {digit}")
    print(f"その他: {other}")

