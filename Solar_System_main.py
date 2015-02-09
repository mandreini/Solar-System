# -*- coding: utf-8 -*-
"""
Created on 15 Jun, 2014

@author: Matthew Andreini
"""

import pygame
#import pygame._view
from ssbodies import *
from ssconstants import *  

def display_font(message,color,position):
    controltext = txt.render(message,1,color)
    controlpos = controltext.get_rect()
    controlpos.topleft = position
    scr.blit(controltext,controlpos)

def pause_font(message,color,position):
    controltext = ptxt.render(message,1,color)
    controlpos = controltext.get_rect()
    controlpos.topleft = position
    scr.blit(controltext,controlpos)

#set up the screen
pygame.init()
xmax = 600
ymax = 600
scr = pygame.display.set_mode((xmax,ymax))
t = pygame.time.get_ticks() * 0.001
txt = pygame.font.SysFont("Ariel",18)
ptxt = pygame.font.SysFont("Ariel",30)

#main game loop
control = True
while control:
#    control = False    
    t0 = pygame.time.get_ticks() * 0.001
    delta_t = t0 - t
    t = t0
    
    pygame.event.pump() 

    keys = pygame.key.get_pressed()
    controls_time += delta_t
    preset_time += delta_t
    
    if controls_time >= 0.5:
        if keys[pygame.K_ESCAPE]:
            control = False
        elif keys[pygame.K_m]:
            mouse_control = not mouse_control
            controls_time = 0
        elif keys[pygame.K_t]:
            track = False
        elif keys[pygame.K_p]:
            paused = not paused
            controls_time = 0
    
    if mouse_control:
        mousecolor = red
        mousex,mousey = pygame.mouse.get_pos()
        if mousey <= 25:
            y_loc += 30*int(z_scale/10.)
        elif mousey <= 50:
            y_loc += 15*int(z_scale/10.)
        if mousey >= ymax-25:
            y_loc -= 30*int(z_scale/10.)
        elif mousey >= ymax-50:
            y_loc -= 15*int(z_scale/10.)
        if mousex <= 25:
            x_loc += 30*int(z_scale/10.)
        elif mousex <= 50:
            x_loc += 15*int(z_scale/10.)
        if mousex >= xmax-25:
            x_loc -=30*int(z_scale/10.)
        elif mousex >= xmax-50:
            x_loc -= 15*int(z_scale/10.)
    else:
        mousecolor = white
        
    if keys[pygame.K_f]:
        time_scale *= 1.1
    if keys[pygame.K_s]:
        time_scale /= 1.1

    z_scale0 = z_scale        
    if keys[pygame.K_i]:
        z_scale /= 1.01
    if keys[pygame.K_o]:
        z_scale *= 1.01
    if z_scale < 1.: 
        z_scale = 1.
                
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            control = False
            
    if preset_time > 0.5:
        if keys[pygame.K_0]:
            x_loc = 0
            y_loc = 0
            z_scale = 300
            preset_time = 0
            track = False
        elif keys[pygame.K_9]:
            x_loc = 0
            y_loc = 0
            z_scale = 1500
            preset_time = 0
            track = False
        elif keys[pygame.K_1]:
            track = True
            tracker = mercury
            preset_time = 0
        elif keys[pygame.K_2]:
            track = True
            tracker = venus
            preset_time = 0
        elif keys[pygame.K_3]:
            track = True
            tracker = earth
            preset_time = 0
        elif keys[pygame.K_4]:
            track = True
            tracker = mars
            preset_time = 0
        elif keys[pygame.K_5]:
            track = True
            tracker = jupiter
            preset_time = 0
        elif keys[pygame.K_6]:
            track = True
            tracker = saturn
            preset_time = 0
        elif keys[pygame.K_7]:
            track = True
            tracker = uranus
            preset_time = 0
        elif keys[pygame.K_8]:
            track = True
            tracker = neptune
            preset_time = 0
            
    scr.fill(black)
            
    for c in planet_lst: #compute each planet position and draw it
        c.sma = c.distance / z_scale     
        c.radius = c.size / z_scale
        dtheta = c.delta_theta(dt) * time_scale
        if not paused:
            c.increase_theta(dtheta)
        planetx,planety = c.get_pos()
        planetx = (planetx + x_loc)/z_scale
        planety = (planety + y_loc)/z_scale
        c.planetx = planetx
        c.planety = planety
       
        if planetx > -400 and planetx < 400 and planety > -400 and planety < 400: #planet is on screen
            pygame.draw.circle(scr,c.color,(int(planetx + xmax/2),int(planety + xmax/2)),int(c.radius))
            
            if c.__class__ == Ringed_Planet:
                x_left,y_down,x_right,y_up = c.ring_position()
                x_left = x_left/z_scale + planetx
                y_down = y_down/z_scale + planety
                x_right = x_right/z_scale + planetx
                y_up = y_up/z_scale + planety
                ring1 = (x_left+xmax/2,y_down+xmax/2)
                ring2 = (x_right+xmax/2,y_up+xmax/2)
                pygame.draw.line(scr,c.ring_color,ring1,ring2,c.thickness)
       
        for m in moon_lst:
            if m.planet == c:
                m.distance = (2*m.sma+m.planet.size)/z_scale
                m.radius = m.size/z_scale
                d_theta = m.delta_theta(dt) * time_scale/1000.
                if not paused:
                    m.increase_theta(d_theta)
                mposx,mposy = m.get_pos_of_moon()
                px,py = m.planet.get_pos()
                px = (px + x_loc)/z_scale
                py = (py + y_loc)/z_scale
                pygame.draw.circle(scr,m.color,(int(mposx+px+xmax/2),int(mposy+py+ymax/2)),int(m.radius/10.))

    if z_scale0 != z_scale: #center planet while zooming - not perfect
        x_loc *= z_scale0/z_scale
        y_loc *= z_scale0/z_scale
    
    if track:
        x_loc = -tracker.planet_position[0]
        y_loc = -tracker.planet_position[1]
        mousecolor = white

