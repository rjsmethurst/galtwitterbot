

from __future__ import print_function, division, unicode_literals
import numpy as np
import matplotlib.pyplot as plt
import requests
from astropy.coordinates import SkyCoord 
from astropy import unit as un
	
def get_random_galaxy():
  d = data[N.random.randint(0, len(data))]
  c = SkyCoord(ra=d['RA'], dec=d['DEC'],unit=(un.hourangle, un.deg))
  url = 'http://skyservice.pha.jhu.edu/DR8/ImgCutout/getjpeg.aspx?ra='+str(c.ra.value)+'&dec='+str(c.dec.value)+'&scale=0.099183&width=424&height=424'
  return url, d['P_EL_DEBIASED'], d['P_CS_DEBIASED']
