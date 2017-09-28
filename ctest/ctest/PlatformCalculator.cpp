//------------------------------------------------------------------------------
// PlatformCalculator Function definitions
// Luke Seale - 2016
//------------------------------------------------------------------------------

#include "PlatformCalculator.h"

PlatformCalculator::PlatformCalculator(int supports)
{
  support_qty_ = supports;
  support_locations_ = new CartesianVector[support_qty_];
  locations_set_flag_ = false;
}

PlatformCalculator::~PlatformCalculator()
{
  delete[] support_locations_;
}

void PlatformCalculator::setSupportXYLocations
     (const float xyLocations[][kXYCoordinate])
{
  for(int i = 0; i < support_qty_; i++)
  {
    support_locations_[i].x = xyLocations[i][0];
    support_locations_[i].y = xyLocations[i][1];
    support_locations_[i].z = 0.0;
  }
  
  locations_set_flag_ = true;
}

bool PlatformCalculator::calculateSupportPositions
     (float thetaInDegrees, float phiInDegrees, float zPositions[])
{
  if(!locations_set_flag_) return false;
  
  solveZValues(sphericalToCartesian(1.0, thetaInDegrees, phiInDegrees), 
                                                         zPositions);
  return true;
}

CartesianVector PlatformCalculator::sphericalToCartesian
                (float radius, float thetaInDegrees, float phiInDegrees)
{
  CartesianVector cartesian_coordinates;

  float theta_in_radians =  thetaInDegrees * kDegreesToRadians;
  float phi_in_radians = phiInDegrees * kDegreesToRadians;

  cartesian_coordinates.x = (float) (radius * sin(theta_in_radians)
				                                    * sin(phi_in_radians));
  cartesian_coordinates.y = (float) (radius * sin(theta_in_radians) 
                                            * cos(phi_in_radians));
  cartesian_coordinates.z = (float) (radius * cos(theta_in_radians));

  return cartesian_coordinates;
}

void PlatformCalculator::solveZValues
     (CartesianVector cartesianNormal, float zPositions[])
{
  for(int i = 0; i < support_qty_; i++)
  {
    zPositions[i] = (-1) * ((cartesianNormal.x * support_locations_[i].x) +
			                      (cartesianNormal.y * support_locations_[i].y)) /
                             cartesianNormal.z;
  }
}
