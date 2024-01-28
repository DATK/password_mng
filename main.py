from src.Server import app
import webbrowser
from src.config import debug, port, host,ip

if __name__=="__main__":
    #ip="localhost"
    webbrowser.open(f'http://{ip}:{port}')
    app.run(debug=debug,port=port,host=host)
      