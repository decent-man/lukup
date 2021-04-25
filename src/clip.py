import pyperclip

def clipcopy():
    data = pyperclip.paste()
    print(data)
    return data
