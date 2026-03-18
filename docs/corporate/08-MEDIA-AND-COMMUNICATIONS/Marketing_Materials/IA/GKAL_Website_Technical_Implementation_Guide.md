# GK and A Logistics Services Ltd - Website Technical Implementation Guide

## Technology Stack

### Frontend Framework
- **Next.js 15+**: React-based framework with App Router
- **React 19**: Latest React version with concurrent features
- **TypeScript**: Full type safety for maintainable code
- **Tailwind CSS**: Utility-first CSS framework for rapid development

### Backend & Database
- **Next.js API Routes**: Serverless API endpoints
- **PostgreSQL**: Robust relational database for customer and content data
- **Prisma ORM**: Type-safe database access
- **NextAuth.js**: Authentication and session management

### Content Management
- **Sanity CMS**: Headless CMS for content management
- **Real-time Updates**: Live content editing and publishing
- **Version Control**: Content revision history

### Hosting & Infrastructure
- **Vercel**: Frontend hosting with global CDN
- **Railway/PlanetScale**: Database hosting with auto-scaling
- **AWS S3**: File storage for images and documents
- **Cloudflare**: Additional CDN and security layer

## System Architecture

### Application Structure
```
gkanda-website/
├── app/                    # Next.js App Router
│   ├── (auth)/            # Authentication pages
│   ├── (dashboard)/       # Customer portal
│   ├── api/               # API routes
│   ├── about/             # Company pages
│   ├── services/          # Service pages
│   └── page.tsx           # Homepage
├── components/            # Reusable components
│   ├── ui/               # Base UI components
│   ├── forms/            # Form components
│   ├── layout/           # Layout components
│   └── sections/         # Page sections
├── lib/                  # Utility functions
│   ├── api/             # API client functions
│   ├── auth/            # Authentication utilities
│   ├── db/              # Database utilities
│   └── utils/           # General utilities
├── hooks/               # Custom React hooks
├── types/               # TypeScript type definitions
└── public/             # Static assets
```

### API Architecture

#### RESTful Endpoints
- `GET /api/container/track` - Container tracking
- `GET /api/vessel/schedule` - Vessel schedule data
- `POST /api/alerts/subscribe` - Terminal alerts subscription
- `POST /api/contact` - Contact form submission
- `GET /api/services/locator` - Service locator data

#### Authentication Endpoints
- `POST /api/auth/signin` - User login
- `POST /api/auth/signup` - User registration
- `POST /api/auth/signout` - User logout
- `GET /api/auth/session` - Session validation

### Database Schema

#### Core Tables
```sql
-- Users and Authentication
CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  email VARCHAR(255) UNIQUE NOT NULL,
  password_hash VARCHAR(255) NOT NULL,
  company_name VARCHAR(255),
  phone VARCHAR(50),
  role VARCHAR(50) DEFAULT 'customer',
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW()
);

-- Container Tracking
CREATE TABLE containers (
  id SERIAL PRIMARY KEY,
  container_id VARCHAR(20) UNIQUE NOT NULL,
  status VARCHAR(50) NOT NULL,
  location VARCHAR(255),
  last_updated TIMESTAMP DEFAULT NOW(),
  customer_id INTEGER REFERENCES users(id)
);

-- Vessel Schedules
CREATE TABLE vessels (
  id SERIAL PRIMARY KEY,
  vessel_name VARCHAR(255) NOT NULL,
  imo_number VARCHAR(20),
  arrival_date TIMESTAMP,
  departure_date TIMESTAMP,
  terminal VARCHAR(100),
  status VARCHAR(50)
);

-- Terminal Alerts
CREATE TABLE alerts (
  id SERIAL PRIMARY KEY,
  user_id INTEGER REFERENCES users(id),
  alert_type VARCHAR(100),
  message TEXT,
  sent_at TIMESTAMP DEFAULT NOW(),
  read_at TIMESTAMP
);

-- Service Requests
CREATE TABLE service_requests (
  id SERIAL PRIMARY KEY,
  user_id INTEGER REFERENCES users(id),
  service_type VARCHAR(100),
  description TEXT,
  status VARCHAR(50) DEFAULT 'pending',
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW()
);
```

## Key Features Implementation

### 1. Container Tracking System

