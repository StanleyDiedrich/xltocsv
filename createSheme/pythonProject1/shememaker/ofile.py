from tkinter import filedialog as fd

def openfile():
    filetypes = (
        ('text files', '*.xlsm'),
        ('All files', '*.*')
    )

    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes)
    return filename





