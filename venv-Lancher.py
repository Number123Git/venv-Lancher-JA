import sys
import os
import subprocess
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import threading

def on_click():
    output_dir_path.set(filedialog.askdirectory())

def create_venv():
    if not output_dir_path.get():
        messagebox.showerror("エラー", "出力フォルダを選択してください")
        return

    def task():
        try:
            progress_bar["value"] = 0
            progress_bar["maximum"] = 3
            progress_bar.grid(row=5, column=0, columnspan=3, pady=10)
            root.update_idletasks()

            steps = [
                ("仮想環境を作成中...", create_virtual_env),
                ("パッケージをインストール中...", install_packages),
                ("依存関係を記録中...", record_requirements if check_var.get() else None),
            ]

            for i, (_, action) in enumerate(steps):
                if action:
                    root.update_idletasks()
                    action()
                    progress_bar["value"] = i + 1

            root.update_idletasks()
            progress_bar.grid_remove()
            messagebox.showinfo("完了", "仮想環境のセットアップが完了しました")
        except Exception as e:
            root.update_idletasks()
            progress_bar.grid_remove()
            messagebox.showerror("エラー", str(e))

    threading.Thread(target=task).start()

def create_virtual_env():
    venv_path = os.path.join(output_dir_path.get(), 'venv')
    subprocess.run(["python", "-m", "venv", venv_path])

def install_packages():
    venv_path = os.path.join(output_dir_path.get(), 'venv')
    pip_path = os.path.join(venv_path, "Scripts", "pip")
    packages = package_entry.get().strip()
    if packages:
        subprocess.run([pip_path, "install"] + packages.split())

def record_requirements():
    venv_path = os.path.join(output_dir_path.get(), 'venv')
    pip_path = os.path.join(venv_path, "Scripts", "pip")
    requirements_path = os.path.join(output_dir_path.get(), 'requirements.txt')
    with open(requirements_path, 'w') as f:
        subprocess.run([pip_path, "freeze"], stdout=f)



root = tk.Tk()

root.title("venv Launcher")
root.geometry("335x250")
root.resizable(False, False)

# ウィンドウを画面中央に配置
window_width, window_height = 335, 250
screen_width, screen_height = root.winfo_screenwidth(), root.winfo_screenheight()
position_top = int(screen_height / 2 - window_height / 2)
position_right = int(screen_width / 2 - window_width / 2)
root.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')

