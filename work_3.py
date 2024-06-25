import tkinter as tk


# ↓↓↓ お約束のコード ↓↓↓
window = tk.Tk()
window.title("GUI App")
window.geometry("600x400")
bg_color = "#333333"  # ダークグレー
fg_color = "#FFFFFF"  # 白
window.configure(bg=bg_color)
# ↑↑↑ お約束のコード ↑↑↑

# これまでに入力された名前を覚えておくところ
name_list = []


def button_action():  # 関数の定義 ※ボタンが押されたときの動き
    user_input = entry1.get()  # 入力値を取得
    name_list.append(user_input)  # 入力された名前を覚える

    # 配列をそのまま出すのではなく、改行を入れて表示する
    # formatted_str = ""
    # for name in name_list:
    #     formatted_str += f"{name}\n"  # \(バックスラッシュ) の入力方法は option + ¥

    formatted_str = "\n".join(name_list)  # これでも改行を入れることができる

    label1.config(text=formatted_str)  # ここまでに入力された名前を表示する


label0 = tk.Label(window, text="名前を入力してください", bg=bg_color, fg=fg_color)
label0.pack(pady=10)

# 入力フィールドの作成
entry1 = tk.Entry(window, bg=fg_color, fg=bg_color)
entry1.pack(pady=10)

# ボタンの作成
button1 = tk.Button(window, text="追加", command=button_action)
button1.pack(pady=10)

# 出力ラベルの作成
label1 = tk.Label(window, text="", bg=bg_color, fg=fg_color)
label1.pack(pady=10)

# ↓↓↓ お約束のコード ↓↓↓
window.mainloop()
# ↑↑↑ お約束のコード ↑↑↑
