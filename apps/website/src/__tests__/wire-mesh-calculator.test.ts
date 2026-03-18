import { calculateWireMesh } from "@/lib/wire-mesh-calculator";

// Simple test without Jest framework
function test(description: string, fn: () => void) {
  try {
    fn();
    console.log(`✓ ${description}`);
  } catch (error) {
    console.error(`✗ ${description}`);
    console.error(error);
  }
}

function expect(actual: unknown) {
  return {
    toBe(expected: unknown) {
      if (actual !== expected) {
        throw new Error(`Expected ${expected} but got ${actual}`);
      }
    },
    toBeCloseTo(expected: number, precision: number = 2) {
      if (Math.abs(actual as number - expected) > Math.pow(10, -precision) / 2) {
        throw new Error(`Expected ${expected} but got ${actual}`);
      }
    }
  };
}

// Test cases
test("calculates square mesh correctly", () => {
  const result = calculateWireMesh(2.5, 50, 50, 10, 2);
  
  expect(result.meshType).toBe("Square");
  expect(result.wireDiameter).toBe(2.5);
  expect(result.apertureWidth).toBe(50);
  expect(result.apertureHeight).toBe(50);
  expect(result.panelLength).toBe(10);
  expect(result.panelWidth).toBe(2);
  expect(result.numberOfPanels).toBe(1);
});

test("calculates rectangular mesh correctly", () => {
  const result = calculateWireMesh(2.5, 50, 100, 10, 2);
  
  expect(result.meshType).toBe("Rectangular");
  expect(result.wireDiameter).toBe(2.5);
  expect(result.apertureWidth).toBe(50);
  expect(result.apertureHeight).toBe(100);
  expect(result.panelLength).toBe(10);
  expect(result.panelWidth).toBe(2);
  expect(result.numberOfPanels).toBe(1);
});

console.log("All tests completed!");