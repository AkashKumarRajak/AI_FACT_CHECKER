# AI Fact Verification & Intelligence Platform

An AI-powered misinformation detection and fact verification platform that combines live web evidence retrieval, LLM-based reasoning, confidence scoring, source credibility analysis, and interactive analytics dashboards.

Built using Streamlit, OpenRouter API, Tavily Search API, Plotly, and SQLite.

---

## Live Demo

https://ak-fact-check-ai.streamlit.app/

---

## GitHub Repository

https://github.com/AkashKumarRajak/AI_FACT_CHECKER

---

# Features

- AI-powered fact verification
- Live web evidence retrieval
- LLM reasoning using OpenRouter
- Confidence score analysis
- Source credibility analysis
- Fake news risk scoring
- Interactive analytics dashboard
- Historical verification tracking
- Category-wise verification analytics
- Risk-level distribution analysis
- Real-time evidence visualization

---

# Tech Stack

## Frontend
- Streamlit

## Backend
- Python

## APIs & AI
- OpenRouter API
- Tavily Search API

## Database
- SQLite

## Data Visualization
- Plotly
- Pandas

---

# Project Architecture

```text
User Claim
   ↓
Tavily Search API
   ↓
Web Evidence Collection
   ↓
OpenRouter LLM Verification
   ↓
Confidence & Risk Analysis
   ↓
Database Storage
   ↓
Analytics Dashboard
```

---

# Screenshots

## Home Page

<img width="100%" alt="Home Page" src="<img width="2048" height="1144" alt="image" src="https://github.com/user-attachments/assets/c3f0b80b-1821-475b-b445-e816ffd4a3f8" />
"/>

---

## AI Verification Result

<img width="100%" alt="Verification Result" src="<img width="2048" height="1144" alt="image" src="https://github.com/user-attachments/assets/3ffe4417-aea3-4135-b017-72ed6aa8fe35" />
"/>

---

## Evidence Sources

<img width="100%" alt="Evidence Sources" src="<img width="2048" height="1144" alt="image" src="https://github.com/user-attachments/assets/f0985146-99b1-4784-bed9-5b88ae61b55c" />
"/>

---

## Analytics Dashboard

<img width="100%" alt="Analytics Dashboard" src="<img width="2048" height="1144" alt="image" src="https://github.com/user-attachments/assets/135d2f2a-6d7c-45f7-b7de-56eb1d79fb62" />
"/>

---

## Category Distribution Analytics

<img width="100%" alt="Category Distribution" src="<img width="2048" height="1144" alt="image" src="https://github.com/user-attachments/assets/77528974-b731-4002-a7d7-bf47f870e3e1" />
"/>

---

## Risk Level Distribution

<img width="100%" alt="Risk Distribution" src="<img width="2048" height="1144" alt="image" src="https://github.com/user-attachments/assets/1252c6ab-a10d-4608-92a5-35c0fd77b328" />
"/>

## <img width="100%" alt="Risk Distribution" src="<img width="2048" height="1144" alt="image" src="https://github.com/user-attachments/assets/4c5e5a62-4885-4139-a202-f21112714d9d"/>
"/>

---

# Installation & Setup

## 1️⃣ Clone Repository

```bash
git clone https://github.com/AkashKumarRajak/AI_FACT_CHECKER.git
cd AI_FACT_CHECKER
```

---

## 2️⃣ Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Mac/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Create `.env` File

Create a `.env` file in the root directory and add:

```env
OPENROUTER_API_KEY=your_openrouter_api_key
TAVILY_API_KEY=your_tavily_api_key
```

---

## 5️⃣ Run Application

```bash
streamlit run app.py
```

---

# Folder Structure

```text
AI_FACT_CHECKER/
│
├── dashboard/
│   └── analytics.py
│
├── database/
│   ├── db.py
│   └── database.db
│
├── services/
│   ├── openrouter_service.py
│   └── tavily_service.py
│
├── utils/
│   ├── category.py
│   ├── confidence.py
│   ├── credibility.py
│   └── risk_score.py
│
├── app.py
├── requirements.txt
├── README.md
└── .env
```

---

# Core Modules

## OpenRouter Service

Handles AI reasoning and fact verification using LLMs.

### Features
- Claim analysis
- AI verdict generation
- Contradiction analysis
- Final summary generation

---

## Tavily Search Service

Retrieves live web evidence for claims.

### Features
- Real-time web search
- Source extraction
- Evidence retrieval
- Multi-source validation

---

## Confidence Engine

Calculates verification confidence scores.

### Metrics
- Evidence strength
- AI reasoning confidence
- Source consistency

---

## Credibility Analyzer

Measures trustworthiness of evidence sources.

### Factors
- Domain reliability
- Information quality
- Reputation analysis

---

## Risk Scoring Engine

Detects misinformation risk levels.

### Risk Categories
- LOW
- MEDIUM
- HIGH

---

# Analytics Dashboard

The analytics dashboard provides:

- Total verification count
- Average confidence score
- Source trust metrics
- Top verification categories
- Category distribution analysis
- Risk-level distribution
- Confidence score visualization
- Verification history tracking

---

# Example Verification Flow

## User Claim

```text
Earth revolves around the Sun
```

## AI Verification Output

### Verdict
TRUE

### Confidence Score
91%

### Risk Level
LOW

### Category
General

### Evidence Sources
- NASA
- Wikipedia
- Educational Research Sources

---

# Deployment

This application is deployed on Streamlit Cloud.

## Deployment Steps

1. Push project to GitHub
2. Connect repository to Streamlit Cloud
3. Add environment variables in Streamlit Secrets
4. Deploy app

---

# Future Improvements

- Multi-model AI comparison
- PDF export functionality
- User authentication
- Claim history search
- Real-time misinformation alerts
- Mobile optimization
- Advanced NLP sentiment analysis
- Social media claim tracking

---

# Author

## Akash Kumar Rajak

- GitHub: https://github.com/AkashKumarRajak
- LinkedIn: [ADD_YOUR_LINKEDIN_LINK](https://www.linkedin.com/in/akash-kumar-rajak-22a98623b/)

---

# License

This project is licensed under the MIT License.

---

# Acknowledgements

- OpenRouter
- Tavily AI
- Streamlit
- Plotly
- Python Community
