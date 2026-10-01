# Study Risk Analyzer

A lightweight web application for a TY IT IKS individual project. It estimates study risk from academic and study-routine inputs and produces recommendations plus a 7-day revision plan.

## Features
- Attendance, internal marks, study hours, backlog, exam days, revision consistency, sleep and practice inputs
- Transparent heuristic risk score from 0–100
- Low / Moderate / High risk classification
- Action-oriented recommendations
- Automatic 7-day revision plan
- IKS connection through discipline, reflective self-assessment, teacher-guided/personalized learning and balanced routine
- Fully client-side: no API key, database or server required
- Responsive mobile-friendly interface

## Tech Stack
- HTML5
- CSS3
- JavaScript (ES6)
- No external API or library required

## Run locally
1. Download/clone the repository.
2. Open `index.html` in a modern browser.
3. Enter the student values and click **Analyze My Risk**.

For a local server, use VS Code Live Server or Python:
```bash
python -m http.server 8000
```
Then open `http://localhost:8000`.

## Project Structure
```text
Study_Risk_Analyzer/
├── index.html
├── README.md
├── src/
│   ├── app.js
│   └── style.css
└── docs/
    └── Study_Risk_Analyzer_Documentation.pdf
```

## Risk Model
The score is a weighted heuristic, not a clinical or guaranteed prediction. Higher values indicate higher study risk. The model combines attendance, marks, study time, backlog, time pressure, revision consistency, sleep routine and practice completion.

## IKS Connection
The project translates broad educational ideas associated with Indian Knowledge Systems into modern self-assessment: regularity/discipline, reflection, personalized learning and balance between study and daily routine. It does not claim that the score is an IKS-derived scientific formula.

## Security
No credentials are used. No API keys, passwords or tokens are included. Inputs remain in the browser and are not sent to a backend.

## Deployment
This static project can be deployed using GitHub Pages, Netlify or Vercel. After deployment, place the live URL in the documentation and README.

## Student Details
- Student: Shlok Karande
- Roll No.: 17053
- Program: TY IT / study risk Analyzer 
- College: S.I.W.S. N.R. Swamy College of Commerce & Economics and Smt. Thirumalai College of Science
- Academic Year: 2026–27
- Faculty: Prathamesh sir
