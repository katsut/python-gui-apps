import tkinter as tk
import random

# ↓↓↓ お約束のコード ↓↓↓
window = tk.Tk()
window.title("GUI App")
window.geometry("600x400")
bg_color = "#333333"  # ダークグレー
fg_color = "#FFFFFF"  # 白
window.configure(bg=bg_color)
# ↑↑↑ お約束のコード ↑↑↑

word_list = [
    "今日はとてもいい天気です。",
    "明日の宿題を早めに終わらせよう。",
    "公園でジョギングを楽しんだ。",
    "友達と映画を見に行きます。",
    "新しい本を読むのが楽しみです。",
    "美味しいケーキを作りました。",
    "猫が窓から外を見ています。",
    "緑の草原が広がっている。",
    "海の波が静かに寄せている。",
    "朝の散歩でリフレッシュした。",
]


def button_action():  # 関数の定義 ※ボタンが押されたときの動き
    user_input = entry1.get()  # 入力値を取得
    # if label1.cget("text") == user_input:  # XXX ラベルの文字を取得する
    if properties["current"] == user_input:
        current_word = random_choice(word_list)
        properties["current"] = current_word
        properties["count"] = properties["count"] + 1
        label1.config(text=current_word)  # 画面に出力
        label2.config(text=f"正解数: {properties['count']}")
        entry1.delete(0, tk.END)  # Entryの文字を削除


def return_action(event):
    button_action()


def random_choice(words):  # 関数の定義 ※ボタンが押されたときの動き
    index = random.randint(0, len(words) - 1)
    return words[index]


current = random_choice(word_list)
properties = {"current": current, "count": 0}


# 出力ラベルの作成
label1 = tk.Label(window, text=current, bg=bg_color, fg=fg_color)
label1.pack(pady=10)

label2 = tk.Label(window, text="正解数:", bg=bg_color, fg=fg_color)
label2.pack(pady=10)

# 入力フィールドの作成
entry1 = tk.Entry(window, bg=fg_color, fg=bg_color)
entry1.pack(pady=10)
entry1.bind("<Return>", return_action)
# ボタンの作成
button1 = tk.Button(window, text="OK", command=button_action)
button1.pack(pady=10)


# ↓↓↓ お約束のコード ↓↓↓
window.mainloop()
# ↑↑↑ お約束のコード ↑↑↑
