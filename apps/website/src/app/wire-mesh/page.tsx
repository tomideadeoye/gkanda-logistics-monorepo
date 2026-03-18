"use client";

import { Button } from "@/components/ui/button";
import Link from "next/link";
import { useState } from "react";
import { calculateWireMesh } from "@/lib/wire-mesh-calculator";

export default function WireMeshCalculator() {
  const [inputs, setInputs] = useState({
    wireDiameter: 2.5,
    apertureWidth: 50,
    apertureHeight: 50,
    length: 10,
    width: 2
  });
  
  const [results, setResults] = useState({
    meshType: "Square",
    wireDiameter: 2.5,
    apertureWidth: 50,
    apertureHeight: 50,
    panelLength: 10,
    panelWidth: 2,
    totalWireLength: 440,
    wireWeight: 7.26,
    numberOfPanels: 1,
    totalWeight: 7.26
  });

  const handleInputChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const { name, value } = e.target;
    setInputs({
      ...inputs,
      [name]: parseFloat(value) || 0
    });
  };

  const handleCalculate = () => {
    const calculated = calculateWireMesh(
      inputs.wireDiameter,
      inputs.apertureWidth,
      inputs.apertureHeight,
      inputs.length,
      inputs.width
    );
    setResults(calculated);
  };

  return (
    <div className="min-h-screen bg-gradient-to-b from-gray-50 to-gray-100 dark:from-gray-900 dark:to-gray-800 p-4 md:p-8">
      <main className="max-w-4xl mx-auto py-12">
        <div className="text-center mb-12">
          <h1 className="text-3xl font-bold tracking-tight mb-4">Wire Mesh Calculator</h1>
          <p className="text-lg text-gray-600 dark:text-gray-300">
            Calculate wire mesh specifications for your project
          </p>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
          {/* Input Section */}
          <div className="bg-white dark:bg-gray-800 rounded-lg shadow-lg p-6">
            <h2 className="text-xl font-semibold mb-4">Input Parameters</h2>
            
            <div className="space-y-4">
              <div>
                <label className="block text-sm font-medium mb-1">Wire Diameter (mm)</label>
                <input 
                  type="number" 
                  name="wireDiameter"
                  className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 dark:bg-gray-700 dark:border-gray-600"
                  value={inputs.wireDiameter}
                  onChange={handleInputChange}
                />
              </div>
              
              <div>
                <label className="block text-sm font-medium mb-1">Aperture Width (mm)</label>
                <input 
                  type="number" 
                  name="apertureWidth"
                  className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 dark:bg-gray-700 dark:border-gray-600"
                  value={inputs.apertureWidth}
                  onChange={handleInputChange}
                />
              </div>
              
              <div>
                <label className="block text-sm font-medium mb-1">Aperture Height (mm)</label>
                <input 
                  type="number" 
                  name="apertureHeight"
                  className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 dark:bg-gray-700 dark:border-gray-600"
                  value={inputs.apertureHeight}
                  onChange={handleInputChange}
                />
              </div>
              
              <div>
                <label className="block text-sm font-medium mb-1">Length (m)</label>
                <input 
                  type="number" 
                  name="length"
                  className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 dark:bg-gray-700 dark:border-gray-600"
                  value={inputs.length}
                  onChange={handleInputChange}
                />
              </div>
              
              <div>
                <label className="block text-sm font-medium mb-1">Width (m)</label>
                <input 
                  type="number" 
                  name="width"
                  className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 dark:bg-gray-700 dark:border-gray-600"
                  value={inputs.width}
                  onChange={handleInputChange}
                />
              </div>
              
              <Button className="w-full mt-4" onClick={handleCalculate}>Calculate</Button>
            </div>
          </div>

          {/* Results Section */}
          <div className="bg-white dark:bg-gray-800 rounded-lg shadow-lg p-6">
            <h2 className="text-xl font-semibold mb-4">Results</h2>
            
            <div className="space-y-4">
              <div className="flex justify-between border-b pb-2">
                <span>Wire Mesh Type:</span>
                <span className="font-medium">{results.meshType}</span>
              </div>
              
              <div className="flex justify-between border-b pb-2">
                <span>Wire Diameter:</span>
                <span className="font-medium">{results.wireDiameter} mm</span>
              </div>
              
              <div className="flex justify-between border-b pb-2">
                <span>Aperture Size:</span>
                <span className="font-medium">{results.apertureWidth} x {results.apertureHeight} mm</span>
              </div>
              
              <div className="flex justify-between border-b pb-2">
                <span>Panel Size:</span>
                <span className="font-medium">{results.panelLength} x {results.panelWidth} m</span>
              </div>
              
              <div className="flex justify-between border-b pb-2">
                <span>Wire Length (m):</span>
                <span className="font-medium">{results.totalWireLength.toFixed(2)} m</span>
              </div>
              
              <div className="flex justify-between border-b pb-2">
                <span>Wire Weight (kg):</span>
                <span className="font-medium">{results.wireWeight.toFixed(2)} kg</span>
              </div>
              
              <div className="flex justify-between border-b pb-2">
                <span>Number of Panels:</span>
                <span className="font-medium">{results.numberOfPanels}</span>
              </div>
              
              <div className="flex justify-between border-b pb-2">
                <span>Total Weight (kg):</span>
                <span className="font-medium">{results.totalWeight.toFixed(2)} kg</span>
              </div>
            </div>
            
            <Button className="w-full mt-6" variant="secondary">Export Results</Button>
          </div>
        </div>

        <div className="mt-12 text-center">
          <Button asChild>
            <Link href="/">← Back to Home</Link>
          </Button>
        </div>
      </main>
    </div>
  );
}