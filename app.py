from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

cart = []

prices = {
    "VapoRub": 15,
    "Jujube Jelly": 3,
    "M&G Jelly": 2,
    "Hong Sah Pill": 5,
    "Sharpener": 1
}

@app.route("/add_item", methods=["POST"])
def add_item():
    data = request.json
    label = data["label"]

    item = {
        "label": label,
        "price": prices.get(label, 0),
        "taken": 1,
        "total": prices.get(label, 0)
    }

    cart.append(item)

    return jsonify({"ok": True, "item": item})

@app.route("/cart")
def cart_data():
    return jsonify({
        "cart": cart,
        "grand_total": sum(i["total"] for i in cart)
    })

@app.route("/clear", methods=["DELETE"])
def clear():
    cart.clear()
    return jsonify({"ok": True})

if __name__ == "__main__":
    app.run()