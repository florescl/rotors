# -*- coding: utf-8 -*-

import itertools
import random
import math
import matplotlib.pyplot as plt
import numpy as np
import random

from random import randrange
from collections import defaultdict

iters = 20
dim = 200

n_iters_try_list = [20, 100, 150, 200, 250, 300, 350, 400, 450, 500]


def __MAIN__():

    frequency_list = np.array([])

    n_particles = 50
    radius = 5

    print '#initialized rotor matrix'

    for n_particle_ind in range(0, n_particles):
        
        for n_iters_try in n_iters_try_list:

            rotor_matrix = [ dim*[0] for i in range(-dim,dim) ]
            rotor_matrix = initialize_rotor_matrix(rotor_matrix)
        
            position_matrix = [ dim*[0] for i in range(-dim,dim) ]
            position_matrix = initialize_position_matrix(position_matrix)
        #print position_matrix
   
            counter_total_particles_crossing_bdry=0

            particle_x = 0
            particle_y = 0

            frequency_list = np.array([])
            n_iters = 0

            while n_iters < n_iters_try:
                rotor_matrix[particle_x][particle_y] = update_rotor_matrix(rotor_matrix, particle_x, particle_y)
                particle_x, particle_y = update_particle_position(rotor_matrix, particle_x, particle_y)
                position_matrix[particle_x][particle_y] = 1

                n_iters+=1

                if math.sqrt(pow(particle_x,2.0)+pow(particle_y, 2.0)) >= radius:
                    counter_total_particles_crossing_bdry+=1

                else:
                    continue

            counter = frequency(position_matrix)
            frequency_list = np.append(frequency_list, counter)

        #print n_iters_try, counter
    
    counter_mean = mean_array(frequency_list)
    
        print n_iters_try, counter_mean


def mean_array(array):
    mean = 0
    sum_array = 0
    
    for ind in range(0,len(array)):
        sum_array+=array[ind]
        
    mean = sum_array/len(array)
    

def frequency(position_matrix):
    counter = 0
    for x_ind in range(-dim, dim):
        for y_ind in range(-dim,dim):
            if position_matrix[x_ind][y_ind] == 1:
                counter+=1
    #print 'counter', counter

    return counter


def update_particle_position(rotor_matrix, particle_x, particle_y):
    #east
      if rotor_matrix[particle_x][particle_y] == 0:
          particle_y+=1
      else:
          if rotor_matrix[particle_x][particle_y] ==1:
              particle_x-=1
          else:
              if rotor_matrix[particle_x][particle_y] == 2:
                  particle_y-=1
              else:
                  if rotor_matrix[particle_x][particle_y] ==3:
                      particle_x+=1

      return particle_x, particle_y


def update_rotor_matrix(rotor_matrix,x,y):
      
  rotor_matrix[x][y] = ((rotor_matrix[x][y]+1)% 4)
  return rotor_matrix[x][y]

def initialize_rotor_matrix(rotor_matrix):
    for x_ind in range(-dim,dim):
        for y_ind in range(-dim,dim):
            rotor_matrix[x_ind][y_ind] = randrange(0,3)
            
    return rotor_matrix

def initialize_position_matrix(position_matrix):
    for x_ind in range(-dim,dim):
        for y_ind in range(-dim,dim):
            position_matrix[x_ind][y_ind] = 0
            
    return position_matrix


if __name__ == '__main__':
  __MAIN__()
