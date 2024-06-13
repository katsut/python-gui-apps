import tkinter as tk

# ↓↓↓ お約束のコード ↓↓↓
window = tk.Tk()
window.title("GUI App")
window.geometry("600x400")
bg_color = "#333333"  # ダークグレー
fg_color = "#FFFFFF"  # 白
window.configure(bg=bg_color)
# ↑↑↑ お約束のコード ↑↑↑


def convert_to_wareki():  # 関数の定義 ※ボタンが押されたときの動き
    seireki = int(entry1.get())  # 入力値を取得

    # 和暦の各元号の開始年を調べる
    meiji = 1868  # 明治
    taisho = 1912  # 大正
    showa = 1926  # 昭和
    heisei = 1989  # 平成
    reiwa = 2019  # 令和

    # 元号を判定する
    if seireki < taisho:
        gengo = "明治"
        wareki = seireki - meiji + 1
    elif seireki < showa:
        gengo = "大正"
        wareki = seireki - taisho + 1
    elif seireki < heisei:
        gengo = "昭和"
        wareki = seireki - showa + 1
    elif seireki < reiwa:
        gengo = "平成"
        wareki = seireki - heisei + 1
    else:
        gengo = "令和"
        wareki = seireki - reiwa + 1

    # 1年の場合は元年にする
    if wareki == 1:
        wareki = "元"

    label1.config(text=f"西暦 {seireki}年 は {gengo} {wareki}年です。")  # 画面に出力


# 入力フィールドの作成
label0 = tk.Label(window, text="西暦を入力して", bg=bg_color, fg=fg_color)
label0.pack(pady=10)

entry1 = tk.Entry(window, bg=fg_color, fg=bg_color)
entry1.pack(pady=10)

# ボタンの作成
button1 = tk.Button(window, text="和暦に変換", command=convert_to_wareki)
button1.pack(pady=10)


# 出力ラベルの作成
label1 = tk.Label(window, text="", bg=bg_color, fg=fg_color)
label1.pack(pady=10)

# ↓↓↓ お約束のコード ↓↓↓
window.mainloop()
# ↑↑↑ お約束のコード ↑↑↑
