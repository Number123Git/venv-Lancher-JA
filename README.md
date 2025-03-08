# venv Lancher-JA
<p align="center">
  <img src="https://github.com/user-attachments/assets/5aeddbc9-8707-4d1e-9715-d692771bc0f7" width="70%" alt="ロゴ">
</p>

## 概要  

Pythonのみで作られた一瞬でvenv環境を構築できるソフト。  
いちいちコマンドプロントで記述して実行する必要がなくなります。    
<p align="center">
  <img src="https://github.com/user-attachments/assets/66fb80f6-048b-49ee-aef2-0cbbf49ab7c8" width="35%" alt="使用画面">
</p>

## 対応OS
### 必要スペック
| Windows10 | Windows11 | Mac | Linux |
| :----: | :----: | :----: | :----: |
| ◯ | ◯ | ✕ | ✕ |


※Mac, Linuxでは使用不可

## 機能（ver.1.0.0-最新版）

* venv環境の構築
* 環境内へのライブラリのインストール
* 依存関係の記録


## 使い方
1. Release内のLatestとマークが付いたリンクをクリック
2. Assets内の`venv.Laancher.exe`をクリックしてダウンロード
3. ダウンロードした`venv Lancher`をダブルクリックで実行
4. "出力フォルダを選択"と書かれたテキストの横にある"選択"ボタンをクリック  
➤出力フォルダを選択

5. "インストールするパッケージ名を入力"と書かれたテキストの横の入力フォームに`pip install`の後ろに続くライブラリ名を入力  
例：NumPyをインストールする場合、通常はコマンドプロントで`pip install numpy`と記述するので入力フォームには`numpy`とのみ入力

6. `依存関係を記録`をクリック（任意）  
依存関係を記録するとrequirements.txtが生成されます


## 使用技術
### 言語
* `Python 3.12.9`

### ライブラリ
- `os`
- `subprocess`
- `tkinter`
  - `tkinter.ttk`
  - `tkinter.filedialog`
  - `tkinter.messagebox`
- `threading`
- `Pyinstaller`
