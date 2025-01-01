from ai_fungeon_api import app

@app.route('/')
def index():
    return 'Hello World!'
