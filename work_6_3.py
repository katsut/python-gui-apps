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

# マルバツを記憶しておく二次元リスト
matrix = [["", "", ""], ["", "", ""], ["", "", ""]]
# マルバツの位置とボタンの位置を紐づける二次元リスト
buttons = [[None, None, None], [None, None, None], [None, None, None]]


class MarkSettings:
    def __init__(self):
        self.player = ""
        self.computer = ""
        self.reset_mark()

    def reset_mark(self):
        if random.randint(0, 1) == 0:
            self.player = "O"
            self.computer = "X"
        else:
            self.player = "X"
            self.computer = "O"


# プレイヤーとコンピュータのマークを設定
mark = MarkSettings()


# リセットボタンが押されたときの動き
def reset():
    mark.reset_mark()
    message_label.config(text="")
    marker_label.config(text=f"あなたは {mark.player} です")

    for row in range(3):
        for col in range(3):
            matrix[row][col] = ""
            buttons[row][col].config(text="")
    # 後攻だったら先にコンピュータが打つ
    if mark.player == "X":
        choice_empty_cell(mark.computer)


# 勝利判定
def check_winner(mark) -> bool:
    for i in range(3):
        for j in range(3 - i):
            # 縦ライン
            if i == 0:
                if mark == matrix[i][j] == matrix[i + 1][j] == matrix[i + 2][j]:
                    return True
            # 横ライン
            if j == 0:
                if mark == matrix[i][j] == matrix[i][j + 1] == matrix[i][j + 2]:
                    return True
    # 斜めライン
    if mark == matrix[0][0] == matrix[1][1] == matrix[2][2]:
        return True
    if mark == matrix[0][2] == matrix[1][1] == matrix[2][0]:
        return True

    return False


def marking_cell(row, col, mark):
    matrix[row][col] = mark  # マトリックスに記録
    buttons[row][col].config(text=mark)  # ボタンのラベルを変える


def choice_empty_cell(mark):
    # 最初に空いてたところに入れる
    for row in range(3):
        for col in range(3):
            if matrix[row][col] == "":
                marking_cell(row, col, mark)
                return row, col
    return 0, 0  # ここには来ないはず


# ボタンが押されたときの動き(Indexが渡される)
def button_action(row, col):

    # 場所がマーキングされていない場合だけ
    if matrix[row][col] == "":
        # ボタンのラベルを変える
        marking_cell(row, col, mark.player)

        # 勝利判定
        if check_winner(mark.player):
            message_label.config(text="あなたの勝ちです！")

        else:
            # 相手のターンを実行する
            choice_empty_cell(mark.computer)
            # 相手の勝利判定
        if check_winner(mark.computer):
            message_label.config(text="コンピュータの勝ちです！")

    # 指定済みだったら何もしない


# --- UI部品の作成 ---
# 出力ラベルの作成
message_label = tk.Label(window, text=" ", bg=bg_color, fg=fg_color)
message_label.pack(pady=10)

marker_label = tk.Label(
    window, text=f"あなたは {mark.computer} です", bg=bg_color, fg=fg_color
)
marker_label.pack(pady=10)

# ボタンの作成
button1 = tk.Button(window, text="Reset", command=reset)
button1.pack(pady=10)

# ボタンを配置するフレーム
matrix_frame = tk.Frame(window)
matrix_frame.pack(pady=0)

# ボタンの作成
for row in range(3):
    for col in range(3):
        button = tk.Button(  # ラムダ式で関数に引数を渡す書き方。９個の関数を個別に定義しても良い
            matrix_frame, text="", command=lambda r=row, c=col: button_action(r, c)
        )
        button.grid(row=row, column=col)
        buttons[row][col] = button


# ↓↓↓ お約束のコード ↓↓↓
window.mainloop()
# ↑↑↑ お約束のコード ↑↑↑
