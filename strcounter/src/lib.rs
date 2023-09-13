use pyo3::prelude::*;

/// 文字列を受け取り英字、数値、その他の文字数をカウントした結果を返す
#[pyfunction]
fn count_chars(s: &str) -> (usize, usize, usize) {
    // カウント用変数定義
    let mut alphabet = 0;
    let mut digit = 0;
    let mut other = 0;

    for c in s.chars() {
        if c.is_ascii_alphabetic() {
            alphabet += 1;
        } else if c.is_ascii_digit() {
            digit += 1;
        } else {
            other += 1;
        }
    }
    (alphabet, digit, other)
}

/// A Python module implemented in Rust.
#[pymodule]
fn strcounter(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(count_chars, m)?)?;
    Ok(())
}
