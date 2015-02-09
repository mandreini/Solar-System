# -*- coding: utf-8 -*-
"""
Created on 19 Jun, 2014

@author: Matthew Andreini
"""

from ssclasses import *
from ssconstants import *
 
#plants - distances in megameters, sizes in kilometers
sun = Planet(0, 10000,0,yellow)
mercury = Planet(57909,243,0.205,brick)
venus = Planet(108208,605,0.007,orange)
earth = Planet(149598,637,0.017,blue)
mars = Planet(249209,338,0.094,red) 
jupiter = Ringed_Planet(816520,6991,0.0487,bisque,2,10,12000,grey)
saturn = Ringed_Planet(1433449,5823,0.0557,lemon,6,45,11000,brick)
uranus = Ringed_Planet(2876679,2536,0.0444,turquoise,2,90,5000,bisque)
neptune = Ringed_Planet(4503443,2462,0.0112, navy,2,60,4500,bisque)

#moons - distances are megameters/10 and sizes are in kilometes
#distances are also from the surface of the plane
#orbits are assumed circular
moon = Moon(earth,380,1737,steel)
phobos = Moon(mars,100,11,grey)
deimos = Moon(mars,230,6,steel)
io = Moon(jupiter,420,3648,lemon)
europa = Moon(jupiter,670,3122,indianred)
ganymede = Moon(jupiter,1070,5262,steel)
callisto = Moon(jupiter,1880,4821,grey)
rhea = Moon(saturn,520,763,orange)
titan = Moon(saturn,1220,2576,grey)
iapetus = Moon(saturn,3560,734,steel)
miranda = Moon(uranus,120,235,steel)
ariel = Moon(uranus,190,578,grey)
umbriel = Moon(uranus,260,584,bisque)
titania = Moon(uranus,430,788,brick)
oberon = Moon(uranus,580,761,indianred)
triton = Moon(neptune,350,1353,brick,False)

planet_lst  =  [sun,mercury,venus,earth,mars,jupiter,saturn,uranus,neptune]
moon_lst = [moon,phobos,deimos,europa,io,callisto,ganymede,titan,rhea, \
            iapetus,miranda,ariel,umbriel,titania,oberon,triton]
