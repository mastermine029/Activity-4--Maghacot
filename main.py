import cv2
import os

os.system("cls")

def menu():
    path = "eyy.jpg"
    show = """
Image View

1 - View provided image
2 - Use your own image """
    print(show)
    usein = int(input(": "))
    
    if usein == 1:
        os.system("cls")
        usein = int(input("1 - Colored \n2 - Grayscale \n: "))
        if usein == 1:
            image = cv2.imread(path, 1)
            cv2.imshow("Kenneth: Pag-Asa ng Carissa", image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        elif usein == 2:
            os.system("cls")
            image = cv2.imread(path, 0)
            cv2.imshow("Kenneth: Wanted ng Carissa", image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        else:
            os.system("cls")
            exit()
        
    elif usein == 2:
        os.system("cls")
        print("Input complete Filepath of your image. Take note: The program may 'FAIL' if the input is wrong or incomplete!")
        path1 = input("Filepath:")
        usein = int(input("1 - Colored \n2 - Grayscale \nRead image as: "))
        if usein == 1:
            image = cv2.imread(path1, 1)
            cv2.imshow("Colored Image", image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        elif usein == 2:
            os.system("cls")
            image = cv2.imread(path1, 0)
            cv2.imshow("Grayscale Image", image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        else:
            exit()
    else:
        print("Wrong Input. Hit enter to continue")
        usein=(input(""))
        menu()

menu()

