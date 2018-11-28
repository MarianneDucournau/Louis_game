from params import *
from Tkinter import *
from PIL import Image, ImageTk
from random import sample
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


def generate_list_random_int(list_images, n=2):
    """"
    Generate a list of unique random int of length n based on the length of list of images names
    """

    assert (n <= len(list_images))

    list_random_int = sample(range(0, len(list_images) - 1), n)
    return list_random_int


def generate_one_random_int(list_random_int):
    """"
    Generate a random int from list_random_int
    """

    one_random_int = sample(list_random_int, 1)
    return one_random_int


def generate_list_photos(list_images, list_random_int):
    """"
    Generate the list of tk photos based on the list of images names and the list of random int
    """

    list_photos = [open_image(list_images[i]) for i in list_random_int]
    return list_photos


def display_images(panned_window, list_photos):
    """"
    Display images from list_photos in panned_window
    """

    for photo in list_photos:
        panned_window.add(Label(panned_window, image=photo, anchor=CENTER))
    panned_window.pack()
    return panned_window


def display_question(panned_window, one_int, list_images):
    """"
    Display question in panned_window
    """

    panned_window.add(Label(panned_window, text='Montre la couleur {}'.format(list_images[one_int[0]]), anchor=CENTER))
    panned_window.pack()
    return panned_window


def main():
    window = create_window()
    image_names = list_images()
    print image_names
    random_int = generate_list_random_int(list_images=image_names)
    print(random_int)
    photos = generate_list_photos(list_images=image_names, list_random_int=random_int)
    panned_window = display_images(window, photos)
    one_int = generate_one_random_int(random_int)
    panned_window = display_question(panned_window, one_int, image_names)
    print(image_names[one_int[0]])
    mainloop()


if __name__ == "__main__":
    main()





