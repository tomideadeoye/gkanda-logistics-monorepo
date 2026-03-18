# GK&A Logistics Services Ltd - Monorepo

**Unified repository for website, corporate documentation, and regulatory filings.**

---

## 🏢 Company Overview

**Company Name:** GK&A Logistics Services Ltd  
**RC Number:** 1195456  
**Incorporated:** June 6, 2014  
**Registered Office:** No 6, Femi Okunnu Road, Ikoyi, Lagos State  

**Operational Facility:** NPA Lighter Terminal, Ikorodu, Lagos  
**Managing Director:** Omobola Abiru  
**Contact:** info@gkaports.com | +234 818 192 7251  

---

## 📁 Repository Structure

This monorepo consolidates all GK&A Logistics digital assets:

```
gkanda-logistics-monorepo/
├── apps/
│   └── website/                    # Next.js corporate website
│       ├── src/                    # React components and pages
│       ├── public/                 # Static assets
│       ├── package.json            # Website dependencies
│       └── next.config.ts          # Next.js configuration
│
├── docs/
│   ├── corporate/                  # Corporate Data Room
│   │   ├── 00-README-AND-INDEX/
│   │   ├── 01-CORPORATE-DOCUMENTS/
│   │   ├── 02-REGULATORY-AND-LICENSES/
│   │   ├── 03-FINANCIAL-INFORMATION/
│   │   ├── 04-TECHNICAL-AND-ENGINEERING/
│   │   ├── 05-ESG-AND-COMPLIANCE/
│   │   ├── 06-COMMERCIAL-AND-CONTRACTS/
│   │   ├── 07-INVESTOR-RELATIONS/
│   │   ├── 08-MEDIA-AND-COMMUNICATIONS/
│   │   ├── 09-OPERATIONS/
│   │   ├── 10-PROJECT-DEVELOPMENT/
│   │   ├── 11-SUBMISSIONS-AND-FILINGS/
│   │   ├── 12-MEETINGS-AND-CORRESPONDENCE/
│   │   ├── 99-ARCHIVE/
│   │   ├── temp/
│   │   └── scripts/
│   │
│   └── website-content/            # Website content repository
│       ├── docs/
│       ├── assets/
│       ├── package/
│       ├── *.html                  # HTML preview files
│       └── *.md                    # Content documentation
│
├── packages/                       # Shared packages (future)
│
├── package.json                    # Root workspace config
└── README.md                       # This file
```

---

## 🚀 Quick Start

### Prerequisites
- Node.js >= 18.0.0
- npm >= 9.0.0
- Git

### Installation

```bash
# Clone the repository
git clone https://github.com/gkanda-logistics/gkanda-logistics-monorepo.git
cd gkanda-logistics-monorepo

# Install all dependencies
npm install
```

### Development

```bash
# Start website development server
npm run dev

# Or run directly
cd apps/website
npm run dev
```

### Build

```bash
# Build website for production
npm run build

# Or build directly
cd apps/website
npm run build
```

---

## 📊 Projects Overview

### Phase I - Operational (Q1 2026)
**NPA Lighter Terminal Facility**
- **Quay Length:** 1,232.2 meters
- **Quay Apron:** 37,305.84 m²
- **Warehouse:** 6,040.83 m² (climate-controlled)
- **Stacking Yard:** 8,871.10 m² (paved)
- **Security Perimeter:** 784.85 meters

### Phase II - Under Development
**Ikorodu Regional Inland Port**
- **Land Bank:** 150 hectares (expandable to 667 hectares)
- **Status:** Environmental & regulatory approvals secured
- **Timeline:** 2026-2028

---

## 📂 Documentation Navigation

### For Investors
Start here: [`docs/corporate/07-INVESTOR-RELATIONS/`](docs/corporate/07-INVESTOR-RELATIONS/)
- Investment Teaser
- Financial Information
- Corporate Documents
- Technical Specifications

### For Regulators
Start here: [`docs/corporate/02-REGULATORY-AND-LICENSES/`](docs/corporate/02-REGULATORY-AND-LICENSES/)
- Licenses and Permits
- ESG Compliance
- Technical Drawings
- Submissions

### For Partners
Start here: [`docs/corporate/08-MEDIA-AND-COMMUNICATIONS/`](docs/corporate/08-MEDIA-AND-COMMUNICATIONS/)
- Company Profile
- Press Releases
- Marketing Materials

### For Internal Team
Start here: [`docs/corporate/09-OPERATIONS/`](docs/corporate/09-OPERATIONS/)
- Standard Operating Procedures
- HR Policies
- Job Descriptions

### For Website Development
Start here: [`docs/website-content/`](docs/website-content/)
- Complete website content
- HTML preview files
- Asset documentation
- Content guidelines

---

## 🛠 Available Scripts

| Command | Description |
|---------|-------------|
| `npm run dev` | Start website development server |
| `npm run build` | Build website for production |
| `npm run start` | Start production server |
| `npm run lint` | Run ESLint on website |
| `npm run test` | Run tests |

---