#### Frontend Component
```typescript
// components/ContainerTracker.tsx
'use client';

import { useState } from 'react';
import { Button } from '@/components/ui/button';
import { Input } from '@/components/ui/input';

export function ContainerTracker() {
  const [containerId, setContainerId] = useState('');
  const [trackingData, setTrackingData] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleTrack = async () => {
    setLoading(true);
    try {
      const response = await fetch(`/api/container/track?id=${containerId}`);
      const data = await response.json();
      setTrackingData(data);
    } catch (error) {
      console.error('Tracking error:', error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="container-tracker">
      <Input
        placeholder="Enter Container ID, Booking ID, or Bill of Lading"
        value={containerId}
        onChange={(e) => setContainerId(e.target.value)}
      />
      <Button onClick={handleTrack} disabled={loading}>
        {loading ? 'Tracking...' : 'Track Container'}
      </Button>
      {trackingData && <ContainerStatus data={trackingData} />}
    </div>
  );
}
```

#### API Route
```typescript
// app/api/container/track/route.ts
import { NextRequest, NextResponse } from 'next/server';
import { PrismaClient } from '@prisma/client';

const prisma = new PrismaClient();

export async function GET(request: NextRequest) {
  const { searchParams } = new URL(request.url);
  const containerId = searchParams.get('id');

  if (!containerId) {
    return NextResponse.json(
      { error: 'Container ID is required' },
      { status: 400 }
    );
  }

  try {
    const container = await prisma.container.findUnique({
      where: { container_id: containerId }
    });

    if (!container) {
      return NextResponse.json(
        { error: 'Container not found' },
        { status: 404 }
      );
    }

    return NextResponse.json(container);
  } catch (error) {
    console.error('Database error:', error);
    return NextResponse.json(
      { error: 'Internal server error' },
      { status: 500 }
    );
  }
}
```

### 2. Vessel Schedule Integration

#### Data Fetching Hook
```typescript
// hooks/useVesselSchedule.ts
import { useState, useEffect } from 'react';

interface VesselSchedule {
  vessel_name: string;
  arrival_date: string;
  departure_date: string;
  status: string;
  terminal: string;
}

export function useVesselSchedule(terminal: string = 'APM Terminals Onne') {
  const [schedules, setSchedules] = useState<VesselSchedule[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const fetchSchedules = async () => {
      try {
        const response = await fetch(`/api/vessel/schedule?terminal=${terminal}`);
        if (!response.ok) throw new Error('Failed to fetch schedules');
        const data = await response.json();
        setSchedules(data);
      } catch (err) {
        setError(err instanceof Error ? err.message : 'Unknown error');
      } finally {
        setLoading(false);
      }
    };

    fetchSchedules();
  }, [terminal]);

  return { schedules, loading, error };
}
```

### 3. Terminal Alerts System

#### Alert Subscription Component
```typescript
// components/TerminalAlerts.tsx
'use client';

import { useState } from 'react';
import { Button } from '@/components/ui/button';
import { Checkbox } from '@/components/ui/checkbox';
import { Input } from '@/components/ui/input';

const ALERT_TYPES = [
  'Weather Warnings',
  'Congestion Alerts',
  'Customs Delays',
  'Gate Updates',
  'Vessel Changes'
];

export function TerminalAlerts() {
  const [email, setEmail] = useState('');
  const [phone, setPhone] = useState('');
  const [selectedAlerts, setSelectedAlerts] = useState<string[]>([]);
  const [submitting, setSubmitting] = useState(false);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setSubmitting(true);

    try {
      const response = await fetch('/api/alerts/subscribe', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          email,
          phone,
          alertTypes: selectedAlerts
        })
      });

      if (response.ok) {
        alert('Successfully subscribed to terminal alerts!');
      } else {
        throw new Error('Subscription failed');
      }
    } catch (error) {
      alert('Failed to subscribe. Please try again.');
    } finally {
      setSubmitting(false);
    }
  };

  return (
    <form onSubmit={handleSubmit} className="terminal-alerts-form">
      <h3>Subscribe to Terminal Alerts</h3>

      <Input
        type="email"
        placeholder="Email address"
        value={email}
        onChange={(e) => setEmail(e.target.value)}
        required
      />

      <Input
        type="tel"
        placeholder="Phone number (optional)"
        value={phone}
        onChange={(e) => setPhone(e.target.value)}
      />

      <div className="alert-types">
        <h4>Select Alert Types:</h4>
        {ALERT_TYPES.map((alertType) => (
          <Checkbox
            key={alertType}
            label={alertType}
            checked={selectedAlerts.includes(alertType)}
            onChange={(checked) => {
              if (checked) {
                setSelectedAlerts([...selectedAlerts, alertType]);
              } else {
                setSelectedAlerts(selectedAlerts.filter(type => type !== alertType));
              }
            }}
          />
        ))}
      </div>

      <Button type="submit" disabled={submitting}>
        {submitting ? 'Subscribing...' : 'Subscribe to Alerts'}
      </Button>
    </form>
  );
}
```

