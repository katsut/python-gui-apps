import tkinter as tk

# ↓↓↓ お約束のコード ↓↓↓
window = tk.Tk()
window.title("GUI App")
window.geometry("600x400")
bg_color = "#333333"  # ダークグレー
fg_color = "#FFFFFF"  # 白
window.configure(bg=bg_color)
# ↑↑↑ お約束のコード ↑↑↑


def add_button_action():  # 関数の定義 ※ボタンが押されたときの動き
    num1 = int(entry1.get())  # 入力値を取得
    num2 = int(entry2.get())  # 入力値を取得
    label1.config(text=f"{num1} + {num2} = {num1 + num2}")  # 画面に出力


def sub_button_action():  # 関数の定義 ※ボタンが押されたときの動き
    num1 = int(entry1.get())  # 入力値を取得
    num2 = int(entry2.get())  # 入力値を取得
    label1.config(text=f"{num1} - {num2} = {num1 - num2}")  # 画面に出力


def mul_button_action():  # 関数の定義 ※ボタンが押されたときの動き
    num1 = int(entry1.get())  # 入力値を取得
    num2 = int(entry2.get())  # 入力値を取得
    label1.config(text=f"{num1} × {num2} = {num1 * num2}")  # 画面に出力


def div_button_action():  # 関数の定義 ※ボタンが押されたときの動き
    num1 = int(entry1.get())  # 入力値を取得
    num2 = int(entry2.get())  # 入力値を取得
    label1.config(text=f"{num1} ÷ {num2} = {num1 / num2}")  # 画面に出力


# 入力フィールドの作成
entry1 = tk.Entry(window, bg=fg_color, fg=bg_color)
entry1.pack(pady=10)
entry2 = tk.Entry(window, bg=fg_color, fg=bg_color)
entry2.pack(pady=10)

# ボタンの作成
button1 = tk.Button(window, text="+", command=add_button_action)
button1.pack(pady=10)
button2 = tk.Button(window, text="-", command=sub_button_action)
button2.pack(pady=10)
button3 = tk.Button(window, text="×", command=mul_button_action)
button3.pack(pady=10)
button4 = tk.Button(window, text="÷", command=div_button_action)
button4.pack(pady=10)

# 出力ラベルの作成
label1 = tk.Label(window, text="", bg=bg_color, fg=fg_color)
label1.pack(pady=10)

# ↓↓↓ お約束のコード ↓↓↓
window.mainloop()
# ↑↑↑ お約束のコード ↑↑↑
