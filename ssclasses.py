# -*- coding: utf-8 -*-
"""
Created on Thu Jun 19 13:42:29 2014

@author: Matt
"""

import math
from ssconstants import *

class Planet(object):
    def __init__(self,distance,size,ecc,color):
        self.distance = distance * 100
        self.size = size
        self.ecc = ecc
        self.color = color
        self.theta = 0.

    def delta_theta(self,time):
        if self.sma == 0:
            return 0
        else: 
            return 2.*math.pi/(time*(self.distance**1.5))

    def increase_theta(self,dtheta):
        self.theta += dtheta
        if self.theta > 2*math.pi:
            self.theta -= 2*math.pi
    
    def get_pos(self):
#        elliptical
        r = self.distance*(1-(self.ecc*self.ecc))/(1+(self.ecc*math.cos(self.theta)))
        posx = int(r*math.cos(self.theta)/z_scale)
        posy = int(r*math.sin(self.theta)/z_scale)
        self.planet_position = (posx, posy)
        return posx,posy

class Moon(object):
    def __init__(self,planet,sma,size,color,retrograde=True):
        self.planet = planet
        self.sma = sma
        self.size = size
        self.color = color
        self.theta = 0.
        self.retrograde=retrograde
    
    def delta_theta(self,time):
        if self.distance == 0:
            return 0
        else:
            if self.retrograde:
                return 2.*math.pi/(time*(self.distance**1.5))
            else: return -2.*math.pi/(time*(self.distance**1.5))
        
    def increase_theta(self,dtheta):
        self.theta += dtheta
        if self.theta > 2*math.pi:
            self.theta -= 2*math.pi	
            
    def get_pos_of_moon(self):
        #relative to the planet
        posx = int(self.distance*math.cos(self.theta))
        posy = int(self.distance*math.sin(self.theta))
        return posx,posy
    
class Ringed_Planet(Planet):
    def __init__(self,distance,size,ecc,color,thickness, angle,rsize,ring_color):
        Planet.__init__(self,distance,size,ecc,color)
        self.thickness = thickness
        self.angle = math.radians(angle) 
        self.rsize = rsize
        self.ring_color = ring_color
    
    def ring_position(self):
        x_left =  int(self.rsize*math.cos(self.angle))
        x_right = int(-self.rsize*math.cos(self.angle))
        y_down =  int(self.rsize*math.sin(self.angle))
        y_up =    int(-self.rsize*math.sin(self.angle))
        return x_left,y_down,x_right,y_up
    