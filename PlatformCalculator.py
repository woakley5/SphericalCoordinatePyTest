import math

class CartesianVector:
    def __init__(self):
        self.x = 0.0
        self.y = 0.0
        self.z = 0.0

class PlatformCalculator:
    def __init__(self):
        self.support_qty = 3;
        self.support_locations = []
        for i in range(0, self.support_qty - 1):
            x = CartesianVector()
            self.support_locations.append(x)

    def setSupportLocations(self, xyLocations):
        for x in range(0, self.support_qty - 1):
            self.support_locations[x].x = xyLocations[x][0]
            self.support_locations[x].y = xyLocations[x][1]
            self.support_locations[x].z = 0.0

    def solveZValues(self, cartesianNormal, zPos):
        for x in range(0, self.support_qty - 1):
            zPos[x] = -1 * ((cartesianNormal.x * self.support_locations[x].x) + (cartesianNormal.y * self.support_locations[x].y)) / cartesianNormal.z

    def sphericalToCartesian(self, radius, thetaDeg, phiDeg):
        cartesianCoordinates = CartesianVector()

        thetaInRadians = thetaDeg * kDegreesToRadians
        phiInRadians = phiDeg * kDegreesToRadians

        cartesianCoordinates.x = radius * math.sin(thetaInRadians) * math.sin(phiInRadians)
        cartesianCoordinates.y = radius * math.sin(thetaInRadians) * math.cos(phiInRadians)
        cartesianCoordinates.z = radius * math.cos(thetaInRadians)

        return cartesianCoordinates

    def calculateSupportPositions(self, thetaDeg, phiDeg, zPos):
        self.solveZValues(self.sphericalToCartesian(1.0, thetaDeg, phiDeg), zPos)


calc = PlatformCalculator()
kDegreesToRadians = (3.1415926535 / 180.0);
kXYLocations = [[0.0, 171.45], [-148.48, -85.725], [148.48, -85.725]]; #change these based on the coordinates of the mounts based on the center
zValues = [0.0, 0.0, 0.0] #default to 0.0

calc.setSupportLocations(kXYLocations)

theta = 30.0 #change theta and phi angles
phi = 83.2

calc.calculateSupportPositions(theta, phi, zValues) 

print(zValues[0])
print(zValues[1])
print(zValues[2])
