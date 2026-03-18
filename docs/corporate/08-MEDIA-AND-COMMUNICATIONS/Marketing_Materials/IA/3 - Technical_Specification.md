# GK and A Logistics Services Ltd Website - Technical Specification

- **Product**: GK and A Logistics Services Ltd Website

This document provides the technical specifications for the development of the GK and A Logistics Services Ltd website. It outlines the technology stack, architecture, database design, API specifications, and implementation details required to build the website as defined in the Product Requirements Document.

## Document Information
- **Product**: GK and A Logistics Services Ltd Website
- **Document**: Technical Specification
- **Version**: 1.0
- **Date**: October 9, 2025

## 1. Introduction

### 1.1 Purpose
This document provides the technical specifications for the development of the GK and A Logistics Services Ltd website. It outlines the technology stack, architecture, database design, API specifications, and implementation details required to build the website as defined in the Product Requirements Document.

### 1.2 Scope
This specification covers:
- Technology stack selection
- System architecture
- Database design
- API design
- Frontend component structure
- Security considerations
- Performance requirements
- Deployment architecture

## 2. Technology Stack

### 2.1 Frontend
- **Framework**: Next.js 14 (React-based)
- **Language**: TypeScript
- **Styling**: Tailwind CSS
- **State Management**: React Context API / Zustand
- **Component Library**: Custom component library based on shadcn/ui
- **Forms**: React Hook Form
- **Validation**: Zod
- **Testing**: Jest and React Testing Library

### 2.2 Backend
- **Runtime**: Node.js 18+
- **Framework**: Express.js
- **Language**: TypeScript
- **API Design**: RESTful API
- **Authentication**: JWT (JSON Web Tokens)
- **Documentation**: Swagger/OpenAPI
- **Testing**: Jest and Supertest

### 2.3 Database
- **Primary Database**: PostgreSQL 14+
- **ORM**: Prisma
- **Caching**: Redis
- **Search**: Elasticsearch (for site search functionality)

### 2.4 Infrastructure
- **Hosting**: AWS (Amazon Web Services)
- **Compute**: AWS EC2 or AWS ECS
- **Storage**: AWS S3 (for assets)
- **Database Hosting**: AWS RDS
- **Caching**: AWS ElastiCache (Redis)
- **CDN**: AWS CloudFront
- **DNS**: AWS Route 53
- **Monitoring**: AWS CloudWatch
- **CI/CD**: GitHub Actions

### 2.5 Third-Party Services
- **Maps**: Google Maps API
- **Email**: SendGrid
- **SMS**: Twilio
- **Analytics**: Google Analytics 4
- **Search**: Elasticsearch or Algolia
- **Payment Processing**: Stripe (if required for future features)

## 3. System Architecture

### 3.1 High-Level Architecture
```
┌─────────────────┐    ┌──────────────────┐    ┌──────────────────┐
│   User Device   │◄──►│   CDN/Load Bal.  │◄──►│   Web Server     │
└─────────────────┘    └──────────────────┘    └──────────────────┘
                                                    │       │
                                                    ▼       ▼
                                            ┌─────────┐ ┌─────────┐
                                            │   API   │ │ Frontend│
                                            │ Server  │ │   SSR   │
                                            └─────────┘ └─────────┘
                                                    │       │
                                                    ▼       ▼
                                            ┌──────────────────┐
                                            │   PostgreSQL     │
                                            │   Database       │
                                            └──────────────────┘
                                                    │
                                                    ▼
                                            ┌──────────────────┐
                                            │   Redis Cache    │
                                            └──────────────────┘
```

