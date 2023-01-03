from fileinput import close
import os
import turtle as tr
import tkinter as tk
from tkinter import ttk
import Trees as ts
import Flowers as fl
import Grass as gr

main_W = tk.Tk()
main_W.title("Tree drawer 3000")
main_W.geometry('480x270')

tabcontrol = ttk.Notebook(main_W)

main_tab = ttk.Frame(tabcontrol)

presets_list = []
settings_list = []

enable_grass = tk.BooleanVar()
enable_trees = tk.BooleanVar()

enable_grass.set(True)  
enable_trees.set(True)

grass_Para = [[10, 30],[20, 40]] # first column is for grass leaf length and the second for the height parameters
tree_Para = [20, 90, 35, 2]
grass_Para_Str = "10/30/20/40"
tree_Para_Str = "20/90/40/2"
hideTurtle = False
turtleSpeed = 0
startPointPosition = 200
save_file_path = "D:\CodeStuff\Scripte\BaumMaler\SaveFiles"

settings_list.append(hideTurtle)
settings_list.append(turtleSpeed)
settings_list.append(save_file_path)

#Handles all the preset related mechanics like loading, overwritting and saving new presets
class Preset():
    preset_name = ''
    dataframe = ""
    save_file = None
    save_file_name = os.path.join(settings_list[2] + "\\" + preset_name + ".txt")
    
    def __init__(self,name):
        self.preset_name = name
        self.LoadFile()

    #Laods the file and saves it into the dataframe for reading the string from the selected preset
    def LoadFile(self):
        self.save_file_name = os.path.join(settings_list[2] + "\\" + self.preset_name + ".txt")
        if(os.path.exists(self.save_file_name)):
            self.save_file = open(self.save_file_name, "r")
            self.dataframe = self.save_file.read()
            self.save_file.close()
        else:
            self.CreateNewFile()

    #Creates a new file or overwrittes a file when it`s already exist     
    def CreateNewFile(self):
        self.save_file = open(self.save_file_name, "w")
        self.save_file.write(self.dataframe) 
        self.save_file = close()

    def DeleteFile(self):
        os.remove(self.save_file_name)

#Loads all presets at the beginning of the runtime and changes the settings to the saved settings from last runtime
def LoadFiles():
    global presets_list
    global settings_list
    #Handles the files loading in the list so the user can access them
    for (root, dirs, files) in os.walk(save_file_path):
        for file in files:
            presets_list.append(Preset(file.replace(".txt","")))
    #Hanldes that the settings are the same as they where when the user left the programm
    for preset in presets_list:
        if (preset.preset_name == "Settings"):
            settings_list_file = [str(x) for x in preset.dataframe.split('/')]
            settings_list[0] = (settings_list_file[0] == 'True')
            settings_list[1] = (int(settings_list_file[1]))
            settings_list[2] = (settings_list_file[2])
            presets_list.remove(preset)

#Is used for creating the string which then gets saved as a preset file
def stringConstructor(list, element_divider):
    newString = ""
    for i in range(len(list)):
        if (i == len(list)-1):
            newString += str(list[i])
        else:
            newString += str(list[i])+element_divider
    return newString

def setStartPoint():
    tr.left(90)
    ts.back(startPointPosition)
    tr.right(90)

#Is used for retrieving the Values the user made to determine what the programm will draw and how many of it
#This only gets used in the function treeDrawer and when a new preset is created
def setValues():
    values = list()
    values.append(int(layers_of_grass_E.get()))
    values.append(int(length_of_grass_E.get()))
    values.append(int(amount_of_Btrees_E.get()))
    values.append(int(amount_of_flowers_E.get()))
    return values

def updateParameters(new_grass_Para, new_tree_Para, startPosition):
    global grass_Para
    global grass_Para_Str
    global tree_Para
    global tree_Para_Str
    global startPointPosition
    grass_Para = new_grass_Para
    grass_Para_Str = stringConstructor(grass_Para, '/')
    tree_Para = new_tree_Para
    tree_Para_Str = stringConstructor(tree_Para, '/')
    startPointPosition = startPosition

# Main drawing function. Place where every other drawing function gets started
# Values is a list where the user inputs from the main tab are saved
def treeDrawer():
    tr.reset()
    tr.screensize(bg="deepskyblue")
    tr.speed(settings_list[1])
    if(settings_list[0]):
        tr.hideturtle()
    setStartPoint()
    values = setValues()
    drawTrees(values)
    drawFlowers(values)
    drawGrass(values)

