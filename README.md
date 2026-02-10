# HERA - Maternal Health AI Platform

HERA is an AI-powered maternal health monitoring platform designed to improve maternal healthcare outcomes through intelligent monitoring and analytics.

## 🎯 Project Overview

HERA connects midwives, doctors, and administrators through a comprehensive platform that leverages AI to provide real-time insights and risk assessments for maternal health.

## 📁 Monorepo Structure

This is a monorepo containing all HERA components:

```
Hera-AI/
├── mobile/           # Flutter mobile app for midwives
├── web/              # Next.js/React dashboard for doctors and admins
├── ai-services/      # Python FastAPI AI/ML backend
├── firebase/         # Firebase backend configuration
├── docs/             # Project documentation
└── README.md         # This file
```

## 🏗️ Architecture

### Mobile App (`/mobile`)
- **Technology**: Flutter
- **Users**: Midwives
- **Purpose**: Field data collection, patient monitoring, real-time communication

### Web Dashboard (`/web`)
- **Technology**: Next.js/React
- **Users**: Doctors and Administrators
- **Purpose**: Data analysis, AI insights, patient management, system administration

### AI Services (`/ai-services`)
- **Technology**: Python FastAPI
- **Purpose**: Machine learning models, risk assessment, predictive analytics

### Firebase Backend (`/firebase`)
- **Technology**: Firebase/Google Cloud
- **Purpose**: Authentication, database, storage, cloud functions

### Documentation (`/docs`)
- **Purpose**: Comprehensive project documentation, guides, and API specs

## 🚀 Getting Started

Each component has its own README with detailed setup instructions:

- [Mobile App Setup](./mobile/README.md)
- [Web Dashboard Setup](./web/README.md)
- [AI Services Setup](./ai-services/README.md)
- [Firebase Setup](./firebase/README.md)
- [Documentation](./docs/README.md)

## 👥 Team Structure

This monorepo is designed for teams working on different layers:

- **Mobile Team**: Works in `/mobile`
- **Web Team**: Works in `/web`
- **AI/ML Team**: Works in `/ai-services`
- **Backend Team**: Works in `/firebase`
- **Documentation Team**: Works in `/docs`

## 🛠️ Development Workflow

1. Clone the repository
2. Navigate to your component directory
3. Follow the component-specific setup instructions
4. Start developing!

## 📝 Contributing

Please refer to the [Development Guidelines](./docs/README.md) before contributing.

## 📄 License

[License information to be added]

## 🤝 Hackathon Project

This project is developed as part of a hackathon initiative to improve maternal healthcare through technology and AI.