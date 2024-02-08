#include <vector>

std::vector<int> invert(std::vector<int> values)
{
  std::vector<int> invert;
  for (int i:values){
    invert.push_back(i*-1);
  }
  return invert;
}
