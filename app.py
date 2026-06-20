from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>AI Customer Support Chatbot</h1>

    <form action="/chat">
        <input name="msg" placeholder="Type your question">
        <button type="submit">Send</button>
    </form>
    """

@app.route("/chat")
def chat():

    msg = request.args.get("msg","").lower()

    if "hello" in msg:
        reply = "Hello! Welcome to Customer Support."

    elif "contact" in msg:
        reply = "Contact us at 9876543210."

    elif "timing" in msg:
        reply = "Office timing is 9 AM to 6 PM."

    elif "service" in msg:
        reply = "We provide AI and Machine Learning solutions."

    elif "bye" in msg:
        reply = "Thank you for visiting."

    else:
        reply = "Sorry, I did not understand your question."

    return f"<h3>User: {msg}</h3><h3>Bot: {reply}</h3><br><a href='/'>Back</a>"

app.run(host="0.0.0.0", port=81)
