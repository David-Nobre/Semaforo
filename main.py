import tkinter as tk

board = [ ['white']*4 for _ in range(4) ]

counter = 0

root = tk.Tk()

def on_click(i,j,event) -> bool:
    match board[i][j]:
        case 'white' : color = 'green'
        case 'green' : color = 'yellow'
        case 'yellow' : color = 'red'
        case 'red' : return False
    event.widget.config(bg=color)
    board[i][j] = color
    return True


for i,row in enumerate(board):
    for j,column in enumerate(row):
        L = tk.Label(root,text='\t\n\t\n\t\n\t\n\t',bg='white')
        L.grid(row=i,column=j)
        L.bind('<Button-1>',lambda e,i=i,j=j: on_click(i,j,e))

root.mainloop()