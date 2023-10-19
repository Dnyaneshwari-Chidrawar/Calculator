import tkinter as tk
from tkinter import messagebox

def button_click(row, col):
    global user_input
    new_input = board[row][col]
    if new_input == '<-':
        user_input = user_input[:-1]
    elif new_input == 'C':
        user_input = ""
    elif new_input == '=':
        ans = calculator_output()
        messagebox.showinfo('Ans',str(ans))
        user_input = ""
    elif new_input in ['%','/','*','-','+'] and user_input[-1] in ['%','/','*','-','+']:
        print("check here")
        user_input = user_input[:-1]
        user_input += new_input
    else:
        user_input += new_input
    label.config(text=user_input)


def calculator_output():
    global user_input
    # length = len(user_input)
    ans, num, j = 0, "", 0
    nums = []
    ops = []
    for item in user_input:
        if item in ['%','/','*','-','+']:
            ops.append(item)
            nums.append(float(num))
            num = ""
        else:
            num += item
    if len(num) != 0:
        nums.append(float(num))
    print('nums=', nums,'ops=',ops)
    ans = nums[0]
    for i in range(len(ops)):
        if ops[i] == '+':
            ans += nums[j + 1]
        elif ops[i] == '-':
            ans -= nums[j + 1]
        elif ops[i] == '*':
            ans *= nums[j + 1]
        elif ops[i] == '/':
            ans /= nums[j + 1]
        elif ops[i] == '%' :
            ans = ans / 100
        j += 1

    if ans == int(ans):
        return int(ans)
    else:
        return round(ans, 2)


# Create the main application window
root = tk.Tk()
root.title("My Calculator GUI")

# Create the label at the top
label = tk.Label(root, height=3,text="", font=18)
label.pack()

# Create a frame to conatain the button grid
frame = tk.Frame(root)
frame.pack()

board, user_input = [], ""
operations = ['C', '%', '<-', '/', '*','-','+','=']
count_ops = 0

numbers = ['7','8','9','4','5','6','1','2','3','00','0','.']
count_num = 0
# Create the button grid 4*5
for i in range(5):
    row = []
    for j in range(4):
        if i == 0 or j == 3:
            button = tk.Button(frame, text=operations[count_ops], command=lambda row=i, col=j: button_click(row, col))
            button.grid(row=i, column=j, padx=5, pady=5)
            row.append(operations[count_ops])
            count_ops += 1
        else:
            button = tk.Button(frame, text=numbers[count_num], command=lambda row=i, col=j: button_click(row, col))
            button.grid(row=i, column=j, padx=5, pady=5)
            row.append(numbers[count_num])
            count_num += 1
    board.append(row)

root.mainloop()