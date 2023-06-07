"""
This is the 1st part of the program where I have defined all the classes and functions.
These classes and functions are then called and used in SpinalTapMain.py to plot and simulate the spinal tap concert.

"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as img
from matplotlib.patches import Rectangle
import matplotlib.patches as patches

class Lights:                                    #code refrence - practest2
    def light1(colour1, colour2, colour3, colour4, colour5, colour6, intensity):
        #Setting Positions
        light_startx = np.linspace(250, 210, 7)
        light_starty = np.linspace(1500, 1500, 7)
        light_endx = np.linspace(500, 200, 7)
        light_endy = np.linspace(600, 600, 7)

        #setting up (x,y) points 1-4 as the corners of the lights
        light_x1 = light_startx[:-1]
        light_x2 = light_startx[1:]
        light_x3 = light_endx[1:]
        light_x4 = light_endx[:-1]
        light_y1 = light_starty[:-1]
        light_y2 = light_starty[1:]
        light_y3 = light_endy[1:]
        light_y4 = light_endy[:-1]
        
        #plot the light 1
        colors = [colour1, colour2, colour3, colour4, colour5, colour6]           #Defining colors of the light
        for i in range(6):
            color = colors[i]
            plt.fill([light_x1[i], light_x2[i], light_x3[i], light_x4[i]],
                        [light_y1[i], light_y2[i], light_y3[i], light_y4[i]], color=color, alpha = intensity)

    def light2(colour1, colour2, colour3, colour4, colour5, colour6, intensity):              #2nd light created same way as light1
        light_startx = np.linspace(250, 210, 7)
        light_starty = np.linspace(1500, 1500, 7)
        light_endx = np.linspace(500, 200, 7)
        light_endy = np.linspace(600, 600, 7)

        #setting up (x,y) points 1-4 as the corners of the lights
        light_x1 = light_startx[:-1]
        light_x2 = light_startx[1:]
        light_x3 = light_endx[1:]
        light_x4 = light_endx[:-1]
        light_y1 = light_starty[:-1]
        light_y2 = light_starty[1:]
        light_y3 = light_endy[1:]
        light_y4 = light_endy[:-1]

        #create a mirrored set of coordinates so light 2 falls exactly opposite to light 1
        max_xy = 2000
        light_x1m = max_xy - light_x1
        light_x2m = max_xy - light_x2
        light_x3m = max_xy - light_x3
        light_x4m = max_xy - light_x4

        # plot the light2 
        colors = [colour1, colour2, colour3, colour4, colour5, colour6]             #Defining colors of the light
        for i in range(6):
            color = colors[i]
            plt.fill([light_x1m[i], light_x2m[i], light_x3m[i], light_x4m[i]],
                        [light_y1[i], light_y2[i], light_y3[i], light_y4[i]], color=color, alpha = intensity)

class Smoke_Machine:                                       #Smoke using Neuman concept
    def smoke(ax,cmap):
        #Set the size of the smoke_grid
        N = 40

        #Set the number of time steps to simulate
        T = 6

        #Create the initial state of the smoke_grid
        smoke_grid = np.zeros((N, N))                                     #Initializing grid of array N,N having zero value
        smoke_grid[N//2, N//2] = 0.1                                      #Center of the smoke_grid has value 0.1

        #Define the Neumann neighborhood
        neighborhood = [(0, -1), (0, 1), (-1, 0), (1, 0)]

        #Iterate over the smoke_grid for T time steps
        for _ in range(T):
        #Create a copy of the smoke_grid to store the updated values
            new_smoke_grid = np.copy(smoke_grid)

        #Update each cell based on its neighboring cells
            for i in range(1, N-1):
                for j in range(1, N-1):
                    neighbors = [(i+x, j+y) for (x, y) in neighborhood]                 #Defining neighbour cells
                    neighbor_values = [smoke_grid[x, y] for (x, y) in neighbors]        #Defining coordinate values of neighbour cells
                    new_smoke_grid[i, j] = np.mean(neighbor_values) + np.random.random_integers(0, 2)   #setting values for the new smoke_grid
                                                                                                        #Using mean of neighbour values and random integers from 0 to 2.
        #Update the smoke_grid with the new values
            smoke_grid = new_smoke_grid
        #Create a heatmap of the smoke_grid
            ax = plt.gca()
            ax.imshow(smoke_grid, cmap=cmap, extent=[-50,2050,300,0] ,alpha = 0.2, zorder=10)
            
class BandProps:
    def band():
        path = 'drummer.png'                    #Image taken from google
        band_image_shape = img.imread(path)     #Path has to be defined correctly in order to get the image
        xpos1 = 800                             #Setting positions of the band (xpos1,xpos2,ypos1,ypos2)
        xpos2 = 1100
        ypos1 = 600
        ypos2 = 1000
        #displaying the image
        #setting zorder at high value to show the band above Backdrop and stage
        plt.imshow(band_image_shape, extent=[xpos1,xpos2,ypos1,ypos2], aspect='auto', zorder=9)

    def drum(ax, center_x, center_y):
        #Creating the dimensions of the drum shape
        drum_width = 200
        drum_height = 300

        #creating the drum body
        drum = patches.Rectangle((center_x - drum_width/2, center_y - drum_height/2), drum_width,
                                 drum_height, edgecolor='black', facecolor='lightgray', zorder =10)
        ax.add_patch(drum)

        #creating the drumhead
        drumhead_radius = drum_width / 2
        drumhead = patches.Circle((center_x, center_y), drumhead_radius, edgecolor='yellow', facecolor='red', zorder =10)
        ax.add_patch(drumhead)

    def piano(ax, center_x, center_y):
        #creating the dimensions of the piano shape
        piano_width = 200
        piano_height = 100

        #creating the piano body
        piano = patches.Rectangle((center_x - piano_width/2, center_y - piano_height/2), piano_width, piano_height, edgecolor='black', facecolor='white', zorder = 10)
        ax.add_patch(piano)

        #creating the piano keys
        piano_key_width = piano_width / 14
        piano_key_height = piano_height
        piano_key_start_x = center_x - piano_width / 2
        piano_key_start_y = center_y - piano_height / 2
        for i in range(14):
            if i % 7 in [0, 3]:
                key_color = 'black'
            else:
                key_color = 'white'
            piano_key = patches.Rectangle((piano_key_start_x + i * piano_key_width, piano_key_start_y), piano_key_width, piano_key_height, edgecolor='black', facecolor=key_color, zorder = 10)
            ax.add_patch(piano_key)
        #adding piano legs
        leg1 = Rectangle((center_x - piano_width/2, center_y - piano_width/1.5 ), 10, 80, edgecolor = "black" ,facecolor="black")
        ax.add_patch(leg1)

        leg2 = Rectangle((center_x + piano_width/2-10, center_y - piano_width/1.5 ), 10, 80, edgecolor = "black" ,facecolor="black")
        ax.add_patch(leg2)

class Backdrop_Stage:
    def backdrop():
        path = 'backdrop.jpg'                       #Spinal Tap backdrop Image taken from google
        backdrop_image = img.imread(path)           #Path of the file
                                                    #displaying the image
        plt.imshow(backdrop_image, extent=[0,2000,800,2000], aspect='auto')

    def stage(colour):                             #Creating stage in the form of rectangle
        stage = Rectangle((0, 200), 2000, 600, edgecolor = "black" ,facecolor = colour, capstyle = 'projecting' ,hatch = '+' ,linewidth = 10, linestyle = 'dotted' ,alpha=0.8)
        ax = plt.gca()
        ax.add_patch(stage)
