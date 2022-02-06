import ctypes
MessageBox = ctypes.windll.user32.MessageBoxW

def msgBox(liAr):
    if len(liAr) > 0:
        MessageBox(None, '\n'.join(liAr), 'The Following Mangas have been updated', 0)
    else:
        MessageBox(None, "No Mangas have been updated", 'Note', 0)

