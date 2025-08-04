from flask import Flask
from babyagi import run_full_automation_cycle

app = Flask(__name__)

@app.route('/')
def home():
    return "✅ 7 Taps Quad-Core AI Orchestrator is live!"

@app.route('/dashboard')
def dashboard():
    results = run_full_automation_cycle()
    return results

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)