#    display controls
    display_font("0-9 - change view to different planets",white,(375,460))
    display_font("t - disable planet tracking (1-8)",white,(375,480))
    display_font("m - toggle Mouse control",mousecolor,(375,500))
    display_font("i - zoom In",white,(375,520))
    display_font("o - zoom Out",white,(375,540))
    display_font("f - speed up simulation (Faster)",white,(375,560))
    display_font("s - Slow down simulation",white,(375,580))
    display_font("press p to pause the simulation and bring up more info",white,(10,580))        

    if paused:
        pause_font("Move the mouse to the edges to move around in the model.",grey,(5,50))
        pause_font("This is a robust, psuedo-accurate model of the solar system.",grey,(5,75))
        pause_font("Pressing f or s will gradually change the simulation speed.",grey,(5,100))
        pause_font("While tracking planets, you cannot use mouse controls.",grey,(5,125))        
        
        pause_font("Number keys description:",grey,(25,175))
        pause_font("1 - track mercury",grey,(25,200))
        pause_font("2 - track venus",grey,(25,225))
        pause_font("3 - track earth",grey,(25,250))
        pause_font("4 - track mars",grey,(25,275))
        pause_font("5 - track jupiter",grey,(25,300))
        pause_font("6 - track saturn",grey,(25,325))
        pause_font("7 - track uranus",grey,(25,350))
        pause_font("8 - track neptune",grey,(25,375))
        pause_font("9 - Center the solar system, see all planets",grey,(25,400))
        pause_font("0 - Center the solar system, see inner planets",grey,(25,425))
            
    pygame.display.flip()
    if dt < 1./fps:
        while delta_t < 1./fps:
            t0 = pygame.time.get_ticks() * 0.001
            delta_t = t0-t
    else: #for slower computers
        while delta_t < 2./fps:
            t0 = pygame.time.get_ticks() * 0.001
            delta_t = t0-t  
pygame.quit()
