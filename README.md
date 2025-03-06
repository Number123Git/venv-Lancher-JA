# venv Lancher-JA-ver.1.0.0  
## 概要  

Pythonのみで作られた一瞬でvenv環境を構築できるソフト。  
いちいちコマンドプロントで記述して実行する必要がなくなります。    
<p align="center">
  <img src="https://github.com/user-attachments/assets/66fb80f6-048b-49ee-aef2-0cbbf49ab7c8" width="35%" alt="使用画面">
</p>

## 必要・推奨スペック
### 必要スペック
* OS: Windows 7 SP1 以降 (32ビットおよび64ビット)
* CPU: 1 GHz 以上のプロセッサ
* メモリ: 1 GB RAM
* ディスク空き容量: 50 MB 以上

### 推奨スペック
* OS: Windows 10 以降 (64ビット)
* CPU: 2 GHz 以上のデュアルコアプロセッサ
* メモリ: 4 GB RAM 以上
* ディスク空き容量: 100 MB 以上


## 機能（ver.1.0.0）

* venv環境の構築
* 環境内へのライブラリのインストール
* 依存関係の記録


## 使い方
1. ここをクリックしてダウンロード
1. "出力フォルダを選択"と書かれたテキストの横にある"選択"ボタンをクリック  
➤出力フォルダを選択

2. "インストールするパッケージ名を入力"と書かれたテキストの横の入力フォームに`pip install`の後ろに続くライブラリ名を入力  
例：NumPyをインストールする場合、通常はコマンドプロントで`pip install numpy`と記述するので入力フォームには`numpy`とのみ入力

3. `依存関係を記録`をクリック（任意）  
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
