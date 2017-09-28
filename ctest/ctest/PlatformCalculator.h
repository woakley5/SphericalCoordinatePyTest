//------------------------------------------------------------------------------
// PlatformCalculator library header
// Luke Seale - 2016
//------------------------------------------------------------------------------

#include <math.h>

#ifndef PlatformCalculator_h
#define PlatformCalculator_h

// Used to set the width of multidimensional arrays of XY coordinates
// Feel free to use it 
const int kXYCoordinate = 2;

// A convenient structure for Cartesian Vectors, which are used to calculate
// the support locations
struct CartesianVector
{
  float x;
  float y;
  float z;
};


class PlatformCalculator
{
  public:
  
    PlatformCalculator(int supports);
    ~PlatformCalculator();
    
    void setSupportXYLocations(const float xyLocations[][kXYCoordinate]);
    bool calculateSupportPositions
         (float thetaInDegrees, float phiInDegrees, float zPositions[]);
    CartesianVector sphericalToCartesian
                    (float radius, float thetaInDegrees, float phiInDegrees);

  private:
  
    void solveZValues(CartesianVector cartesianNormal, float zPositions[]);
  
    int support_qty_;
    CartesianVector* support_locations_;
    bool locations_set_flag_;
    const float kDegreesToRadians = (3.1415926535 / 180.0);
};

#endif
