# gihyo で解説された PyO3 の記事のサンプルコード

https://gihyo.jp/article/2023/07/monthly-python-2307

## 前提条件

- Rust
- rye

## 実行方法

仮想環境を activate しておく。
```bash
rye sync
source .venv/bin/activate
```

## Note

muturin develop を実行すると、pip を使ってライブラリを仮想環境にインストールしようとするが、
rye は仮想環境 `.venv` に pip をインストールしないので、自分でインストールしておく必要がある。

**Type hints**
現状は、自分で stub files を作成するのが一番簡単なようだ。(参照: `strcounter/strcounter/strcounter.pyi`)
- [Typing and IDE hints for you Python package](https://pyo3.rs/v0.19.2/python_typing_hintsa)
- [PEP 484 – Type Hints | Stub Files](https://peps.python.org/pep-0484/#stub-files)
