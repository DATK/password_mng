from src.Server import app
import webbrowser
from src.config import debug, port

if __name__=="__main__":
    webbrowser.open(f'http://127.0.0.1:{port}', new=2)
    app.run(debug=debug,port=port)
      