import tkinter as tk
from utils import removeBgr, shortLink
from tkinter import filedialog

main = tk.Tk()
main.geometry('1000x800')
main.title('APP Da Nang=)))')









def rm12():
    input = filedialog.askopenfilename(title='Select Image', filetypes=[("Image File", "*")])
    if not input:
        return
    output = str(input).split('.')[0] + 'rmbgr.' + str(input).split('.')[1]
    remo = removeBgr.rm1(input, output)
    remo.run()
    tk.Label(main, text='vui long cho...').grid(column=1, row=0)
    print('Xong')
    tk.Label(main, text=f'Anh cua ban duoc luu tai {output}').grid(row=0, column=1)

def shortLINK():
    link = tk.StringVar()
    frame = tk.Frame(main)
    frame.grid(row=1, column=1, columnspan=2)
    tk.Entry(frame, width=50, textvariable=link).pack(side=tk.LEFT, padx=5)
    tk.Label(frame, text="<-Nhap | Xuat->").pack(side=tk.LEFT, padx=5)
    resultText = tk.Entry(frame, width=50)
    resultText.pack(side=tk.LEFT, padx=5)
    def shorted():
        sl = shortLink.short(link.get())
        url = sl.run()
        print(url)
        resultText.delete(0, tk.END) 
        resultText.insert(0, url)  
        resultText.config(state='readonly')

    tk.Button(frame, text='Short', command=shorted).pack(side=tk.LEFT, padx=5)


# def downmp3():
#     link = tk.StringVar()
#     frame = tk.Frame(main)
#     frame.grid(row=2, column=1, columnspan=2)
#     tk.Entry(frame, width=50, textvariable=link).pack(side=tk.LEFT, padx=5)


    
#     def dow():
#        yt = youtobe.ytb(link.get())
#        yt.mp3('name')

#     tk.Button(frame, text='Download', command=dow).pack(side=tk.LEFT, padx=5)
    
    

    



def ui():
    tk.Button(main, text='Remove', command=rm12).grid(row=0, column=0)
    tk.Button(main, text='Short Link', command=shortLINK).grid(column=0, row=1)
    # tk.Button(main, text='Download MP3', command=downmp3).grid(column=0, row=2)
ui()
main.mainloop()
print("Success")

