#include <stdbool.h>

bool better_than_average(const int class_points[], int class_size, int your_points) {
  // Your code here :)
  // Note: class_size is the length of class_points.
  int s = 0;
  for (int i=0;i<class_size;i++){
    s+=class_points[i];
  }
  double a = s/class_size;
  return your_points > a;
}
