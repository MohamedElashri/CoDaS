#include <stdio.h>
#include <omp.h>
static long num_steps = 100;
double step;
int main ()
{
	  int i;
	  double x, pi, sum = 0.0;
	  double start_time, run_time;

	  step = 1.0/(double) num_steps;
	 for (i=1;i<= num_steps;i++){
          sum = 0.0;
          omp_set_num_threads(10); // Set the # of threads we need. which is int i in our case
	  start_time = omp_get_wtime(); // define start time by calling omp API
#pragma omp parallel // start parallel programming block
{
    #pragma omp single
	  printf(" # of Threads are = %d",omp_get_num_threads()); // omp_get_num_threads
#pragma omp for reduction(+:sum)
	  for (i=1;i<= num_steps; i++){
		  x = (i-0.5)*step;
		  sum = sum + 4.0/(1.0+x*x);
	  }

}

      pi = step * sum;
	  run_time = omp_get_wtime() - start_time;
	  printf("\n Estimated pi has value %f and took %f seconds and  step # is %d \n",pi,run_time,i);
}

}


/*
int main(int argc, const char* argv[]) {

	double pi = 0.0;
	double start, delta, sum[NUM_THREADS];
	start = omp_get_wtime();
	step = 1.0 / (double)steps;
	omp_set_num_threads(NUM_THREADS);
#pragma omp parallel
	{
		double x;
		int id, i;
		id = omp_get_thread_num();
		for (i = id, sum[id] = 0.0; i < steps; i = i + NUM_THREADS) {
			x = (i + 0.5) * step;
			sum[id] += 4.0 / (1.0 + x * x);
		}
	}
	for (int i = 0; i < NUM_THREADS; i++) {
		pi += sum[i] * step;
	}
	delta = omp_get_wtime() - start;
	printf("PI = %.16g computed in %.4g seconds with %d threads.", pi, delta, NUM_THREADS);
}
*/
