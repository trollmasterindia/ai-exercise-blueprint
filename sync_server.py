#!/usr/bin/env python3
import http.server
import json
import os
import sys

PORT = 8789
VAULT_PATH = '/Users/nipunmehra/Desktop/ai-exercise-blueprint/logs/active_workout_state.json'
HTML_PATHS = [
    '/Users/nipunmehra/Desktop/interactive_muscle_feedback.html',
    '/Users/nipunmehra/Desktop/ai-exercise-blueprint/interactive_muscle_feedback.html',
    '/Users/nipunmehra/Desktop/ai-exercise-blueprint/index.html'
]

class SyncHandler(http.server.BaseHTTPRequestHandler):
    def _set_headers(self, status=200):
        self.send_response(status)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

    def do_OPTIONS(self):
        self._set_headers(200)

    def do_HEAD(self):
        self.do_GET()

    def do_GET(self):
        from urllib.parse import urlparse, parse_qs
        parsed = urlparse(self.path)
        path = parsed.path
        query = parse_qs(parsed.query)

        if path in ['/', '/index.html', '/interactive_muscle_feedback.html']:
            html_target = '/Users/nipunmehra/Desktop/interactive_muscle_feedback.html'
            if os.path.exists(html_target):
                with open(html_target, 'rb') as f:
                    content = f.read()
                self.send_response(200)
                self.send_header('Content-Type', 'text/html; charset=utf-8')
                self.send_header('Content-Length', str(len(content)))
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                self.wfile.write(content)
            else:
                self._set_headers(404)
                self.wfile.write(json.dumps({'error': 'File not found'}).encode('utf-8'))
        elif path == '/player':
            yt_id = query.get('id', [''])[0]
            start_sec = query.get('start', ['0'])[0]
            player_html = f"""<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="referrer" content="strict-origin-when-cross-origin">
  <style>
    html, body {{ margin: 0; padding: 0; width: 100%; height: 100%; overflow: hidden; background: #000; }}
    iframe {{ width: 100%; height: 100%; border: none; display: block; }}
  </style>
</head>
<body>
  <iframe src="https://www.youtube.com/embed/{yt_id}?start={start_sec}&autoplay=1&rel=0&playsinline=1&modestbranding=1" 
          allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" 
          referrerpolicy="strict-origin-when-cross-origin" 
          allowfullscreen></iframe>
</body>
</html>"""
            body = player_html.encode('utf-8')
            self.send_response(200)
            self.send_header('Content-Type', 'text/html; charset=utf-8')
            self.send_header('Content-Length', str(len(body)))
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(body)
        elif path == '/api/status':
            self._set_headers(200)
            self.wfile.write(json.dumps({'status': 'active', 'port': PORT}).encode('utf-8'))
        elif self.path == '/api/state':
            if os.path.exists(VAULT_PATH):
                with open(VAULT_PATH, 'r', encoding='utf-8') as f:
                    data = f.read()
                self._set_headers(200)
                self.wfile.write(data.encode('utf-8'))
            else:
                self._set_headers(404)
                self.wfile.write(json.dumps({'error': 'No state found'}).encode('utf-8'))
        else:
            self._set_headers(404)
            self.wfile.write(json.dumps({'error': 'Endpoint not found'}).encode('utf-8'))

    def do_POST(self):
        if self.path == '/api/sync':
            try:
                content_len = int(self.headers.get('Content-Length', 0))
                body = self.rfile.read(content_len).decode('utf-8')
                data = json.loads(body)

                # 1. Save canonical JSON state
                os.makedirs(os.path.dirname(VAULT_PATH), exist_ok=True)
                with open(VAULT_PATH, 'w', encoding='utf-8') as f:
                    json.dump(data, f, indent=2)

                print(f'[SyncServer] Successfully synced {len(data)} exercises to active_workout_state.json')

                self._set_headers(200)
                self.wfile.write(json.dumps({'success': True, 'keys_saved': len(data)}).encode('utf-8'))
            except Exception as e:
                print(f'[SyncServer] Error during sync: {e}')
                self._set_headers(500)
                self.wfile.write(json.dumps({'error': str(e)}).encode('utf-8'))
        else:
            self._set_headers(404)
            self.wfile.write(json.dumps({'error': 'Endpoint not found'}).encode('utf-8'))

def run():
    server_address = ('127.0.0.1', PORT)
    httpd = http.server.HTTPServer(server_address, SyncHandler)
    print(f'[SyncServer] Local Workout Vault Sync Server listening on http://127.0.0.1:{PORT}')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print('[SyncServer] Shutting down...')
        httpd.server_close()

if __name__ == '__main__':
    run()