### 4. Service Locator with Google Maps

#### Google Maps Integration
``typescript
// components/ServiceLocator.tsx
'use client';

import { useState, useEffect } from 'react';
import { GoogleMap, LoadScript, Marker, InfoWindow } from '@react-google-maps/api';

const LIBRARIES = ['places'];

const MAP_CONTAINER_STYLE = {
  width: '100%',
  height: '400px'
};

const CENTER = {
  lat: 6.5244, // Lagos coordinates
  lng: 3.3792
};

interface Location {
  id: number;
  name: string;
  address: string;
  services: string[];
  coordinates: {
    lat: number;
    lng: number;
  };
}

export function ServiceLocator() {
  const [locations, setLocations] = useState<Location[]>([]);
  const [selectedLocation, setSelectedLocation] = useState<Location | null>(null);
  const [mapLoaded, setMapLoaded] = useState(false);

  useEffect(() => {
    // Fetch locations from API
    const fetchLocations = async () => {
      try {
        const response = await fetch('/api/services/locator');
        const data = await response.json();
        setLocations(data);
      } catch (error) {
        console.error('Failed to fetch locations:', error);
      }
    };

    fetchLocations();
  }, []);

  const handleMapLoad = () => {
    setMapLoaded(true);
  };

  return (
    <LoadScript
      googleMapsApiKey={process.env.NEXT_PUBLIC_GOOGLE_MAPS_API_KEY!}
      libraries={LIBRARIES}
      onLoad={handleMapLoad}
    >
      <GoogleMap
        mapContainerStyle={MAP_CONTAINER_STYLE}
        center={CENTER}
        zoom={10}
        options={{
          zoomControl: true,
          streetViewControl: false,
          mapTypeControl: false,
          fullscreenControl: true
        }}
      >
        {locations.map((location) => (
          <Marker
            key={location.id}
            position={location.coordinates}
            onClick={() => setSelectedLocation(location)}
          />
        ))}

        {selectedLocation && (
          <InfoWindow
            position={selectedLocation.coordinates}
            onCloseClick={() => setSelectedLocation(null)}
          >
            <div className="location-info">
              <h3>{selectedLocation.name}</h3>
              <p>{selectedLocation.address}</p>
              <div className="services">
                <strong>Services:</strong>
                <ul>
                  {selectedLocation.services.map((service, index) => (
                    <li key={index}>{service}</li>
                  ))}
                </ul>
              </div>
              <Button
                onClick={() => {
                  const url = `https://www.google.com/maps/dir/?api=1&destination=${selectedLocation.coordinates.lat},${selectedLocation.coordinates.lng}`;
                  window.open(url, '_blank');
                }}
              >
                Get Directions
              </Button>
            </div>
          </InfoWindow>
        )}
      </GoogleMap>
    </LoadScript>
  );
}
```

## Performance Optimization

### Image Optimization
```typescript
// lib/imageOptimization.ts
import { getPlaiceholder } from 'plaiceholder';

export async function getOptimizedImage(src: string) {
  try {
    const { base64, img } = await getPlaiceholder(src);
    return {
      ...img,
      blurDataURL: base64,
    };
  } catch (error) {
    return null;
  }
}
```

### Caching Strategy
```typescript
// lib/cache.ts
import { unstable_cache } from 'next/cache';

export const getCachedVesselSchedules = unstable_cache(
  async (terminal: string) => {
    // Fetch vessel schedule data
    const response = await fetch(`${process.env.API_BASE_URL}/vessels?terminal=${terminal}`);
    return response.json();
  },
  ['vessel-schedules'],
  { revalidate: 300 } // Cache for 5 minutes
);
```

## Security Implementation

### Authentication Setup
```typescript
// lib/auth.ts
import NextAuth from 'next-auth';
import CredentialsProvider from 'next-auth/providers/credentials';
import { PrismaAdapter } from '@next-auth/prisma-adapter';
import { PrismaClient } from '@prisma/client';
import bcrypt from 'bcryptjs';

