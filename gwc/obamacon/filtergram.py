import filters

def main():
    imagenames = ['capamerica', 'obamaphone', 'obamababy', 'obamababy2', 'obamababy3']
    print("What image would you like to edit?")
    print(imagenames)
    filename = input("Which image would you like to edit? ")

    # load the image from the file picked
    original_img = filters.load_img(filename)
    original_img.show()

    filtered_img = filters.obamacon(original_img)
    filtered_img.show()

if __name__ == '__main__':
    main()
