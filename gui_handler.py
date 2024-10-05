import tkinter as tk
from tkinter import ttk

def select_question(questions):
    root = tk.Tk()
    root.title("Select Research Question")
    
    selected = tk.StringVar()
    
    for i, question in enumerate(questions):
        ttk.Radiobutton(root, text=question, variable=selected, value=question).pack(anchor='w')
    
    ttk.Button(root, text="Submit", command=root.quit).pack()
    
    root.mainloop()
    root.destroy()
    
    return selected.get()

def select_keywords(keywords):
    root = tk.Tk()
    root.title("Select Keywords")
    
    selected_keywords = []
    
    for keyword in keywords:
        var = tk.BooleanVar()
        ttk.Checkbutton(root, text=keyword, variable=var, command=lambda v=var, k=keyword: selected_keywords.append(k) if v.get() else selected_keywords.remove(k)).pack(anchor='w')
    
    ttk.Button(root, text="Submit", command=root.quit).pack()
    
    root.mainloop()
    root.destroy()
    
    return selected_keywords

def select_articles(articles):
    # Similar implementation to select_keywords, but for articles
    pass