from params import *
from Tkinter import *
from PIL import Image, ImageTk
from random import randint
import os



def list_images():
    """"
    List the images that are stored in IMAGES_PATH except '.DS_Store'
    """

    list_images = os.listdir(IMAGES_PATH)
    if '.DS_Store' in list_images:
        list_images.remove('.DS_Store')

    return list_images


def create_window():
    """"
    Create a tk window with panels
    """

    window = Tk()
    p = PanedWindow(window, orient=HORIZONTAL)
    p.pack()
    return p


def open_image(name_img_file):
    """"
    Open the image that are stored in IMAGES_PATH/name_img_file and resize it
    """

    image = Image.open("{}/{}".format(IMAGES_PATH, name_img_file))
    image = image.resize((300, 200), Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(image)
    return photo

def generate_list_photos(list_images, n=2):
    """"
    Generate a list of tk photos of length n based on the list of images names
    """

    list_photos = [open_image(list_images[randint(0, len(list_images) - 1)]) for i in range(n)]
    return list_photos


def display_images(panned_window, list_photos):
    """"
    Display images from list_photos in panned_window
    """

    for photo in list_photos:
        panned_window.add(Label(panned_window, image=photo, anchor=CENTER))
    panned_window.pack()
    return panned_window


def main():
    p = create_window()
    out = list_images()
    print out
    list_photos = generate_list_photos(list_images=out)
    panned_window = display_images(p, list_photos)
    mainloop()


if __name__ == "__main__":
    main()





