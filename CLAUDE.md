# SaaS Support Ticket Analysis

Portfolio project: analysis of customer support tickets (Kaggle `suraj520/customer-support-ticket-dataset`) for CX / support operations insights: volumes, resolution times, satisfaction, channel and priority mix.

## Structure
- `analysis.py` - loads the dataset via `kagglehub` and prints columns and head (starter only)
- `final_analysis.ipynb` - main analysis notebook
- `data/`, `images/` - data and chart outputs (`data/` currently empty)
- `README.md` - short "Featured Projects" summary (8,469 tickets, key findings); not yet a full write-up

## Commands (PowerShell, from this folder)
- `python -m venv .venv` - create a virtual environment (none exists yet)
- `.\.venv\Scripts\Activate.ps1` - activate it
- `pip install kagglehub pandas matplotlib seaborn jupyterlab` - install dependencies
- `pip freeze > requirements.txt` - record dependencies
- `jupyter lab` - open the notebook

## Rules
- Frame findings as CX Ops decisions (staffing, routing, SLA, escalation), not just charts
- Every number in the README must come from the notebook output; never invent figures
- Kaggle credentials stay in `$HOME\.kaggle\kaggle.json`; never commit them
- Keep raw downloaded data out of Git

## Open items
- README still has a `$X` placeholder for revenue leakage; fill it from the notebook or remove the line
- README says "reduced refund processing time by 30-40%": the analysis can only estimate this, so word it as a projection, not a result
- README heading uses an emoji; remove it if I ask for a cleanup
