from timeit import timeit

import httpx
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
    # 特定のURLからテキストを取得
    url = "https://gihyo.jp/article/2023/06/monthly-python-2306"
    res = httpx.get(url)
    res.encoding = "utf-8"
    text = res.text

    loop = 100 # ベンチマークのループ回数
    # Python 版
    p_res = timeit(lambda: count_chars(text), number=loop)
    p_time = p_res / loop * 1_000_000 # マイクロ秒で表示
    print(f"Python avg: {p_time:.2f} μs")

    # Rust 版
    r_res = timeit(lambda: strcounter.count_chars(text), number=loop)
    r_time = r_res / loop * 1_000_000
    print(f"Rust avg: {r_time:.2f} μs")
