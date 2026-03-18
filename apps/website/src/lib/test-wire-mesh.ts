// Simple test runner for wire mesh calculator
import { calculateWireMesh } from "./wire-mesh-calculator";

console.log("Running Wire Mesh Calculator Tests...\n");

// Test 1: Square mesh calculation
console.log("Test 1: Square mesh calculation");
const result1 = calculateWireMesh(2.5, 50, 50, 10, 2);
console.log(`Mesh Type: ${result1.meshType}`);
console.log(`Wire Diameter: ${result1.wireDiameter} mm`);
console.log(`Aperture Size: ${result1.apertureWidth} x ${result1.apertureHeight} mm`);
console.log(`Panel Size: ${result1.panelLength} x ${result1.panelWidth} m`);
console.log(`Wire Length: ${result1.totalWireLength.toFixed(2)} m`);
console.log(`Wire Weight: ${result1.wireWeight.toFixed(2)} kg`);
console.log(`Number of Panels: ${result1.numberOfPanels}`);
console.log(`Total Weight: ${result1.totalWeight.toFixed(2)} kg\n`);

// Test 2: Rectangular mesh calculation
console.log("Test 2: Rectangular mesh calculation");
const result2 = calculateWireMesh(2.5, 50, 100, 10, 2);
console.log(`Mesh Type: ${result2.meshType}`);
console.log(`Wire Diameter: ${result2.wireDiameter} mm`);
console.log(`Aperture Size: ${result2.apertureWidth} x ${result2.apertureHeight} mm`);
console.log(`Panel Size: ${result2.panelLength} x ${result2.panelWidth} m`);
console.log(`Wire Length: ${result2.totalWireLength.toFixed(2)} m`);
console.log(`Wire Weight: ${result2.wireWeight.toFixed(2)} kg`);
console.log(`Number of Panels: ${result2.numberOfPanels}`);
console.log(`Total Weight: ${result2.totalWeight.toFixed(2)} kg\n`);

console.log("All tests completed successfully!");