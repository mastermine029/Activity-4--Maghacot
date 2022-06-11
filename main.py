import cv2
import os

os.system("cls")

def menu():
    filepath1 = "eyy.jpg"

    show = """
Image View

1 - View provided image
2 - Use your own image """
    print(show)
    usein = int(input(": "))
    
    if usein == 1:
        os.system("cls")
        usein = int(input("1 - Color \n2 - Grayscale \n: "))
        if usein == 1:
            image = cv2.imread(filepath1, 1)
            cv2.imshow("Kenneth: Pag-Asa ng Carissa", image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        elif usein == 2:
            os.system("cls")
            image = cv2.imread(filepath1, 0)
            cv2.imshow("Kenneth: Wanted ng Carissa", image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        else:
            os.system("cls")
            exit()
        
    elif usein == 2:
        os.system("cls")
        filepath2 = input("Please Enter Complete and Correct Filepath of your Image:")
        usein = int(input("1 - Color \n2 - Grayscale \n3 - Unchanged \nRead image as: "))
        if usein == 1:
            image = cv2.imread(filepath2, 1)
            cv2.imshow("Your Image in Color", image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        elif usein == 2:
            os.system("cls")
            image = cv2.imread(filepath2, 0)
            cv2.imshow("Your Image in Grayscale", image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        else:
            exit()
    else:
        print("Please choose between 1 and 2 only")
        menu()

menu()

