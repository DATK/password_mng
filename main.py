from src.Server import app
import webbrowser

if __name__=="__main__":
    webbrowser.open('http://127.0.0.1:6070', new=2)
    app.run(debug=1,port=6070)
      