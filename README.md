# push_swap_tester

## 機能

1. push_swapのテスト
   - `push_swap` を実行し、`checker` を使って出力を確認します。
     - オプションで、引数の個数、数値の範囲、テスト回数、push_swapのディレクトリを指定できます。
2. テスト用の引数生成
   - テスト用の引数を生成し、標準出力に出力します。

## 使い方

Python 3.8.2で動作を確認しています。

1. リポジトリのclone

   push_swapのプロジェクト内にリポジトリをcloneします。
   ```bash
   git clone https://github.com/nafuka11/push_swap_tester.git
   ```

1. `checker` の配置

   `checker_Mac` / `checker_linux` を使う場合
   - 実行ファイル `push_swap` と同じディレクトリに配置し、`checker` にリネームしてください。
   - リネーム後、 `checker` に実行権限がついていることを確認してください。
     ```bash
     ls -l checker
     ```
   - `checker` に実行権限が付いていない場合、実行権限を付与してください。
     ```bash
     chmod +x checker
     ```

   自分でビルドした `checker` を使う場合
   - この手順はスキップしてください。

1. `push_swap` のビルド

   - push_swap_testerは、実行ファイル `push_swap` のビルドを行いません。  
     push_swap_testerを実行する前に `make` 等のコマンドを実行して `push_swap` をビルドするようにしてください。

1. cloneしたリポジトリのディレクトリに移動
   ```bash
   cd push_swap_tester
   ```

### ヘルプ

```bash
python3 push_swap_tester.py -h
```

### テストの実行

```bash
python3 push_swap_tester.py
```

- 引数5個の順列を作成してテストします。
  - 順列の個数が、引数で指定したテスト回数（デフォルトは200回）を下回る場合、順列を生成します。
  - そうでない場合はランダムな数列を生成します。

テストすると以下のような標準出力がされます。
```bash
........................................................................................................................
---- Result ----
max   : 10
median: 7
min   : 0
See result.log for details
```
- checkerでOK/KOを判定します。OKなら緑色の `.` を、KOなら赤色の `F` を標準出力します。
- push_swap命令数の最大値（max）、中央値（median）、最小値（min）を標準出力します。
- `result.log` に詳細な情報を出力します。

#### オプション

オプションで、引数の個数、数値の範囲、テスト回数、push_swapのディレクトリを指定できます。

|オプション|内容|デフォルト値|
|--|--|--|
|-l, --len <個数>|push_swapに渡す引数の個数を指定します|5|
|-c, --count <回数>|テストする回数を指定します|200|
|-r, --range <最小値 最大値>|push_swapに渡す引数の範囲を指定します|`INT_MIN` `INT_MAX`|
|-d, --dir <ディレクトリ>|push_swapのディレクトリを指定します|`..`|
|-g, --gen|指定すると、テストをする代わりに引数を生成して標準出力します|無効|

#### コマンド例

```bash
# 引数5個のテスト（引数の値の範囲：INT_MINからINT_MAX）
python3 push_swap_tester.py
# 引数5個のテスト（引数の値の範囲：1から5）
python3 push_swap_tester.py -r 1 5

# 引数100個のテストを200回行う（引数の値の範囲：INT_MINからINT_MAX）
python3 push_swap_tester.py -l 100
# 引数100個のテストを400回行う（引数の値の範囲：INT_MINからINT_MAX）
python3 push_swap_tester.py -l 100 -c 400

# 引数500個のテストを200回行う（引数の値の範囲：INT_MINからINT_MAX）
python3 push_swap_tester.py -l 500

# ../project_dir にあるpush_swapをテスト
python3 push_swap_tester.py -d ../project_dir
```

### テスト用の引数生成

```bash
python3 push_swap_tester.py --gen
```
オプションで、引数の個数、数値の範囲を指定できます。

#### 例
INT_MINからINT_MAXの範囲で10個の引数を生成
```bash
python3 push_swap_tester.py --gen -l 10
```
出力
```bash
-1110677087 -738511178 1555694097 1972999663 989665463 -2116604533 819005173 -895360136 -613437200 1767332339
```
使用例
```bash
ARG=`python3 push_swap_tester.py --gen -l 10` ../push_swap $ARG | ../checker $ARG
```
