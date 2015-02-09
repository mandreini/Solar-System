# -*- coding: utf-8 -*-
"""
Created on Thu Jun 19 16:50:01 2014

@author: Matt
"""

#colors     R    G    B       
black =   ( 0 ,  0 ,  0 )
white =   (255, 255, 255)
yellow =  (255, 255,  0 )
red =     (255,  0 ,  0 )
orange =  (255, 165,  0 )
blue =    ( 0 ,  0 , 255)
brick =   (178,  34,  34)
steel =   ( 70, 130, 180)
grey =    (119, 136, 153)
bisque =  (205, 183, 158)
lemon =   (255, 250, 205)
indianred=(205,  92,  92)
turquoise=( 64, 224, 208)
navy =    ( 0 ,  0 , 128)

x_loc = 0
y_loc = 0
z_scale = 300. #zoom
time_scale = 1 #speed of simulation
dt = 0.02
show_orbits = False
mouse_control = False
track = False
controls_time = 0 #for controls
preset_time = 0
fps = 100.
paused = False

"""
Todo (in no particular order):
Change to mouse controls - done
Fix distances/radii to be more "realistic" - done
Sun needs to always be at the center of the orbit area - done
Fix rings - done 
Fix moons - done
Fix zoom - done
Add text to show controls - done
Add presets: - done
only draw planets/moons when they are on-screen (or very close) - done
"""

"""
Presets:
1 - Mercury
2 - Venus
3 - Earth
4 - Mars
5 - Jupiter
6 - Saturn
7 - Uranus
8 - Neptune
9 - Sun in the middle, show all planets
0 - Sun in the middle, show inner planets
"""

"""
Controls:
f - speed up simulation
s - slow down simulation
i - zoom in
o - zoom out
m - toggle mouse control
0-9 - zoom to different planets/views
"""