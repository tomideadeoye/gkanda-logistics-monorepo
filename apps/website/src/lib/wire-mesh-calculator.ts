// Utility functions for wire mesh calculations

/**
 * Calculate the weight of wire mesh
 * @param wireDiameter Wire diameter in mm
 * @param apertureWidth Aperture width in mm
 * @param apertureHeight Aperture height in mm
 * @param length Length in meters
 * @param width Width in meters
 * @returns Object containing calculation results
 */
export function calculateWireMesh(
  wireDiameter: number,
  apertureWidth: number,
  apertureHeight: number,
  length: number,
  width: number
) {
  // Convert wire diameter to meters
  const wireDiameterM = wireDiameter / 1000;
  
  // Calculate number of wires
  const numWiresLength = Math.ceil(length * 1000 / apertureHeight) + 1;
  const numWiresWidth = Math.ceil(width * 1000 / apertureWidth) + 1;
  
  // Calculate total wire length in meters
  const totalWireLength = (numWiresLength * width) + (numWiresWidth * length);
  
  // Calculate wire volume in cubic meters (assuming cylindrical wires)
  const wireVolume = totalWireLength * Math.PI * Math.pow(wireDiameterM / 2, 2);
  
  // Calculate weight (assuming steel density of 7850 kg/m³)
  const wireWeight = wireVolume * 7850;
  
  // Determine mesh type
  const meshType = apertureWidth === apertureHeight ? "Square" : "Rectangular";
  
  return {
    meshType,
    wireDiameter,
    apertureWidth,
    apertureHeight,
    panelLength: length,
    panelWidth: width,
    totalWireLength,
    wireWeight,
    numberOfPanels: 1,
    totalWeight: wireWeight
  };
}