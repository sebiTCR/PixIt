
import PIL
from PIL import Image
from tkinter import Tk
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import os



ui = Tk()


def pixelise():
    
    image = filedialog.askopenfilename(initialdir = "/",title = "Select image",filetypes = (("PNG","*.png"),("JPG","*.jpg"),("Costum","*.*")))
    # Input image
    input = PIL.Image.open(image)
    width, height = input.size
    pixButton.pack_forget()
    if(width != height):
        PixDif(width, height,input,image)
    else:
        PixSquare(width, height,input,image)

def PixSquare(w,h,input,image):
    rl = Label(ui, text="Resolution")
    rl.pack()
    NewResX = Scale(ui, from_=1, to= w)
    NewResX.pack()
    pixButton1 = Button(ui, text="pixelate", command=lambda : PixelEit(NewResX.get(),NewResX.get(),input,image))
    pixButton1.pack()
    mainloop()



def PixDif(w,h,input,image):
    wl = Label(ui, text="Width")
    wl.pack()
    NewResX = Scale(ui, from_=1, to= w,  orient=HORIZONTAL)
    NewResX.pack()
    wl = Label(ui, text="Height")
    wl.pack()
    NewResY = Scale(ui, from_=1, to= h,  orient=HORIZONTAL)
    NewResY.pack()
    pixButton1 = Button(ui, text="pixelate", command=lambda : PixelEit(NewResX.get(),NewResY.get(),input,image))
    pixButton1.pack()
    mainloop()
    


    
   
def PixelEit(w,h,input,image):
    

  
    output = input.resize((w,h),resample=PIL.Image.NEAREST)
    output = output.resize(input.size,PIL.Image.NEAREST)
    outputDialog = filedialog.askdirectory()
    path = outputDialog +"/" "output_" + os.path.basename(image)
    print(path)
    output.save(path)
    ui.destroy()
    # Get input size

    #print(input.shape)

    # Desired "pixelated" size

    #PixelrateW = Tk.Entry(ui)
    #PixelrateH = Tk.Entry(ui)
    #root.mainloop()
    #pixPrecent = pixelScalePrecent.get()
    #w, h = (width % pixPrecent, height % pixPrecent)
    #if ( w == h):
    #    print("oke")
    



    

    # Initialize output image
Attempt = 0
pixButton = Button(ui, text="select image", command=pixelise)
pixButton.pack()

#def pixlt():
#    image = filedialog.askopenfilename(initialdir = "/",title = "Select image",filetypes = (("JPG","*.jpg"),("PNG","*.png")))
#    pixelise()
    

     





#output = filedialog.askdirectory(initialdir = image,title = "Select output location",filetypes = (("JPG","*.jpg"),("PNG","*.png")))


mainloop()