### 3.2 Component Architecture
```
┌─────────────────────────────────────────────────────────────────────┐
│                        Frontend Application                         │
├─────────────────────────────────────────────────────────────────────┤
│  ┌──────────────┐  ┌──────────────┐  ┌────────────────────────────┐ │
│  │   Layout     │  │ Navigation   │  │          Pages             │ │
│  │              │  │              │  │  ┌───────────────────────┐ │ │
│  │              │  │              │  │  │ Home                  │ │ │
│  │              │  │              │  │  ├───────────────────────┤ │ │
│  │              │  │              │  │  │ Services              │ │ │
│  │              │  │              │  │  ├───────────────────────┤ │ │
│  │              │  │              │  │  │ Track & Trace         │ │ │
│  │              │  │              │  │  ├───────────────────────┤ │ │
│  │              │  │              │  │  │ Locations             │ │ │
│  │              │  │              │  │  ├───────────────────────┤ │ │
│  │              │  │              │  │  │ News & Updates        │ │ │
│  │              │  │              │  │  ├───────────────────────┤ │ │
│  │              │  │              │  │  │ About Us              │ │ │
│  │              │  │              │  │  ├───────────────────────┤ │ │
│  │              │  │              │  │  │ Contact               │ │ │
│  └──────────────┘  └──────────────┘  │  └───────────────────────┘ │ │
│                                      └────────────────────────────┘ │
│  ┌────────────────────────────────────────────────────────────────┐ │
│  │                        UI Components                           │ │
│  │  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌────────────────────┐ │ │
│  │  │  Button  │ │   Card   │ │Accordion │ │   Search Bar       │ │ │
│  │  └──────────┘ └──────────┘ └──────────┘ └────────────────────┘ │ │
│  │  ┌─────────────────┐ ┌─────────────────┐ ┌───────────────────┐ │ │
│  │  │  Form Elements  │ │   Data Tables   │ │  Map Component    │ │ │
│  │  └─────────────────┘ └─────────────────┘ └───────────────────┘ │ │
│  └────────────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────────────┘
                                │
                                ▼
┌─────────────────────────────────────────────────────────────────────┐
│                         Backend Services                            │
├─────────────────────────────────────────────────────────────────────┤
│  ┌────────────────────────────────────────────────────────────────┐ │
│  │                    API Endpoints                               │ │
│  │  ┌──────────────┐ ┌──────────────┐ ┌────────────────────────┐ │ │
│  │  │ Authentication│ │  Containers  │ │      Locations         │ │ │
│  │  │ /auth/*       │ │ /containers/*│ │ /locations/*           │ │ │
│  │  └──────────────┘ └──────────────┘ └────────────────────────┘ │ │
│  │  ┌──────────────┐ ┌──────────────┐ ┌────────────────────────┐ │ │
│  │  │   Services   │ │   Users      │ │      News              │ │ │
│  │  │ /services/*  │ │ /users/*     │ │ /news/*                │ │ │
│  │  └──────────────┘ └──────────────┘ └────────────────────────┘ │ │
│  │  ┌──────────────┐ ┌──────────────┐ ┌────────────────────────┐ │ │
│  │  │   Search     │ │ Notifications│ │   Vessel Schedules     │ │ │
│  │  │ /search/*    │ │ /alerts/*    │ │ /schedules/*           │ │ │
│  │  └──────────────┘ └──────────────┘ └────────────────────────┘ │ │
│  └────────────────────────────────────────────────────────────────┘ │
│  ┌────────────────────────────────────────────────────────────────┐ │
│  │                      Business Logic                            │ │
│  │  ┌──────────────┐ ┌──────────────┐ ┌────────────────────────┐ │ │
│  │  │ Auth Service │ │Track Service │ │Notification Service    │ │ │
│  │  └──────────────┘ └──────────────┘ └────────────────────────┘ │ │
│  │  ┌──────────────┐ ┌──────────────┐ ┌────────────────────────┐ │ │
│  │  │Data Services │ │ Map Service  │ │  Search Service        │ │ │
│  │  └──────────────┘ └──────────────┘ └────────────────────────┘ │ │
│  └────────────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────────────┘
                                │
                                ▼
┌─────────────────────────────────────────────────────────────────────┐
│                         Data Layer                                  │
├─────────────────────────────────────────────────────────────────────┤
│  ┌────────────────────────────────────────────────────────────────┐ │
│  │                       PostgreSQL                               │ │
│  │  ┌──────────────┐ ┌──────────────┐ ┌────────────────────────┐ │ │
│  │  │   Users      │ │ Containers   │ │    Locations           │ │ │
│  │  ├──────────────┤ ├──────────────┤ ├────────────────────────┤ │ │
│  │  │   Services   │ │  Tracking    │ │    Schedules           │ │ │
│  │  ├──────────────┤ ├──────────────┤ ├────────────────────────┤ │ │
│  │  │  News        │ │  Alerts      │ │    Partners            │ │ │
│  │  └──────────────┘ └──────────────┘ └────────────────────────┘ │ │
│  └────────────────────────────────────────────────────────────────┘ │
│  ┌────────────────────────────────────────────────────────────────┐ │
│  │                        Redis Cache                             │ │
│  │  ┌──────────────┐ ┌──────────────┐ ┌────────────────────────┐ │ │
│  │  │ Session Data │ │ API Cache    │ │    Search Cache        │ │ │
│  │  └──────────────┘ └──────────────┘ └────────────────────────┘ │ │
│  └────────────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────────────┘
```