const prisma = new PrismaClient();

export const authOptions = {
  adapter: PrismaAdapter(prisma),
  providers: [
    CredentialsProvider({
      name: 'credentials',
      credentials: {
        email: { label: 'Email', type: 'email' },
        password: { label: 'Password', type: 'password' }
      },
      async authorize(credentials) {
        if (!credentials?.email || !credentials?.password) {
          return null;
        }

        const user = await prisma.user.findUnique({
          where: { email: credentials.email }
        });

        if (!user) {
          return null;
        }

        const isPasswordValid = await bcrypt.compare(
          credentials.password,
          user.password
        );

        if (!isPasswordValid) {
          return null;
        }

        return {
          id: user.id.toString(),
          email: user.email,
          name: user.company_name,
        };
      }
    })
  ],
  session: {
    strategy: 'jwt'
  },
  pages: {
    signIn: '/auth/signin',
    signUp: '/auth/signup'
  }
};

export default NextAuth(authOptions);
```

## Testing Strategy

### Unit Tests
```typescript
// __tests__/ContainerTracker.test.tsx
import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import { ContainerTracker } from '@/components/ContainerTracker';

// Mock fetch
global.fetch = jest.fn();

describe('ContainerTracker', () => {
  beforeEach(() => {
    jest.clearAllMocks();
  });

  it('displays tracking results when container is found', async () => {
    const mockContainerData = {
      container_id: 'ABC123456',
      status: 'In Transit',
      location: 'APM Terminals Onne'
    };

    (global.fetch as jest.Mock).mockResolvedValueOnce({
      ok: true,
      json: async () => mockContainerData
    });

    render(<ContainerTracker />);

    const input = screen.getByPlaceholderText('Enter Container ID...');
    const button = screen.getByRole('button', { name: 'Track Container' });

    fireEvent.change(input, { target: { value: 'ABC123456' } });
    fireEvent.click(button);

    await waitFor(() => {
      expect(screen.getByText('In Transit')).toBeInTheDocument();
      expect(screen.getByText('APM Terminals Onne')).toBeInTheDocument();
    });
  });
});
```

### E2E Tests
```typescript
// e2e/container-tracking.spec.ts
import { test, expect } from '@playwright/test';

test('container tracking workflow', async ({ page }) => {
  await page.goto('/');

  // Enter container ID
  await page.fill('input[placeholder*="Container ID"]', 'ABC123456');

  // Click track button
  await page.click('button:has-text("Track Container")');

  // Wait for results
  await page.waitForSelector('.tracking-results');

  // Verify results display
  await expect(page.locator('.tracking-results')).toContainText('In Transit');
  await expect(page.locator('.tracking-results')).toContainText('APM Terminals Onne');
});
```

## Deployment Configuration

### Vercel Configuration
```json
// vercel.json
{
  "buildCommand": "npm run build",
  "outputDirectory": ".next",
  "framework": "nextjs",
  "regions": ["fra1"],
  "functions": {
    "app/api/**/*.ts": {
      "maxDuration": 30
    }
  },
  "rewrites": [
    {
      "source": "/api/(.*)",
      "destination": "/api/$1"
    }
  ],
  "headers": [
    {
      "source": "/(.*)",
      "headers": [
        {
          "key": "X-Frame-Options",
          "value": "DENY"
        },
        {
          "key": "X-Content-Type-Options",
          "value": "nosniff"
        },
        {
          "key": "Referrer-Policy",
          "value": "strict-origin-when-cross-origin"
        }
      ]
    }
  ]
}
```

### Environment Variables
```bash
# .env.local
NEXT_PUBLIC_GOOGLE_MAPS_API_KEY=your_google_maps_api_key
DATABASE_URL=your_database_connection_string
NEXTAUTH_SECRET=your_nextauth_secret
NEXTAUTH_URL=http://localhost:3000
SANITY_PROJECT_ID=your_sanity_project_id
SANITY_DATASET=production
SANITY_API_TOKEN=your_sanity_api_token
```

This technical implementation guide provides the complete blueprint for implementing the GK&A Logistics website with all required features, security measures, and performance optimizations.