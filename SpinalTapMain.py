"""
This is the 2nd part of the program, which when executed  will open the Spinal tap concert for the duration entered by the user.
Code depends on Matplot library, csv and SpinalTapExtensions. It will call all the classes and functions from SpinalTapExtensions code.
Plot has two subplots, first one only shows the light source and another one will show the whole choreography of the concert.
Positions and some colour values of sources of light, drum, stage, piano and smoke_machine are read from csv file to perform the choreography

"""
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from SpinalTapExtensions import Lights, Backdrop_Stage, Smoke_Machine, BandProps     # Importing classes and their functions from SpinalTapExtensions.py
import csv

def main():
    try:                                                           #Error handling for non integer values                                                                       
        concert_time = int(input('Enter the concert length in numbers. Eg, 20\n'))  #Should be integer value only. This will define the range till which concert will be played
                                                                                    
        fig, (ax0,ax1) = plt.subplots(2,1, gridspec_kw={'height_ratios': [1, 12]},figsize = (8,8))  #Creating subplots, height ratio 1:12
        fig.suptitle('Spinal tap concert')                         #Super title 

        with open('choreography.csv', newline='') as f:            #Reading csv file to get positions for source of lights, stage, drum, piano and smoke machine
            reader = csv.reader(f)
            data = list(reader)                                    #Coverting into list
            for i in range(concert_time):                          #Define the lenght of the concert(i.e number of iteration), Entered by the user in code line 15
                ax0.axis('off')                                    #Setting off axis to give cleaner look
                ax0.set_title('Spinal Tap Lights')                 #Title of the 1st subplot
                ax0.autoscale()
                ax0.fill([0,500,500,0],[0,0,50,50], color="black") #Filling the 1st subplot with black background

                ax1.set_title('Spinal Tap Choreography')           #Title for the 2nd plot where choreography happens
                ax1.axis('off')                                    #Setting off axis to give cleaner and better look
                ax1.set_xlim([0,2000])                             #Limiting x axes from 0-2000
                ax1.set_ylim([0,1500])                             #Limiting y axes from 0-1500

                Backdrop_Stage.stage(data[4][0])                   #Calling Stage function from Backdrop_Stage class. (using csv)
                Backdrop_Stage.backdrop()                          #Calling Backdrop function from Backdrop_Stage class  

                if i % 2 == 0:                                     #loop through light1() and light2() in alternating manner
                    Lights.light1(data[8][0],data[8][1],data[8][2],data[8][3],data[8][4],data[8][5],float(data[8][6])) #Calling Light1 function from Lights class

                    circle1_xpos = (int(data[0][0]))               #Reading axis values for positions from csv file to plot source of lights
                    circle1_ypos=(int(data[0][1]))
                    circle1_rad=(int(data[0][2]))
                    circle1_facecolor = data[0][3]
                    circle1 = plt.Circle((circle1_xpos,circle1_ypos),circle1_rad, edgecolor = 'red', facecolor= circle1_facecolor,
                                         linewidth=5, linestyle='-', alpha=0.5, fill=True, zorder=2)  #This is the light source for 1st light
                    ax0.add_patch(circle1)

                else:
                    Lights.light2(data[9][0],data[9][1],data[9][2],data[9][3],data[9][4],data[9][5],float(data[9][6])) #Calling Light2 function from Lights class

                    circle2_xpos = (int(data[1][0]))                #Reading axis values for positions from csv file to plot source of lights
                    circle2_ypos = (int(data[1][1]))
                    circle2_rad = (int(data[1][2]))
                    circle2_facecolor = data[0][3]
                    circle1 = plt.Circle((circle2_xpos,circle2_ypos),circle2_rad, edgecolor = 'red', facecolor= circle2_facecolor,
                                         linewidth=5, linestyle='-', alpha=0.5, fill=True, zorder=2)   #This is the light source for 2nd light
                    ax0.add_patch(circle1)

                BandProps.band()                                      #Calling band function from BandProps class
                BandProps.drum(ax1, int(data[2][0]), int(data[2][1])) #Calling drum function from BandProps class and reading positions from csv file
                BandProps.piano(ax1,int(data[3][0]),int(data[3][1]))  #Calling piano function from BandProps class and reading positions from csv file
                Smoke_Machine.smoke(ax1, data[7][0])                  #Calling smoke function from Smoke class to create smoke     
                
                #This is the first smoke machine in elliptical shape
                smk_machine1 = patches.Ellipse((50, 50), 50, 150, angle=135, edgecolor='violet', facecolor= data[5][0],
                                               linewidth=4, linestyle='-', alpha= float(data[5][1]), fill=True, zorder=10)
                ax1.add_patch(smk_machine1)
                
                #This is the second smoke machine in elliptical shape
                smk_machine2 = patches.Ellipse((1950, 50), 50, 150, angle=45, edgecolor='violet', facecolor=data[6][0],
                                               linewidth=4, linestyle='-', alpha= float(data[6][1]), fill=True, zorder=10)
                ax1.add_patch(smk_machine2)

                plt.pause(float(data[10][0]))                       #pause of 0.5 between iterations
                ax1.cla()                                           #Clearing lights to show alternate effect
                ax0.cla()                                           #Clearing source of lights from 1st subplot to show on off effect
            
            #To show the message on the 2nd plot once the concert is over.
            #Code refrence Matplotlib org - https://matplotlib.org/stable/tutorials/text/text_intro.html
            ax1.text(0.05, 0.95, "End of Concert. Thank you for visiting :)",
                    transform=ax1.transAxes, fontsize=14, verticalalignment='top', bbox=dict(facecolor='white', alpha=0.5))
            
            plt.show()    

    except ValueError:                                          # Catching error if user enters non integer value.
        print('Concert length should be an integer number only. Please play again and enter integer value :)')

if __name__ == '__main__':                                      # Executing main function
    main()