## 4. Database Design

### 4.1 Entity Relationship Diagram
```
┌──────────────┐        ┌────────────────┐        ┌──────────────┐
│    Users     │◄──────►│ ContainerTrack │◄──────►│  Containers  │
└──────────────┘        └────────────────┘        └──────────────┘
       │                        │                         │
       ▼                        ▼                         ▼
┌──────────────┐        ┌────────────────┐        ┌──────────────┐
│ UserAlerts   │        │   Tracking     │        │   Events     │
└──────────────┘        └────────────────┘        └──────────────┘
       │                        │
       ▼                        ▼
┌──────────────┐        ┌────────────────┐
│   Alerts     │        │   Locations    │
└──────────────┘        └────────────────┘
                                │
                                ▼
                       ┌────────────────┐
                       │   Schedules    │
                       └────────────────┘
```

### 4.2 Table Definitions

#### Users Table
``sql
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    uuid UUID UNIQUE NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    company VARCHAR(255),
    phone VARCHAR(20),
    role VARCHAR(50) DEFAULT 'user',
    is_verified BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

#### Containers Table
``sql
CREATE TABLE containers (
    id SERIAL PRIMARY KEY,
    container_number VARCHAR(20) UNIQUE NOT NULL,
    booking_id VARCHAR(50),
    bill_of_lading VARCHAR(50),
    current_location_id INTEGER REFERENCES locations(id),
    status VARCHAR(50),
    estimated_arrival TIMESTAMP,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

#### Locations Table
``sql
CREATE TABLE locations (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    code VARCHAR(10) UNIQUE NOT NULL,
    type VARCHAR(50), -- terminal, port, warehouse, etc.
    address TEXT,
    city VARCHAR(100),
    country VARCHAR(100),
    region VARCHAR(100),
    latitude DECIMAL(10, 8),
    longitude DECIMAL(11, 8),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

#### Tracking Events Table
``sql
CREATE TABLE tracking_events (
    id SERIAL PRIMARY KEY,
    container_id INTEGER REFERENCES containers(id),
    location_id INTEGER REFERENCES locations(id),
    event_type VARCHAR(50),
    event_description TEXT,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

#### Vessel Schedules Table
``sql
CREATE TABLE vessel_schedules (
    id SERIAL PRIMARY KEY,
    vessel_name VARCHAR(255),
    voyage_number VARCHAR(50),
    location_id INTEGER REFERENCES locations(id),
    scheduled_arrival TIMESTAMP,
    scheduled_departure TIMESTAMP,
    actual_arrival TIMESTAMP,
    actual_departure TIMESTAMP,
    status VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

#### User Alerts Table
``sql
CREATE TABLE user_alerts (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id),
    container_id INTEGER REFERENCES containers(id),
    alert_type VARCHAR(50),
    method VARCHAR(20), -- email, sms
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

#### Services Table
``sql
CREATE TABLE services (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    slug VARCHAR(255) UNIQUE NOT NULL,
    description TEXT,
    content JSONB, -- Flexible content structure
    category VARCHAR(100),
    is_published BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

#### News Table
``sql
CREATE TABLE news (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    slug VARCHAR(255) UNIQUE NOT NULL,
    excerpt TEXT,
    content TEXT,
    featured_image VARCHAR(255),
    author_id INTEGER REFERENCES users(id),
    is_published BOOLEAN DEFAULT FALSE,
    published_at TIMESTAMP,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

## 5. API Specification

### 5.1 Authentication Endpoints

#### POST /api/auth/register
**Description**: Register a new user account
**Request Body**:
``json
{
  "email": "string",
  "password": "string",
  "firstName": "string",
  "lastName": "string",
  "company": "string",
  "phone": "string"
}
```
**Response**:
``json
{
  "success": true,
  "message": "User registered successfully",
  "data": {
    "user": {
      "id": "number",
      "email": "string",
      "firstName": "string",
      "lastName": "string",
      "company": "string"
    }
  }
}
```

#### POST /api/auth/login
**Description**: Authenticate user and return access token
**Request Body**:
```json
{
  "email": "string",
  "password": "string"
}
```
**Response**:
``json
{
  "success": true,
  "data": {
    "token": "string",
    "user": {
      "id": "number",
      "email": "string",
      "firstName": "string",
      "lastName": "string"
    }
  }
}
```

### 5.2 Container Tracking Endpoints

#### GET /api/containers/search
**Description**: Search for containers by various identifiers
**Query Parameters**:
- containerIds: string[] (comma-separated)
- bookingIds: string[] (comma-separated)
- billOfLading: string[] (comma-separated)

**Response**:
``json
{
  "success": true,
  "data": [
    {
      "containerNumber": "string",
      "bookingId": "string",
      "billOfLading": "string",
      "currentLocation": {
        "name": "string",
        "code": "string"
      },
      "status": "string",
      "estimatedArrival": "timestamp",
      "events": [
        {
          "eventType": "string",
          "location": "string",
          "timestamp": "timestamp",
          "description": "string"
        }
      ]
    }
  ]
}
```

#### POST /api/containers/watchlist
**Description**: Add container to user's watchlist
**Request Body**:
```json
{
  "containerId": "number"
}
```

### 5.3 Location Endpoints

#### GET /api/locations
**Description**: Get all locations
**Response**:
```json
{
  "success": true,
  "data": [
    {
      "id": "number",
      "name": "string",
      "code": "string",
      "type": "string",
      "address": "string",
      "city": "string",
      "country": "string",
      "region": "string"
    }
  ]
}
```

#### GET /api/locations/{id}
**Description**: Get specific location details
**Response**:
``json
{
  "success": true,
  "data": {
    "id": "number",
    "name": "string",
    "code": "string",
    "type": "string",
    "address": "string",
    "city": "string",
    "country": "string",
    "region": "string",
    "latitude": "number",
    "longitude": "number",
    "schedules": [
      {
        "vesselName": "string",
        "voyageNumber": "string",
        "scheduledArrival": "timestamp",
        "scheduledDeparture": "timestamp",
        "status": "string"
      }
    ]
  }
}
```

### 5.4 Vessel Schedule Endpoints

#### GET /api/schedules
**Description**: Get vessel schedules with filtering options
**Query Parameters**:
- region: string
- country: string
- locationId: number

### 5.5 Services Endpoints

#### GET /api/services
**Description**: Get all published services
**Response**:
```json
{
  "success": true,
  "data": [
    {
      "id": "number",
      "title": "string",
      "slug": "string",
      "excerpt": "string",
      "category": "string"
    }
  ]
}
```

#### GET /api/services/{slug}
**Description**: Get specific service details

### 5.6 News Endpoints

```
