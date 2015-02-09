# -*- coding: utf-8 -*-
"""
Created on Thu Jun 19 13:42:29 2014

@author: Matt
"""

import math
from ssconstants import sun_radius

class Planet(object):
    def __init__(self,sma,radius,ecc,color):
        self.sma = sma + sun_radius
        self.radius = radius
        self.ecc = ecc
        self.color = color
        self.theta = 0.
        self.r_a = self.sma*(1+self.ecc)
#        rect = (left,top,width,height)
        self.rect = (int(-self.sma),int((-self.sma*(1-self.ecc))), \
         int((self.sma*(1-self.ecc)/(1+self.ecc))+self.sma), \
         int(2*self.sma*(1-self.ecc)))      

        
    def increase_theta(self,time):
        self.theta += 2.*math.pi/(time*(self.sma**1.5))
        if self.theta > 2*math.pi:
            self.theta -= 2*math.pi
    
    def get_pos(self):
#        ellipse
        r = (self.sma*(1-self.ecc))/(1+self.ecc*math.cos(self.theta))
        posx = int(r*math.cos(self.theta))
        posy = int(r*math.sin(self.theta))
        return (posx,posy)

class Moon(object):
    def __init__(self,planet,distance,radius,color,retrograde=True):
        self.planet = planet
        self.distance = distance
        self.radius = radius
        self.color = color
        self.theta = 0.
        self.retrograde=retrograde
        
    def increase_theta(self,time):
        if self.retrograde:
            self.theta += (2.*math.pi/(time*(self.distance**1.5)))/5.
        else:
            self.theta -= (2.*math.pi/(time*(self.distance**1.5)))/5.
        if self.theta > 2*math.pi:
            self.theta -= 2*math.pi
        if self.theta > 2*math.pi:
            self.theta += 2*math.pi	
            
    def get_pos(self):
        planet_x,planet_y = self.planet.get_pos()
        posx = int(self.distance*math.cos(self.theta))
        posy = int(self.distance*math.sin(self.theta))
        moonx = planet_x + posx
        moony = planet_y + posy
        return (moonx,moony)
    
class Ringed_Planet(Planet):
    def __init__(self,sma,radius,ecc,color,thickness,angle,size,ring_color):
        Planet.__init__(self,sma,radius,ecc,color)
        self.thickness = thickness
        self.angle = math.radians(angle)
        self.size = size        
        self.ring_color = ring_color
    
    def ring_position(self,planet_position):
        x_left =  planet_position[0] - self.size*math.cos(self.angle)
        x_right = planet_position[0] + self.size*math.cos(self.angle)
        y_down =  planet_position[1] + self.size*math.sin(self.angle)
        y_up =    planet_position[1] - self.size*math.sin(self.angle)
        return (x_left,y_down),(x_right,y_up)
        
        