# Draws grass over the specific lenght and layers it.
# values[0] specifices the amount of layers the grass will have
# values[1] specifices the length of the grass
def drawGrass(values):
    if (enable_grass.get()):
        for i in range(values[0]):
            gr.grass(values[1], grass_Para)

# Handles the drawing from the trees
# tree_Para[0] defines the stop where the recursion will end
# tree_Para[1] defines the length from the first line of the tree which gets shorter as the recursion proceeds
# tree_Para[2] defines the angle from the branches
# tree_Para[3] defines the placements of fruits and leafes. There are 3 different modes
def drawTrees(values):
    if(enable_trees.get()):
        if (values[2] == 1): # When there is only one tree
            tr.left(90)
            ts.baum(tree_Para[0], tree_Para[1], tree_Para[2], tree_Para[3])
            tr.right(90)
        elif (values[2] % 2 == 0):
            evenAmountOfBTrees(values[1], values[2])
        else:
            unevenAmountOfBTrees(values[1], values[2])    

# Draws trees based on the amount with a certain space between them
def treeDistance(distance, amount):
    for i in range(int(amount)):
        tr.forward(distance)
        tr.left(90)
        ts.baum(tree_Para[0], tree_Para[1], tree_Para[2], tree_Para[3])
        tr.right(90)

#Draws a tree in the middle and then evenly on both sides of it
def unevenAmountOfBTrees(length, amount):
    tr.left(90)
    ts.baum(tree_Para[0], tree_Para[1], tree_Para[2], tree_Para[3])
    tr.right(90)
    evenAmountOfBTrees(length, amount -1)

# Distributes the trees evenly on both sides from the middle 
def evenAmountOfBTrees(length, amount):
    distance = length / (amount/2)
    treeDistance(distance, amount/2)
    ts.back(distance * (amount/2))
    treeDistance(-distance, amount/2)
    ts.back(-distance * (amount/2))

# Handles the drawing of the flowers
# values[1] defines the length of the picture
# values[3] defines the amount of flowers
def drawFlowers(values):
    distance = (values[1]-25)/(values[3]/2)
    flowerDistance(distance, values[3]/2)
    ts.back(distance * (values[3]/2))
    flowerDistance(-distance, values[3]/2)
    ts.back(-distance * (values[3]/2))

# Works the same as tree distance
def flowerDistance(distance, amount):
    for i in range(int(amount)):
        tr.forward(distance)
        tr.left(90)
        fl.FlowerB(50)
        tr.right(90)

# Handles the parameters from the parameter Tab they define specifics like the tree lenght or the gras leaf hight    
class ParameterTab(tk.Frame):
    grass_Para = list()
    tree_Para = list()

    def __init__(self, master = None):
        super().__init__(master=master)

        global grass_para_E
        global tree_para_E
        global startPoint_E

        grass_para_L = tk.Label(self ,text="Grass parameters: min/max lenght, min/max height").pack()
        grass_para_E = tk.Entry(self)
        grass_para_E.insert(0, grass_Para_Str)
        grass_para_E.pack()
        tree_para_L = tk.Label(self, text="min/max branch length, branch angle").pack()
        tree_para_E = tk.Entry(self)
        tree_para_E.insert(0, tree_Para_Str)
        tree_para_E.pack()
        startPoint_L = tk.Label(self, text="Set Start Point").pack()
        startPoint_E = tk.Entry(self)
        startPoint_E.insert(0, str(startPointPosition))
        startPoint_E.pack()
        button = tk.Button(self, text="Apply", command= lambda:self.setParameters(grass_para_E.get(), tree_para_E.get(), startPoint_E.get())).pack()
    
    def setParameters(self, grass_para, tree_para, startPoint):
        grass_Para_String = grass_para
        self.grass_Para = [int(x) for x in grass_Para_String.split('/')]
        tree_Para_String = tree_para
        self.tree_Para = [int(x) for x in tree_Para_String.split('/')]
        updateParameters(self.grass_Para, self.tree_Para, int(startPoint))
