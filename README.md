# push_swap_tester

## 機能
1. push_swapのテスト
   - `push_swap` を実行し、`checker` を使って出力を確認します。
     - オプションで、引数の個数、数値の範囲、テスト回数、push_swapのディレクトリを指定できます。
2. テスト用の引数生成
   - テスト用の引数を生成し、標準出力に出力します。

## 使い方

Python 3.8.2で動作を確認しています。

### ヘルプ

```bash
python3 push_swap_tester.py -h
```

### テストの実行

```bash
python3 push_swap_tester.py
```
オプションで、引数の個数、数値の範囲、テスト回数、push_swapのディレクトリを指定できます。

### テスト用の引数生成

```bash
python3 push_swap_tester.py --gen
```
オプションで、引数の個数、数値の範囲を指定できます。
