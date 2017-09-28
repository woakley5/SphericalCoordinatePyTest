//
//  main.cpp
//  ctest
//
//  Created by Will Oakley on 9/27/17.
//  Copyright © 2017 Will Oakley. All rights reserved.
//

#include <iostream>
#include "PlatformCalculator.h"

PlatformCalculator c = *new PlatformCalculator(3);

const int kSupportQty = 3;
const float kXYLocations[kSupportQty][2] = {{0.0, 171.45},
    {-148.48, -85.725},
    {148.48, -85.725}};

int main(int argc, const char * argv[]) {
    
    c.setSupportXYLocations(kXYLocations);
    float z_values[kSupportQty];
    
    double theta = 30.0;
    double phi = 83.2;
    c.calculateSupportPositions(theta, phi, z_values);

    printf( "%6.4lf\n", z_values[0] );
    printf( "%6.4lf\n", z_values[1] );
    printf( "%6.4lf\n", z_values[2] );

    return 0;
}
