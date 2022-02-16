import tkinter as tk

CORRECT_ANSWER = 'Some answer'

def callback():

    if var.get() != CORRECT_ANSWER:
        for i in range(10, 50):
            canvas.move(text, -i if i% 2 == 0 else i, 0)
            canvas.update()
            canvas.move(text, i if i % 2 == 0 else -i, 0)                     
            canvas.update()

if __name__ == '__main__':

    root = tk.Tk()
    var = tk.StringVar()
    canvas = tk.Canvas(root, bg="black")
    canvas.pack(fill=tk.BOTH, expand=1)
    text = canvas.create_text(200, 100, text='Enter the answer to this question.',
        fill='white')
    entry = tk.Entry(root, textvariable = var)
    entry.pack(side=tk.LEFT, fill=tk.X, expand=1)
    submit = tk.Button(root, text='Submit', command=callback)
    submit.pack(side=tk.LEFT, fill=tk.X, expand=1)
    root.mainloop()