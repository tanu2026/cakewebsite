from flask import Flask, render_template, request, redirect, url_for, flash
import os

# Tell Flask to look for templates in the SAME folder as this file
app = Flask(__name__, template_folder=os.path.dirname(os.path.abspath(__file__)))
app.secret_key = "cakeshop_secret_2024"

# ── Sample data ──────────────────────────────────────────────────────────────

CAKES = [
    {"id":1,"name":"Classic Vanilla Dream","category":"Classic","price":45.00,
     "description":"Light, fluffy vanilla sponge layered with fresh cream and topped with hand-piped rosettes. A timeless favourite for every celebration.",
     "emoji":"🎂","tag":"Bestseller"},
    {"id":2,"name":"Dark Chocolate Obsession","category":"Chocolate","price":55.00,
     "description":"Rich Belgian dark chocolate layers with ganache filling and a mirror-glaze finish that makes every slice utterly irresistible.",
     "emoji":"🍫","tag":"Popular"},
    {"id":3,"name":"Strawberry Bliss","category":"Fruit","price":50.00,
     "description":"Fresh strawberry compote between delicate vanilla layers, draped in whipped cream and crowned with whole strawberries.",
     "emoji":"🍓","tag":"Seasonal"},
    {"id":4,"name":"Lemon Zest Delight","category":"Fruit","price":48.00,
     "description":"Tangy lemon curd paired with light sponge and lemon-cream frosting — sunshine in every bite.",
     "emoji":"🍋","tag":"New"},
    {"id":5,"name":"Red Velvet Romance","category":"Classic","price":58.00,
     "description":"Velvety red layers with cream-cheese frosting — deep, dramatic, and utterly luxurious.",
     "emoji":"❤️","tag":"Romantic"},
    {"id":6,"name":"Caramel Crunch Tower","category":"Specialty","price":65.00,
     "description":"Salted caramel buttercream stacked high with toffee crunch layers and a dramatic caramel drip.",
     "emoji":"🍮","tag":"Indulgent"},
    {"id":7,"name":"Matcha Green Dream","category":"Specialty","price":60.00,
     "description":"Japanese ceremonial matcha sponge with white-chocolate cream and delicate gold leaf decoration.",
     "emoji":"🍵","tag":"Artisan"},
    {"id":8,"name":"Funfetti Celebration","category":"Classic","price":42.00,
     "description":"Rainbow sprinkle-studded vanilla cake with cloud-like vanilla buttercream. Pure joy on a plate.",
     "emoji":"🎉","tag":"Fun"},
]

TESTIMONIALS = [
    {"name":"Priya S.","text":"Ordered the Chocolate Obsession for my wedding anniversary — everyone was speechless. Absolutely divine!","stars":5},
    {"name":"Rohan M.","text":"The Lemon Zest Delight was the highlight of our office party. Fresh, light, and perfectly balanced.","stars":5},
    {"name":"Ananya K.","text":"Stunning presentation and even better taste. My daughter's birthday was truly special thanks to Crumble & Co.","stars":5},
]

# ── Routes ────────────────────────────────────────────────────────────────────

@app.route("/")
def home():
    featured = [c for c in CAKES if c["tag"] in ("Bestseller","Popular","Romantic")][:3]
    return render_template("index.html", featured=featured, testimonials=TESTIMONIALS)

@app.route("/menu")
def menu():
    category = request.args.get("category","All")
    categories = ["All"] + sorted(set(c["category"] for c in CAKES))
    filtered = CAKES if category == "All" else [c for c in CAKES if c["category"] == category]
    return render_template("menu.html", cakes=filtered, categories=categories, active=category)

@app.route("/cake/<int:cake_id>")
def cake_detail(cake_id):
    cake = next((c for c in CAKES if c["id"] == cake_id), None)
    if not cake:
        return redirect(url_for("menu"))
    related = [c for c in CAKES if c["category"] == cake["category"] and c["id"] != cake_id][:3]
    return render_template("detail.html", cake=cake, related=related)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact", methods=["GET","POST"])
def contact():
    if request.method == "POST":
        name    = request.form.get("name","").strip()
        email   = request.form.get("email","").strip()
        message = request.form.get("message","").strip()
        if name and email and message:
            flash(f"Thank you, {name}! We'll be in touch soon. 🎂","success")
        else:
            flash("Please fill in all fields.","error")
        return redirect(url_for("contact"))
    return render_template("contact.html")

@app.route("/order", methods=["GET","POST"])
def order():
    if request.method == "POST":
        name        = request.form.get("name","").strip()
        cake_choice = request.form.get("cake","").strip()
        date        = request.form.get("date","").strip()
        if name and cake_choice and date:
            flash(f"🎉 Order placed! We'll bake your {cake_choice} for {date}, {name}!","success")
        else:
            flash("Please complete all fields.","error")
        return redirect(url_for("order"))
    return render_template("order.html", cakes=CAKES)

# ── Run ───────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    app.run(debug=True)
