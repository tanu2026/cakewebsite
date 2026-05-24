# 🎂 Crumble & Co — Cake Website

A full Flask website for an artisan cake shop.
All files live in **one flat folder** — no subfolders required.

## Files in this folder

| File | Purpose |
|------|---------|
| `app.py` | Flask application & routes |
| `base.html` | Shared nav/footer layout |
| `index.html` | Home page |
| `menu.html` | Full cake menu with category filter |
| `detail.html` | Individual cake detail page |
| `about.html` | About / team page |
| `contact.html` | Contact form |
| `order.html` | Order form |
| `requirements.txt` | Python dependencies |

## Pages

- `/` — Home (hero, featured cakes, testimonials)
- `/menu` — All cakes with category filter
- `/cake/<id>` — Individual cake detail
- `/about` — Our story, values, team
- `/contact` — Contact form
- `/order` — Order form

## How to Run

```bash
# 1. Install Flask
pip install -r requirements.txt

# 2. Run the development server
python app.py
```

Then open **http://127.0.0.1:5000** in your browser.

## Requirements

- Python 3.8+
- Flask 3.x
