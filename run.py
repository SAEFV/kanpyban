from threading import Thread
from app import create_app
import webview

app = create_app()

def run_flask():
    app.run(debug=False, port=5000)

if __name__ == '__main__':
    flask_thread = Thread(target=run_flask)
    flask_thread.daemon = True
    flask_thread.start()

    webview.create_window("Kanpyban", "http://127.0.0.1:5000", width=1000, height=700)