## 📝 Document Management

### Naming Convention
`YYYY-MM-DD_DocumentType_Description_vVersion.pdf`

**Example:**
`2024-07-16_CAC_Registration_Extract_v1.0.pdf`

### Version Control
- All corporate documents in `docs/corporate/`
- Website content in `docs/website-content/`
- Website code in `apps/website/`

---

## 🔐 Access Levels

| Folder | Access Level |
|--------|-------------|
| `apps/website/` | Public |
| `docs/corporate/00-README-AND-INDEX/` | Public |
| `docs/corporate/08-MEDIA-AND-COMMUNICATIONS/` | Public |
| `docs/website-content/` | Internal + Developers |
| `docs/corporate/01-CORPORATE-DOCUMENTS/` | Internal + Investors |
| `docs/corporate/02-REGULATORY-AND-LICENSES/` | Internal + Regulators |
| `docs/corporate/03-FINANCIAL-INFORMATION/` | Internal + Active Investors |
| `docs/corporate/09-OPERATIONS/` | Internal Only |
| `docs/corporate/12-MEETINGS-AND-CORRESPONDENCE/` | Internal Only |
| `docs/corporate/99-ARCHIVE/` | Internal Only |

---

## 📞 Key Contacts

### Corporate Office
**Omobola Abiru**  
Managing Director  
📧 mobola.abiru@gkaports.com (direct)  
📧 info@gkaports.com (general)  
📞 +234 703 834 1611  

**Adegboriye Moshood Abiru**  
Key Personnel  
📧 gkandalogistics@gmail.com  
📞 +234 802 384 7516  

**Bamidele Addy Abiru**  
Key Personnel  
📧 deleabiru@yahoo.com  

**Tomide Adeoye**  
IT Administrator  
📧 tomide.adeoye@gkaports.com  
📞 +234 818 192 7251  

### Website Development
**Dmox Tech Solutions (Adediran Dimeje)**  
📧 Dmoxtechsolutions@gmail.com  
📞 08131690705  

---

## 📋 Document Checklist for Due Diligence

### ✅ Corporate Documents
- [ ] Certificate of Incorporation
- [ ] CAC Registration Extract
- [ ] Memorandum & Articles of Association
- [ ] Board Resolution Authorizing Fundraising

### ✅ Regulatory & Licenses
- [ ] NPA Terminal Operating License
- [ ] NIWA Inland Waterway License
- [ ] Nigeria Customs Section 14 CEMA Approval
- [ ] Lagos State EPA EIA Certificate

### ✅ Technical
- [ ] As-Built Drawings (D-01 to D-08)
- [ ] QAQC Records
- [ ] Survey Reports
- [ ] Material Certificates

### ✅ Financial
- [ ] CAPEX Breakdown ($60.79M)
- [ ] Financial Projections
- [ ] Audited Accounts (2022-2024)

### ✅ ESG & Compliance
- [ ] ESMS Handbook
- [ ] Emergency Response Plan
- [ ] OHS Policy
- [ ] Waste Management Plan

---

## 🌐 Core Services

1. **Port Terminal Operations** - World-class maritime logistics facility
2. **Maritime Cargo Handling** - Efficient cargo processing and handling
3. **Secure Storage Solutions** - Climate-controlled warehouse and open stacking areas
4. **Import/Export Logistics Coordination** - Comprehensive logistics support
5. **Customs Clearance Support** - Documentation and clearance assistance
6. **Last-Mile Delivery Coordination** - Ground transportation services

---

## 🏗 Technology Stack

### Website
- **Framework:** Next.js 15.5.4 (React 19.1.0)
- **Styling:** Tailwind CSS 4
- **UI Components:** Radix UI, Lucide Icons
- **Testing:** Jest, Playwright
- **Linting:** ESLint 9
- **TypeScript:** 5.x

### Documentation
- Static files (PDF, DOCX, MD)
- HTML preview files
- Organized by stakeholder access

---

## 📈 Success Metrics

### Website Performance
- Bounce rate below 40%
- Session duration above 3 minutes
- Pages per session above 4
- Mobile responsiveness 100%

### Business Impact
- Lead generation increase (25% target)
- Customer satisfaction (4.5+ star rating)
- Operational efficiency improvement (30% reduction in support calls)
- Track & trace usage (500+ searches/month)

---

## 🤝 Contributing

This is a private repository for GK&A Logistics Services Ltd and authorized personnel only.

### For Developers
1. Work within `apps/website/` for website changes
2. Update `docs/website-content/` for content changes
3. Corporate documents managed by admin team

### For Content Updates
1. Update content in `docs/website-content/`
2. Sync with website team for deployment
3. Corporate docs require management approval

---

## 📄 License

**UNLICENSED** - Proprietary and Confidential

This repository contains confidential and proprietary information. Access is restricted to authorized personnel only.

---

## 📅 Last Updated

**Date:** March 18, 2026  
**Version:** 1.0.0  
**Maintained by:** GK&A Logistics IT Department  

---

*Built with ❤️ for Nigeria's maritime future*
