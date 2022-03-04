import cv2
import numpy as np
import math
import matplotlib.pyplot as plt
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk

img = cv2.imread('0123456789.png', 0)
cells = [np.hsplit(row, 100) for row in np.vsplit(img, 50)]  # hsp:cot  vs vsp:dong => Cat tung anh nho
x = np.array(cells)
print(x.shape)
# ------------------------------------------------------------------------------
listKhong = x[0:5, :100].reshape(-1, 400).astype(np.float32)
listMot = x[5:10, :100].reshape(-1, 400).astype(np.float32)
listHai = x[10:15, :100].reshape(-1, 400).astype(np.float32)
listBa = x[15:20, :100].reshape(-1, 400).astype(np.float32)
listBon = x[20:25, :100].reshape(-1, 400).astype(np.float32)
listNam = x[25:30, :100].reshape(-1, 400).astype(np.float32)
listSau = x[30:35, :100].reshape(-1, 400).astype(np.float32)
listBay = x[35:40, :100].reshape(-1, 400).astype(np.float32)
listTam = x[40:45, :100].reshape(-1, 400).astype(np.float32)
listChin = x[45:50, :100].reshape(-1, 400).astype(np.float32)

def loadData():

    img= cv2.imread('0123456789.png', 0)
    imgnhandang = cv2.imread(filename, 0)
    imgnhandang =cv2.resize(imgnhandang,dsize=(20,20))
    bard = Image.open(filename)
    bardejov = ImageTk.PhotoImage(bard)
    label1 = Label(root, image=bardejov)
    label1.image = bardejov
    label1.place(x=190, y=100)

    cells = [np.hsplit(row, 100) for row in np.vsplit(img, 50)]  # hsp:cot  vs vsp:dong => Cat tung anh nho
    x = np.array(cells)
    x2 = np.array(imgnhandang)
    trainSet = x[:, :100].reshape(-1, 400).astype(np.float32)  # [:,:50] Lay 50 so dau tien
    testSet = x2.reshape(-1, 400).astype(np.float32)
    print(trainSet.shape)
    print(testSet.shape)
    return trainSet, testSet


def calcDistancs(pointA, pointB, numOfFeature=400):
    tmp = 0
    for i in range(numOfFeature):
        tmp += (float(pointA[i]) - float(pointB[i])) ** 2
    return math.sqrt(tmp)


def kNearestNeighbor(trainSet, point, k):
    distances = []
    for item in trainSet:
        distances.append({
            "label": item,
            "value": calcDistancs(item, point)
        })
    distances.sort(key=lambda x: x["value"])
    labels = [item["label"] for item in distances]
    return labels[:k]


