#include <math.h>
#include <stdlib.h>
#include <stdio.h>

typedef struct point {int x, y, z, rotor;} point;


void free_matrix(int ***box, int dimx, int dimy, int dimz);

void update_rotor_matrix(int ***box, int dim_x_ind, int dim_y_ind, 
			  int dim_z_ind);

int*** allocate_matrix(int dim_x, int dim_y, int dim_z);
void print_matrix(int ***box, int dim_x, int dim_y, int dim_z);
void update_particle_position(int ***rotor_matrix, int x_ind, int y_ind, 
			      int z_ind);
void initialize_matrix(int ***box, int rows, int cols, int dim_z, int value);
void initialize_random(int ***box, int rows, int cols, int dim_z);

int main(int argc, char *argv[]){

  int n_particles = 20, n_particle_ind;  

  for(n_particle_ind = 0; n_particle_ind < n_particles; n_particle_ind+=1){

  /* initialize all rotors north */
  int i = 0;
  int counter_total_particles_that_cross_boundary = 0;
  int dim = 100;

  int ***rotor_matrix = allocate_matrix(dim, dim, dim);
  initialize_random(rotor_matrix, dim, dim, dim);

  /* these are the particles that reach radius */
  while (i < n_particle_ind){
    int frequencies_N_of_a_particle = 0;
    int radius = 10;
    int n_iters = 0;
    point particle;
    particle.x = 0;  particle.y =0; particle.z = 0;

    while(n_iters < 10000){  
    update_rotor_matrix(rotor_matrix, particle.x, particle.y, particle.z);    
      switch(rotor_matrix[particle.x][particle.y][particle.z]){
      case 0:
	particle.x++;
	break;    
      case 1:
	particle.y++;
	break;
      case 2:
	particle.z++;
	  break;
      case 3:
	particle.x--;
	break;
	case 4:
	  particle.y--;
	  break;
      case 5:
	particle.z--;
	break;
      default:
	break;
      }
      n_iters++;

      if(sqrt(pow(particle.x,2.0)+pow(particle.y, 2.0)+pow(particle.z,2.0)) > radius){
	if(frequencies_N_of_a_particle == 0){
	  counter_total_particles_that_cross_boundary++;}

	frequencies_N_of_a_particle++;
	particle.x = 0;
	particle.y = 0;
	particle.z = 0;
      }      
    }
    
  i++;

  }
  printf("%d %d \n", n_particle_ind, counter_total_particles_that_cross_boundary);
  free_matrix(rotor_matrix, dim, dim, dim);
  }

  return 0;
}

int*** allocate_matrix(int dim_x, int dim_y, int dim_z)
{
  int i, j;
  int ***matrix;
  matrix = malloc(2*dim_x*sizeof(int*));

  for(i = -dim_y; i < dim_y; ++i){
    matrix[i] = malloc(2*dim_y*sizeof(int));
    if(matrix[i] == NULL){
      printf("Memory allocation failed while allocating for matrix[i][].\n"); 
      exit(-1);
    }

    for(j = -dim_z; j < dim_z; ++j){
      matrix[i][j] = malloc(2*dim_z*sizeof(int));
        if(matrix[i][j] == NULL){
      printf("Memory allocation failed while allocating for matrix[i][].\n"); 
      exit(-1);
	}
    }
  }
  
  int row_ind, col_ind, z_ind;
  for(row_ind=-dim_x;row_ind<dim_x;row_ind++){
    for(col_ind=-dim_y;col_ind<dim_y;col_ind++){
      for(z_ind=-dim_z;z_ind<dim_z;z_ind++){
	matrix[row_ind][col_ind][z_ind] = 0;
      }
    }
  }
  
return matrix;
}


void print_matrix(int ***box, int dim_x, int dim_y, int dim_z){
  int row_ind, col_ind, z_ind;
  for(row_ind=0;row_ind<dim_x;row_ind++){
    for(col_ind=0;col_ind<dim_y;col_ind++){
      for(z_ind=0;z_ind<dim_z;z_ind++){	
	printf("%d", box[row_ind][col_ind][z_ind]);
      }
    }
    printf("\n");
  }
}


void initialize_matrix(int ***box, int rows, int cols, int dim_z, int value){
  int row_ind, col_ind, z_ind;
  for(row_ind=-rows;row_ind<rows;row_ind++){
    for(col_ind=-cols;col_ind<cols;col_ind++){
      for(z_ind=-dim_z;z_ind<dim_z;z_ind++){
	box[row_ind][col_ind][z_ind] = value;
      }
    }
  }
}

void initialize_random(int ***box, int rows, int cols, int dim_z){
 int row_ind, col_ind, z_ind;
 for(row_ind=-rows;row_ind<rows;row_ind++){
   for(col_ind=-cols;col_ind<cols;col_ind++){
     for(z_ind=-dim_z;z_ind<dim_z;z_ind++){
       box[row_ind][col_ind][z_ind] = random() % 6;
     }
   }
 } 

}

void update_rotor_matrix(int ***box, int dim_x_ind, int dim_y_ind, 
			 int dim_z_ind){
  
  box[dim_x_ind][dim_y_ind][dim_z_ind] = 
    (box[dim_x_ind][dim_y_ind][dim_z_ind]+1) % 6;
}


void free_matrix(int ***box, int dimx, int dimy, int dimz){
  
  int i_free, j_free, k_free;

  for (j_free = -dimy; j_free < dimy; j_free++) {
    for (k_free = -dimz; j_free < dimz; j_free++) {
    free(box[j_free][k_free]);
    
    }	    
  }

  free(box);
}