# Hanldes the prestes and applies them
class PresetTab(tk.Frame):
    deleteAll = tk.BooleanVar()
    createNewFile = tk.BooleanVar()
    def __init__(self, master = None):
        super().__init__(master=master)
        self.previous_selected = None
        self.createNewFile.set(True)

        head_text_label = tk.Label(self, text="Presets")
        self.presets = tk.Listbox(self)
        preset_name_E = tk.Entry(self)
        delete_all_C = tk.Checkbutton(self, text="Delete All" ,variable=self.deleteAll, onvalue=True, offvalue= False)
        createNewFile_C = tk.Checkbutton(self, text="Create new File", variable=self.createNewFile, onvalue=True, offvalue= False)
        create_B = tk.Button(self, text="Create", command=lambda:self.SavePreset(preset_name_E.get()))
        load_B = tk.Button(self, text="Load", command=lambda: self.LoadPreset())
        delete_B = tk.Button(self, text="Delete", command=lambda:self.DeletePreset())

        head_text_label.grid(column=2, row=0)
        self.presets.grid(column=2, row=1)
        preset_name_E.grid(column=2, row=2)
        createNewFile_C.grid(column=1, row=2)
        create_B.grid(column=1, row=3)
        load_B.grid(column=2, row=3)
        delete_all_C.grid(column=3, row=2)
        delete_B.grid(column=3, row=3)

        self.LoadPresets()

    def SavePreset(self, preset_name):
        if(self.createNewFile.get()):
            self.CreatePreset(preset_name)
        else: 
            for preset in presets_list:
                if (preset.preset_name == self.presets.get(tk.ANCHOR)):
                    self.SaveData(preset)
        
    def CreatePreset(self, preset_name):
        global presets_list
        for preset in presets_list:
                if (preset.preset_name == preset_name):
                    self.SaveData(preset)
                    break
        else:
            preset = Preset(preset_name)
            self.SaveData(preset)
            presets_list.append(preset)
            self.presets.insert(tk.END,preset_name)

    def LoadPreset(self):
        global enable_grass
        global enable_trees 
        for preset in presets_list:
                if (preset.preset_name == self.presets.get(tk.ANCHOR)):
                    data = preset.dataframe
                    datalist = data.split('/')
                    length_of_grass_E.delete(0, 'end')
                    layers_of_grass_E.delete(0, 'end')
                    amount_of_Btrees_E.delete(0, 'end')
                    startPoint_E.delete(0, 'end')
                    grass_para_E.delete(0, 'end')
                    tree_para_E.delete(0, 'end')
                    layers_of_grass_E.insert(0, datalist[0])
                    length_of_grass_E.insert(0, datalist[1])
                    amount_of_Btrees_E.insert(0, datalist[2])                
                    enable_grass.set(datalist[3] == 'True')
                    enable_trees.set(datalist[4] == 'True')
                    startPoint_E.insert(0, datalist[5])
                    grass_para_E.insert(0, datalist[6] + '/' + datalist[7] + '/' + datalist[8] + '/' + datalist[9])
                    tree_para_E.insert(0, datalist[10] + '/' + datalist[11] + '/' + datalist[12])

    # Either deletes one file or all of them based on a checkbox the user can click in the preset tab
    def DeletePreset(self):
        global presets_list
        for preset in presets_list:
            if(preset.preset_name == self.presets.get(tk.ANCHOR)): # Deletes one file
                self.DeleteP(preset)
                self.presets.delete(tk.ANCHOR)
            if (self.deleteAll.get()): # Deletes all of them 
                preset.DeleteFile()
                self.presets.delete(0, tk.END)
        if(self.deleteAll.get()):
            presets_list.clear() # Clears the list after it 
    
    # Is just for deleting one file not all of them
    def DeleteP(self, preset):
        preset.DeleteFile()
        presets_list.remove(preset)

    def SaveData(self, preset):
        values = setValues()
        values.append(enable_grass.get())
        values.append(enable_trees.get())
        values.append(str(startPointPosition))
        preset.dataframe = self.CreatePresetDataFrame(values)
        preset.CreateNewFile()

    def CreatePresetDataFrame(self, values):
        tempstr = stringConstructor(values, '/')
        tempstr += '/' + grass_Para_Str
        tempstr += '/' + tree_Para_Str
        return tempstr

    def LoadPresets(self):
        for i in presets_list:
            self.presets.insert(tk.END,i.preset_name)   

