# Optional: run "python serve.py" here, then open http://localhost:8000/aero.html
# (a few games need to be served over http instead of opened as a plain file)
import http.server, socketserver
with socketserver.TCPServer(("", 8000), http.server.SimpleHTTPRequestHandler) as s:
    print("Aero -> http://localhost:8000/aero.html"); s.serve_forever()
