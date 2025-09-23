from flask import Flask, jsonify
import random

app = Flask(__name__)

# An expanded in-memory "database" of quotes
QUOTES = [
    {"author": "Grace Hopper", "quote": "The most damaging phrase in the language is 'We've always done it this way.'"},
    {"author": "Linus Torvalds", "quote": "Talk is cheap. Show me the code."},
    {"author": "Ada Lovelace", "quote": "The Analytical Engine has no pretensions whatever to originate anything. It can do whatever we know how to order it to perform."},
    {"author": "Albert Einstein", "quote": "Imagination is more important than knowledge. Knowledge is limited. Imagination encircles the world."},
    {"author": "Steve Jobs", "quote": "The only way to do great work is to love what you do."},
    {"author": "Bill Gates", "quote": "Your most unhappy customers are your greatest source of learning."},
    {"author": "Richard Feynman", "quote": "The first principle is that you must not fool yourself and you are the easiest person to fool."},
    {"author": "Martin Fowler", "quote": "Any fool can write code that a computer can understand. Good programmers write code that humans can understand."},
    {"author": "Alan Turing", "quote": "We can only see a short distance ahead, but we can see plenty there that needs to be done."},
    {"author": "Donald Knuth", "quote": "Premature optimization is the root of all evil."},
    {"author": "Edsger W. Dijkstra", "quote": "Simplicity is a prerequisite for reliability."},
    {"author": "Tim Berners-Lee", "quote": "The web as I envisaged it, we have not seen it yet. The future is still so much bigger than the past."},
    {"author": "Nikola Tesla", "quote": "The present is theirs; the future, for which I have really worked, is mine."},
    {"author": "Vint Cerf", "quote": "The internet is a reflection of our society and that mirror is going to be reflecting what we see."}
]

@app.route('/quote')
def get_random_quote():
    """Returns a single random quote."""
    return jsonify(random.choice(QUOTES))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)