# vl-icon.icoのbase64エンコード結果
data = '''R0lGODlhAAEAAfQAAAAAAAAAAAEAAAABAAEBAAAAAQEAAQABAQEBAQICAgMCAgID
AgICAwMCAwMDAwQEBAQFBAUFBAUEBQUFBQYGBgcHBwgICAkJCQoKCgsKCgsLCwwM
DAAAAAAAAAAAAAAAACH5BAEAAAAALAAAAAAAAQABAAX/ICCOZGmeaKqubOu+cCzP
dG3feK7vfO//wKBwSCwaj8ikcslsOp/QqHRKrVqv2Kx2y+16v+CweEwum8/otHrN
brvf8Lh8Tq/b7/i8fs/v+/+AMAmDhIWGh4iJiouMjY6PFCuKFAmBPgmUhZmPnJ2e
n5CYK5Sbh5Y8g5QXoKytrp+RKqmImac6iKulr7u8raOEuoW2N4OrvcfInMbCkozG
wzXJ0tOezcCL0DPU29yJLNXZgt3j1LWy4OEt5OvHmaTNwbSi6ZLx7PehzCmYs4ub
sfRQ4BsIikIpa43cDQoo8BrBh48u1LPHCCDDERAz5vvlMFGwiyQ0inT0jZ8ng5VA
/wI4OfKexRPyOqlsRaolNxY1KTa6+MnYP5vSVq3I5XAZJ4YJjEbsCLSXuX39krIK
yEphU2kvTdTspxNbul1br4JNCbXdV1f0XGUNpJZsNpNTh+ULi3SWVY+Ehv3stPat
oa4mJZ4CbPcgT2Bhd1rSRFjfYU66FqOdCdkUILUqR+h6kDCvn2uEc2YWEXWStz6l
/fUbjVETOj1wP7EOOVlPY0PPZpO+bTnPK920WQnGU3UhcNK17Qza4CnX8eCw3M5J
ffQ59MrG6fy23ppvqr5ttnPv7j17HPHjVyZ/U/BpeuS8HbdBGbr3e/WuIYE/U9qe
QoP3leCQf/m9oUp+qkkXoP96gJWSGxuFKJXQgiXEZ1R4sTU4D4UkJIaXfWggWJFn
HHbXmGFpYFaigDSlKBUoK8K03hjxGRKjCbG9NkaOMt2IY0HmiaGijx3O+AU/KOlI
JHLRKdgFjz0ueR1LQjL1iJQy+gIGKMtg2ZCWXqDnJUYSVvdki2PKWGOQWYiZJpNx
beHmm/DFicWL5dFZVnRaQHmlnlnaWYWfJAH6paBTzGkoftTF5CQUhFa0KFSldLXJ
oIF5N+mhCTAXqY1T7BXlpj8apeF+SRQ1Kqk/Vpogm0woyupKa1ISxadezcrpq/wM
14SsurIknxLA6orfmr8WG2ySNcbaE4nG7kklsWvCGi3/jtU+KoSy13LLQ7baXltC
mWYScZeS4gbKZxFDposQjERw4gAi7r5wSJIxuQdEoyIOWy8K8Wg4hLf/MtqZJtv2
q3C4BU+Jq76oFPMpvgw3fJ2loPZw7qoWSzsixZeomiCqHReJK70RC1txycHptHHK
iLLsMbo0SDytzC4IZ60MFG+Ec878TkKyOiej/DPQTRKj89ExECwjuYoxnXONENub
rdRNF1ezkVjPzDHRYHYNNNSMZK212C9sXG5JYaPdArj2lle1280YQ/a9SCsDDN1m
FwS23vzwzXPRIKqrqeDiVPUudojLELQ/KXi4duN5w/sj4f5SXo/i2FaruTbPspnJ
/92nfS4I1UE6bTp5sJgY8+qLO2IYVzTDHjtkAMBtO+j5uOb57o6jRfvXwHsNCZO1
Fv92k9nprvw5nGv2uCLP74O6gpj8Xv3lnXR5ObLbh1RtX9Pfu3PxsmKe8fbtGl47
7NmSXKP31fd6M/Rc1n/1344oVX+E72MRdqBlO+fxb0R2WRnddtE3y8FOdXBy4OcM
KA7tmY4mCnQf8fhWnAyeQHKNEIrpKBi86DWugzkoH27Oh7VMzOtwOMAg5bLXHBYm
zm+CI6ENgGTDn1npL6nRmMgUYTe+qc00PWygBKXmHZCFTCoYy5wPF5arJwYtHmJz
FBITprIsDpCAVuSVFDv2If/VxKt3Y7SYFoFoEnah6Wc6/MERCyWzthwhjgWDoNLa
1jA9EmN/JfPjHrsHxnoRgnRGS1X73AUuD/ZAkHSCZAq5Ziz1pZFdc6xiuqLzDkhR
klVIup8TBrRBUGYILyiCwiYQub5K4ulhSTTCCivTrUJ46jaDGl8tXfWqK6gQiK78
IeR8+Uk9SZKLOCQVHm91vVn90jVyKqaXjulGPr7pO0vEwviGRiRWlo4LzHMkh6h5
BC4Vcpo2C6AVqKhJdFpTTsuMkStEGAYkNStNKCTDPMcUT3i+U5485E9ApfTMVu7o
laWkEDmfsMgSxW8N7PSIj4SpRQidspc3OhkWLWozDYn/kzXLcNlyLimGA1G0KPKs
zyFjuaWL0nFBViGQQ+AQyjwtyHz6OU95zmmdgpLUDDzkZmb6GSJpsoaHH63SP2fT
JADVIYHqzMxCwdkplvjqODIkjjmTaouTtlM7zOtpK65qh1ptiKk+PStxADkbEL7U
N3ARaRvR6tVEwgaqslPrRdy6MKHS9It6ZYguPMpVjr4uHDvlKVzTKtXEFnY+oXBi
XbApV5bSQVTHe0x5yPqHucBlsiatLDTqKo+0eLMjflnqZYzKB6ewsJFiiWhCOxtU
hOEvtq61pGVhc9p0pmIUsMXtIXorlckC7ie/CG5s90JczbLEVipQrnBrmk3EEtKg
oCyS7nR92lji2nC7GZnbWQ4rAu2C16ZD7eI5Mnneafj1FB3tzOZ0297N7tYSvBFv
eetLkPfagq+FE1DP+LuNTgKnf7+NrmwJzAuxYswa5mUwTrmTWeNJeBrj8S3ebndh
ZDxIrKbhSIe7cR9JySLCI/5pY0t74hTfJEB4ma+LpRG+Gtv4xjjOsY53zOMe+/jH
QA6ykIdM5CIb+chITnIdQgAAOw==
'''

root.tk.call('wm', 'iconphoto', root._w, tk.PhotoImage(data=data))


# 出力フォルダ選択
output_dir_path = tk.StringVar()

# ラベルの作成
tk.Label(root, text="出力フォルダを選択").grid(row=0, column=0)
tk.Entry(root, state="readonly", textvariable=output_dir_path).grid(row=0, column=1)
tk.Button(root, text="選択", command=on_click).grid(row=0, column=2)

# パッケージ入力
tk.Label(root, text="インストールするパッケージ名を入力").grid(row=1, column=0)
package_entry = tk.Entry(root)
package_entry.grid(row=1, column=1)

# 依存関係記録ファイルの作成の有無
check_var = tk.IntVar()
tk.Checkbutton(root, text="依存関係を記録", variable=check_var).grid(row=2, column=0, columnspan=3, sticky="we")

# 実行ボタンの作成
tk.Button(root, text="実行", command=create_venv, width=20).grid(row=3, column=0, columnspan=3, pady=10)

# 進捗バー
progress_bar = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate")
progress_bar.grid(row=5, column=0, columnspan=3, pady=10)

# 進捗ラベル
tk.Label(root, text="").grid(row=4, column=0, columnspan=3)

root.mainloop()