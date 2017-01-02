# -*- coding: utf-8 -*-

import itertools
import random
import math
import numpy as np
import random

from random import randrange
from collections import defaultdict

dim = 450
n_iters_list = [1000000, 2000000, 3000000, 4000000, 5000000, 6000000, 7000000, 10000000]
k = 110
n_particles = 1


def __MAIN__():

    #define some matrices I need
    print '#n_iters_item, n_sites_visited, n_iters_item/math.log(n_iters_item), pow(n_iters_item,0.667), n_excursions'
    for n_iters_item in n_iters_list:

        rotor_matrix = [[0 for y in xrange(0, dim)] for x in xrange(0,dim)]

        rotor_matrix_box = [[[0 for y in xrange(0, k)] for x in xrange(0,k)] for z in xrange(0,dim)]
        visited_matrix = [[0 for y in xrange(0,dim)] for x in xrange(0,dim)]
        unique_visited_matrix = [[0 for y in xrange(0,dim)] for x in xrange(0,dim)]

        #iid rotors
        rotor_matrix = initialize_rotor_matrix(rotor_matrix)

        #setting particle at origin 
        particle_x = dim/2
        particle_y = dim/2

        n_iters_try = 0
        n_excursions = 0
        n_succesive_visits = 0
        n_sites_visited = 0
        n_sites_per_excursion = 0
        n_new_sites_per_excursion = 0
       
        while n_iters_try < n_iters_item:
            #update rotor
            rotor_matrix[particle_x][particle_y] = update_rotor_matrix(rotor_matrix, particle_x, particle_y)
            #move particle
            particle_x, particle_y = update_particle_position(rotor_matrix, particle_x, particle_y)
            n_sites_per_excursion+=1
        
            #print n_iters_try, particle_x, particle_y
            if(unique_visited_matrix[particle_x][particle_y] == 0):
                n_sites_visited+=1
                n_new_sites_per_excursion+=1
            unique_visited_matrix[particle_x][particle_y] = 1
            visited_matrix[particle_x][particle_y]+=1
                   
            if particle_x==dim/2 and particle_y==dim/2:
                #print 'origin visit'
                #rotor_matrix = initialize_rotor_matrix(rotor_matrix)
                n_succesive_visits+=1
             
            if n_succesive_visits==4:
                n_excursions+=1
                #print '#n_excursion, n_new_sites, n_total_sites'

                print n_excursions, n_new_sites_per_excursion, n_sites_per_excursion
                print 'excursion!'
                n_new_sites_per_excursion = 0
                n_sites_per_excursion =0
                #n_total_sites = 0
                n_succesive_visits=0
                form_rotor_matrix_box(rotor_matrix_box, rotor_matrix,k,n_excursions)
                if check_matrices_equal(rotor_matrix_box, n_excursions, k)==1:
                    print n_iters_item, 'we have equality!', n_excursions
                    
                #print 'n_exc', n_excursions
            n_iters_try+=1

        print n_iters_item, n_sites_visited, n_iters_item/math.log(n_iters_item), pow(n_iters_item,0.667), n_excursions


def form_rotor_matrix_box(rotor_matrix_box, rotor_matrix,k,n_excursions):
    for row_ind in range(0,k):
        for col_ind in range(0,k):
            #print row_ind, col_ind
            rotor_matrix_box[n_excursions][row_ind][col_ind] = rotor_matrix[dim/2-k/2+row_ind][dim/2-k/2+col_ind]

def check_matrices_equal(rotor_matrix_box, n_excursions, k):
    ok = 1
    for r_ind in range(0,k):
        for c_ind in range(0,k):
            if rotor_matrix_box[n_excursions][r_ind][c_ind] != rotor_matrix_box[n_excursions-1][r_ind][c_ind]:
                ok=0
    return ok


def compute_n_ones(a_matrix,dimension):
    n_new = 0
    for i_ind in range(0,dimension):
        for j_ind in range(0,dimension):
            if a_matrix[i_ind][j_ind] == 1:
                #print 'found one' 
                n_new=n_new+1
    return n_new
                

def print_rotor_box(k, rotor_matrix):

    for row_ind in range(dim/2-k/2,dim/2+k/2):
        for col_ind in range(dim/2-k/2,dim/2+k/2):
            print rotor_matrix[row_ind][col_ind]
        print "\n" 

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
    for x_ind in range(0,dim):
        for y_ind in range(0,dim):
            rotor_matrix[x_ind][y_ind] = randrange(0,4)
            
    return rotor_matrix

def initialize_position_matrix(position_matrix):
    for x_ind in range(0,dim):
        for y_ind in range(0,dim):
            position_matrix[x_ind][y_ind] = 0
            
    return position_matrix


if __name__ == '__main__':
  __MAIN__()
