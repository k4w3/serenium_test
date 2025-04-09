# Selenium CSV Automation Bot

自動でCSVファイルを読み取り、ブラウザ操作を行い、出力結果を保存するPythonスクリプトです。  
ファイルを監視し、必要な情報をWebページから取得してCSVに出力、整理までを全自動で実行します。

---

## 機能

- `input` フォルダ内のCSVファイルを自動監視
- Webサイト（[Proleed Academy](https://proleed.academy/exercises/selenium/automation-practice-form-with-radio-button-check-boxes-and-drop-down.php)）へ自動入力
- ラベルテキスト（Full Name / Father Name / Mother Name）を取得
- 出力ファイルを自動生成し、`result` フォルダへ移動
- 処理済みファイルは自動削除
- 無限ループ監視

---

## インストール

```
pip install selenium pandas
```

## 使い方

```
python .\test.py
```
