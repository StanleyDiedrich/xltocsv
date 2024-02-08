import pandas as pd
from tkinter import filedialog as fd
from process import proc

def export():
    df = proc()
    filename = fd.asksaveasfilename()
    df.to_csv(filename, sep=";")
