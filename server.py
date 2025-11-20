#!/usr/bin/env python3
"""
Simple HTTP server to launch the Vale flower visualization page.
Run this script and open http://localhost:8000 in your browser.
"""
import http.server
import socketserver
import webbrowser
import os
from pathlib import Path

PORT = 8000

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        super().end_headers()

def main():
    # Change to the script's directory
    os.chdir(Path(__file__).parent)
    
    with socketserver.TCPServer(("", PORT), MyHTTPRequestHandler) as httpd:
        print(f"Server running at http://localhost:{PORT}/")
        print(f"Open http://localhost:{PORT}/Index.html to view the visualization")
        print("Press Ctrl+C to stop the server")
        
        # Automatically open the browser
        try:
            webbrowser.open(f'http://localhost:{PORT}/Index.html')
        except:
            pass
        
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServer stopped.")

if __name__ == "__main__":
    main()
