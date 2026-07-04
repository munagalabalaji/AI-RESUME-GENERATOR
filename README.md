# AI Resume Generator with ATS Score & AI Content Enhancement

A production-ready, feature-rich web application built using **Python (Flask)**, **SQLite**, and the **Google Gemini API** (with smart local fallbacks). It enables users to build high-quality, ATS-optimized resumes in minutes, optimize bullet points, correct grammar, generate custom cover letters, review missing job description keywords, and prep for interviews.

---

## Core Features

- **Multi-step Resume Wizard:** 9 guided steps capturing all details (Personal Info, objective, education, experience, projects, skills, certifications, achievements, languages, and hobbies).
- **Auto-Save Engine:** Dynamic field updates and sub-relation modifications are saved asynchronously on input focus loss.
- **ATS Analytics Checker:** Analyzes resume completeness, contact formatting, action verbs, keyword densities, and length to return a score out of 100 with section metrics and suggestions.
- **Google Gemini API Integration:**
  - Automated Objective and Professional Summary generation.
  - Bullet-point optimization utilizing dynamic metrics and strong action verbs.
  - Recommendations for missing skills matching the candidate's career level.
  - Star-method tailored Cover Letter generator based on target Job Descriptions.
  - Job description keyword audits and match metrics.
  - 5 customized interview questions, interviewer intents, and STAR tips.
  - Floating AI Resume Chat Assistant acting as a personal resume coach.
- **6 Professional templates:** Modern, Minimal, Professional, Executive, Creative, and ATS-Friendly. Can be swapped dynamically without losing data.
- **Exports:** High-fidelity browser printing (pixel-perfect matching layout, web fonts, icons) + backend PDF download (`xhtml2pdf`) + backend structured Word document download (`python-docx`).
- **Profile Photo Uploads:** Auto-crop simulation, securely served assets.
- **Audit Logging & Admin Dashboard:** Admins can view analytics, toggle user roles, delete accounts, delete inappropriate resumes, and inspect system-wide audit logs.

---

## Folder Structure

```text
ai_resume_generator/
│
├── app.py                  # Main application entry point
├── config.py               # Flask configurations
├── requirements.txt        # Application dependencies
├── README.md               # Documentation
├── .env                    # Environment variables (created on install)
├── seed_db.py              # Seeds database with test data
├── tests.py                # Unit test suite
│
├── models/                 # Database SQLAlchemy Models
│   ├── __init__.py         # DB connection definitions
│   ├── user.py             # User profile schemas
│   ├── resume.py           # Resume & sub-relationship schemas
│   └── audit.py            # Audit log schemas
│
├── services/               # Core business services
│   ├── ai_service.py       # Google Gemini API & Fallback Mock AI
│   ├── ats_service.py      # ATS Scoring engine
│   ├── pdf_service.py      # PDF rendering (xhtml2pdf)
│   └── docx_service.py     # DOCX builder (python-docx)
│
├── routes/                 # Flask Blueprints
│   ├── auth.py             # Authentication controls
│   ├── dashboard.py        # Dashboards
│   ├── resume.py           # Wizard, preview, downloads, AI endpoints
│   ├── admin.py            # Admin panels
│   └── main.py             # Landing views & file servings
│
├── templates/              # Jinja2 Layout HTML Files
│   ├── base.html           # Master layout
│   ├── auth/               # Login, Signup, Reset Password
│   ├── dashboard/          # Dashboard panels
│   ├── resume/             # Form wizard, preview, share, printable frames
│   │   └── templates/      # 6 HTML resume layouts
│   ├── admin/              # Admin dashboard
│   ├── errors/             # 403, 404, 500 error pages
│   └── layouts/            # Link mapping directory
│
├── static/                 # Static Assets
│   ├── css/
│   │   └── style.css       # Core variables & light/dark styles
│   └── js/
│       ├── main.js         # Theme toggler & toast triggers
│       ├── builder.js      # Form row duplication & builder AI triggers
│       ├── preview.js      # Zoom, template changing, JD audit, cover letters
│       └── chat.js         # AI Assistant coach chat drawer UI
│
├── database/               # Created sqlite file
└── uploads/                # Profile photo directories
```

---

## Installation & Setup

Follow these steps to run the application locally on Windows:

### 1. Clone & Set Up Directory
Open your terminal (PowerShell or Command Prompt) and navigate to the project directory:
```powershell
cd "f:\AI RESUME Generator"
```

### 2. Create and Activate Virtual Environment
```powershell
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies
```powershell
pip install -r requirements.txt
```

### 4. Configure API Keys & Env Variables
A `.env` file has been automatically created in the root folder. Open it and add your Google Gemini API key:
```env
GEMINI_API_KEY=AIzaSyYourActualKeyFromGoogleAIStudio
```
*(If no key is provided, the application will automatically fall back to an intelligent mock generator so the app remains fully functional and testable!)*

### 5. Seed the Database
Create database tables and populate standard test users and sample resumes:
```powershell
python seed_db.py
```

### 6. Run the Unit Tests
Verify all functions, database connections, and routes are working correctly:
```powershell
python tests.py
```

### 7. Run the Application
Start the local development server:
```powershell
python app.py
```
Open [http://localhost:5000](http://localhost:5000) in your web browser.

---

## Testing Accounts (Seed Data)

The database seeding script creates two default accounts for testing:

### 1. Standard Candidate Account
- **Email:** `user@resumegen.com`
- **Password:** `user123`
- **Pre-loaded Data:** Features a complete, pre-built candidate profile (John Doe) with 4 years of experience, multiple education records, projects, certifications, and skills ready for review.

### 2. System Administrator Account
- **Email:** `admin@resumegen.com`
- **Password:** `admin123`
- **Access:** Grants full access to the **Admin Control Panel** to inspect audit logs, ban users, audit system resumes, and track AI usage rates.