def findMostOccur(arr):

    list0 = []
    list1 = []
    list2 = []
    list3 = []
    list4 = []
    list5 = []
    list6 = []
    list7 = []
    list8 = []
    list9 = []
    for item0 in listKhong:
        list0.append(list(item0))
    for item1 in listMot:
        list1.append(list(item1))
    for item2 in listHai:
        list2.append(list(item2))
    for item3 in listBa:
        list3.append(list(item3))
    for item4 in listBon:
        list4.append(list(item4))
    for item5 in listNam:
        list5.append(list(item5))
    for item6 in listSau:
        list6.append(list(item6))
    for item7 in listBay:
        list7.append(list(item7))
    for item8 in listTam:
        list8.append(list(item8))
    for item9 in listChin:
        list9.append(list(item9))

    khong=[0,'số 0 nha bạn !!!']
    mot=[0,'số 1 nha bạn !!!']
    hai = [0, 'số 2 nha bạn !!!']
    ba = [0, 'số 3 nha bạn !!!']
    bon = [0, 'số 4 nha bạn !!!']
    nam = [0, 'số 5 nha bạn !!!']
    sau = [0, 'số 6 nha bạn !!!']
    bay = [0, 'số 7 nha bạn !!!']
    tam = [0, 'số 8 nha bạn !!!']
    chin = [0, 'số 9 nha bạn !!!']

    labels = []
    labels = arr
    print(type(labels))
    labels = np.array(labels)
    print(labels.shape)
    print(type(listBa))
    labels = list(labels)
    a=0
    for label in labels:
        # print(label)
        # print(label.reshape(20,20))
        plt.imsave(f"ketquatest{a+1}.png",label.reshape(20,20), cmap='Greys')
        a = a + 1
    # framAnh = Frame(root)
    d=d=170
    for anh in range(5) :
        bard = Image.open(f'ketquatest{anh+1}.png')
        bardejov = ImageTk.PhotoImage(bard)
        label1=Label(root,image=bardejov)
        label1.image = bardejov
        label1.place(x=d, y=130)
        d=d+20
        # label1.grid(row=4,column=anh+1)

    # framAnh.grid(row=5,column=0)



    print(">>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
    for label in labels:
        label = list(label)
        if label in list0:
            khong[0]=khong[0]+1

    for label in labels:
        label = list(label)
        if label in list1:
            mot[0]=mot[0]+1


    for label in labels:
        label = list(label)
        if label in list2:
            hai[0]=hai[0]+1

    for label in labels:
        label = list(label)
        if label in list3:
            ba[0]=ba[0]+1

    for label in labels:
        label = list(label)
        if label in list4:
            bon[0]=bon[0]+1

    for label in labels:
        label = list(label)
        if label in list5:
            nam[0]=nam[0]+1

    for label in labels:
        label = list(label)
        if label in list6:
            sau[0]=sau[0]+1

    for label in labels:
        label = list(label)
        if label in list7:
            bay[0]=bay[0]+1

    for label in labels:
        label = list(label)
        if label in list8:
            tam[0]=tam[0]+1

    for label in labels:
        label = list(label)
        if label in list9:
            chin[0]=chin[0]+1

    listValues=[khong,mot,hai,ba,bon,nam,sau,bay,tam,chin]
    max=0
    ans=''
    num=0
    listbox.delete(0, END)
    for itemx in listValues:
        print(f"so {num} xuat hien : ", itemx[0], " lan")

        listbox.insert(END, "so {} xuat hien {} lan".format(num,itemx[0]))
        num=num+1
        if itemx[0]>max:
            max=itemx[0]
            ans=itemx[1]
    listbox.insert(END,">>>>>>>>>>>>>>>>>>>>    KQ       <<<<<<<<<<<<<<<<<<<<<<<<<")
    listbox.insert(END,ans)
    print(">>>>>>>>>>>>>>>>>>>>    KQ       <<<<<<<<<<<<<<<<<<<<<<<<<")
    print(ans)

def thucthi():
# if __name__ == "__main__":
    trainSet, testSet = loadData()
    for item in testSet:
        knn = kNearestNeighbor(trainSet, item, 5)
        findMostOccur(knn)

#--------------------------------------------------------------------------


def browseFiles():
    global  filename
    filename = filedialog.askopenfilename(initialdir="/",
                                          title="Select a File",
                                          filetypes=(("Text files",
                                                      "*.*",
                                                      ),
                                                     ("all files",
                                                      "*.*")))

    label_file_explorer.configure(text="File Opened: " + filename)



root=Tk()
root.title("team dep trai")


root.minsize(width=100,height=450)
# root.config(background="pink")
Label(root,text="KNN - handwritten numbers",fg="blue",font=("tahoma",16)).grid(row=0,column=3)
frameOne=Frame(root)

Label(frameOne,text="file image input : ",fg="blue",font=("tahoma",10)).pack(side=LEFT)
Button(frameOne,text="Open",width=6,command=browseFiles,fg='green',font=("tahoma",10)).pack(side=LEFT)
frameOne.grid(row=2,column=0,columnspan=4)

label_file_explorer = Label(root,
                            text="File Explorer using Tkinter",
                            width=100, height=4,
                            fg="blue")

Label(root,text="KET QUA",fg="red",font=("tahoma",16)).grid(row=3,column=3)

listbox=Listbox(root,width=70,height=15,font=("tahoma",10),fg='red')
listbox.grid(row=5,column=3)

Label(root,text="input:",fg="blue",font=("tahoma",10)).place(x=105,y=100)
Label(root,text="KQ-5-KNN:",fg="blue",font=("tahoma",10)).place(x=105,y=130)


Button(root,text="thuc thi",width=6,command=thucthi,fg='green',font=("tahoma",10)).grid(row=6,column=3)
label_file_explorer.grid(column=3, row=1)
root.mainloop()