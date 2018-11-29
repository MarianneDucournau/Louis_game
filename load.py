from params import *
from Tkinter import *
from PIL import Image, ImageTk
from random import sample
import os
import re



def list_images():
    """"
    List the images that are stored in IMAGES_PATH except '.DS_Store'
    Return eg ['verte.png', 'bleue.png', 'violette.png', 'orange.png', 'jaune.png', 'rouge.png']
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


def list_random_images(list_images, n=2):
    """"
    Generate a list of unique random images of length n based from list_images
    Returns eg ['verte.png', 'orange.png']
    """

    assert (n <= len(list_images))

    list_random_images = sample(list_images, n)
    return list_random_images



def generate_list_photos(list_random_images):
    """"
    Generate the list of tk photos based on list_random_images
    Returns a list of tk obkects
    """

    list_photos = [open_image(image) for image in list_random_images]
    return list_photos


def display_images(panned_window, list_photos):
    """"
    Display images from list_photos in panned_window
    """

    for photo in list_photos:
        panned_window.add(Label(panned_window, image=photo, anchor=CENTER))
    panned_window.pack()
    return panned_window


def display_question(panned_window, one_image):
    """"
    Display question in panned_window
    """

    panned_window.add(Label(panned_window, text='Montre la couleur {}'.format(re.sub('.png', '', one_image[0])), anchor=CENTER))
    panned_window.pack()
    return panned_window


def main():
    window = create_window()
    all_images = list_images()
    print all_images
    random_images = list_random_images(list_images=all_images)
    one_image = list_random_images(list_images=random_images, n=1)
    print random_images; print one_image
    photos = generate_list_photos(list_random_images=random_images)
    panned_window = display_images(window, photos)
    panned_window = display_question(panned_window, one_image)
    mainloop()


if __name__ == "__main__":
    main()





