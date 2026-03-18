const mermaid = require('mermaid');
const fs = require('fs');
const path = require('path');

async function generateDiagram(diagramCode, outputPath) {
    try {
        // Generate SVG using mermaid CLI approach
        const { execSync } = require('child_process');

        // Write diagram code to temp file
        const tempInput = outputPath.replace('.svg', '.mmd');
        fs.writeFileSync(tempInput, diagramCode);

        // Use mermaid CLI to generate SVG
        execSync(`npx mmdc -i ${tempInput} -o ${outputPath}`, { stdio: 'inherit' });

        // Clean up temp file
        fs.unlinkSync(tempInput);

        console.log(`Generated diagram: ${outputPath}`);
    } catch (error) {
        console.error('Error generating diagram:', error);
    }
}

async function generateAllDiagrams() {
    // ESMS Framework Flowchart
    const esmsFlowchart = `
graph TD
    A[Policy] --> B[Risk Identification]
    B --> C[Management Programs]
    C --> D[Organizational Capacity]
    D --> E[Emergency Preparedness]
    E --> F[Stakeholder Engagement]
    F --> G[External Communications]
    G --> H[Monitoring & Review]
    H --> A

    style A fill:#e1f5fe
    style B fill:#f3e5f5
    style C fill:#e8f5e8
    style D fill:#fff3e0
    style E fill:#ffebee
    style F fill:#f3e5f5
    style G fill:#e8f5e8
    style H fill:#e1f5fe
`;

    // Regulatory Bodies Relationship
    const regulatoryDiagram = `
graph TD
    A[GK & A Logistics] --> B[NPA]
    A --> C[NIWA]
    A --> D[NIMASA]
    A --> E[NSC]
    A --> F[NESREA]
    A --> G[NCS]
    A --> H[SON]

    B --> I[Port Operations]
    C --> J[Inland Waterways]
    D --> K[Maritime Safety]
    E --> L[Economic Regulation]
    F --> M[Environmental Compliance]
    G --> N[Customs Clearance]
    H --> O[Quality Standards]

    style A fill:#4CAF50,color:#fff
    style B fill:#2196F3,color:#fff
    style C fill:#2196F3,color:#fff
    style D fill:#2196F3,color:#fff
    style E fill:#2196F3,color:#fff
    style F fill:#2196F3,color:#fff
    style G fill:#2196F3,color:#fff
    style H fill:#2196F3,color:#fff
`;

    // Risk Assessment Process
    const riskProcess = `
flowchart TD
    A[Identify Hazards] --> B[Assess Risks]
    B --> C[Evaluate Significance]
    C --> D{Acceptable?}
    D -->|Yes| E[Monitor]
    D -->|No| F[Develop Controls]
    F --> G[Implement Controls]
    G --> H[Monitor Effectiveness]
    H --> I{Effective?}
    I -->|Yes| E
    I -->|No| J[Review Controls]
    J --> F

    style A fill:#FFF3CD
    style E fill:#D1ECF1
    style F fill:#F8D7DA
`;

    // Generate diagrams
    await generateDiagram(esmsFlowchart, 'esms_framework.svg');
    await generateDiagram(regulatoryDiagram, 'regulatory_bodies.svg');
    await generateDiagram(riskProcess, 'risk_assessment_process.svg');

    console.log('All diagrams generated successfully!');
}

generateAllDiagrams();