class SettingsTab(tk.Frame):
    hideTurtle_ = tk.BooleanVar()
    def __init__(self, master):
        super().__init__(master)
        hideTurtle_L = tk.Label(self, text="Hide turtle")
        hideTurtle_C = tk.Checkbutton(self, variable=self.hideTurtle_, onvalue=True, offvalue= False)
        turtleSpeed_L = tk.Label(self, text="Speed of Turtle.  \nBetween 0-9. Max = 0")
        turtleSpeed_E = tk.Entry(self, width=47)
        filePath_L = tk.Label(self, text="Change Save File Path")
        filePath_E = tk.Entry(self, width=47)
        apply_B = tk.Button(self, text="Apply", width=15, height=3, command=lambda:self.ApplySettings(turtleSpeed_E.get(),filePath_E.get()))

        self.hideTurtle_.set(settings_list[0])
        turtleSpeed_E.insert(0,str(settings_list[1]))
        filePath_E.insert(0,settings_list[2])

        hideTurtle_L.grid(column=0, row=0, padx=20)
        hideTurtle_C.grid(column=1, row=0)
        turtleSpeed_L.grid(column=0, row=1, padx=20)
        turtleSpeed_E.grid(column=1, row=1)
        filePath_L.grid(column=0, row=3, padx=20)
        filePath_E.grid(column=1, row=3)
        apply_B.grid(columnspan=2, row=4, pady=10)

    def ApplySettings(self, turtlespeed,new_path):
        global settings_list
        global save_file_path
        global settingsFile
        settings_list[0] = self.hideTurtle_.get()
        settings_list[1] = int(turtlespeed)
        settings_list[2] = new_path
        settingsFile.dataframe = stringConstructor(settings_list, '/')
        settingsFile.CreateNewFile()

def MainTab():
    global length_of_grass_E
    global layers_of_grass_E
    global amount_of_Btrees_E
    global amount_of_flowers_E
    global enable_grass
    global enable_trees

    enable_grass_L = tk.Label(main_tab, text="Enable Grass")
    enable_grass_C = tk.Checkbutton(main_tab, variable=enable_grass, onvalue=True, offvalue= False)
    length_of_grass_L = tk.Label(main_tab, text="Length of grass")
    length_of_grass_E = tk.Entry(main_tab, width=50)
    layers_of_grass_L = tk.Label(main_tab, text="Layers_of_grass")
    layers_of_grass_E = tk.Entry(main_tab, width=50)
    enable_trees_L = tk.Label(main_tab, text="Enable Trees")
    enable_trees_C = tk.Checkbutton(main_tab, variable=enable_trees, onvalue=True, offvalue= False)
    amount_of_Btrees_L = tk.Label(main_tab, text="Amount of big trees")
    amount_of_Btrees_E = tk.Entry(main_tab, width=50)
    amount_of_flowers_L = tk.Label(main_tab, text="Amount of flowers")
    amount_of_flowers_E = tk.Entry(main_tab, width=50)
    start = tk.Button(main_tab,text="Start", width=25, height=5, command=treeDrawer)

    layers_of_grass_E.insert(0, '4')
    length_of_grass_E.insert(0, '600')
    amount_of_Btrees_E.insert(0, '1')
    amount_of_flowers_E.insert(0, '2')

    enable_grass_L.grid(column=0,row=0)
    enable_grass_C.grid(column=1,row=0)
    layers_of_grass_L.grid(column=0,row=1)
    layers_of_grass_E.grid(column=1,row=1)
    length_of_grass_L.grid(column=0,row=2)
    length_of_grass_E.grid(column=1,row=2)
    enable_trees_L.grid(column=0,row=3)
    enable_trees_C.grid(column=1,row=3)
    amount_of_Btrees_L.grid(column=0,row=4)
    amount_of_Btrees_E.grid(column=1,row=4)
    amount_of_flowers_L.grid(column=0, row=5)
    amount_of_flowers_E.grid(column=1, row=5)
    start.grid(columnspan=2,row=6)

LoadFiles()

settingsFile = Preset("Settings")
settingsFile.dataframe = stringConstructor(settings_list, '/')
settingsFile.CreateNewFile()

MainTab()
settings = SettingsTab(tabcontrol)
presets = PresetTab(tabcontrol)
parameters = ParameterTab(tabcontrol) 
tabcontrol.add(main_tab, text="Main")
tabcontrol.add(parameters, text="Parameters")
tabcontrol.add(presets, text="Presets")
tabcontrol.add(settings, text="Settings")
tabcontrol.pack(expand=1, fill="both")
main_W.mainloop()