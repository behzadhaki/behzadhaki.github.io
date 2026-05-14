#!/usr/bin/env python3
"""
Dev server for the Jekyll Post Builder tool.

Serves the repo over HTTP AND accepts POST /write-files requests
so the browser tool can write files directly to disk without needing
the File System Access API (which is blocked in Brave).

Usage:
    python3 _tools/dev-server.py          # serves on port 4099
    python3 _tools/dev-server.py 4099     # explicit port

Then open: http://localhost:4099/_tools/new-post-builder.html
"""

import http.server
import json
import os
import base64
import sys
import urllib.parse
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 4099


class Handler(http.server.SimpleHTTPRequestHandler):

    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        params = urllib.parse.parse_qs(parsed.query)

        if parsed.path == '/read-file':
            rel = params.get('path', [''])[0].lstrip('/')
            if not rel:
                self._json(400, {'ok': False, 'error': 'path param required'}); return
            dest = (REPO_ROOT / rel).resolve()
            try:
                dest.relative_to(REPO_ROOT.resolve())  # security: stay in repo
                if dest.is_file():
                    self._json(200, {'ok': True, 'content': dest.read_text(encoding='utf-8')})
                else:
                    self._json(404, {'ok': False, 'error': 'File not found'})
            except Exception as e:
                self._json(500, {'ok': False, 'error': str(e)})

        elif parsed.path == '/touch-file':
            rel = params.get('path', [''])[0].lstrip('/')
            if not rel:
                self._json(400, {'ok': False, 'error': 'path param required'}); return
            dest = (REPO_ROOT / rel).resolve()
            try:
                dest.relative_to(REPO_ROOT.resolve())
                if dest.is_file():
                    import os as _os
                    _os.utime(dest, None)  # update mtime to now
                    self._json(200, {'ok': True})
                else:
                    self._json(404, {'ok': False, 'error': 'File not found'})
            except Exception as e:
                self._json(500, {'ok': False, 'error': str(e)})

        elif parsed.path == '/list-dir':
            rel = params.get('path', [''])[0].lstrip('/')
            dest = (REPO_ROOT / rel).resolve()
            try:
                dest.relative_to(REPO_ROOT.resolve())
                if dest.is_dir():
                    files = sorted(f.name for f in dest.iterdir() if f.is_file())
                    self._json(200, {'ok': True, 'files': files})
                else:
                    self._json(404, {'ok': False, 'error': 'Directory not found'})
            except Exception as e:
                self._json(500, {'ok': False, 'error': str(e)})

        else:
            super().do_GET()

    def do_OPTIONS(self):
        self.send_response(200)
        self._cors_headers()
        self.end_headers()

    def do_POST(self):
        if self.path == '/write-files':
            try:
                length = int(self.headers.get('Content-Length', 0))
                body = json.loads(self.rfile.read(length))
                files = body.get('files', [])
                written = []
                for f in files:
                    rel = f['path'].lstrip('/')
                    dest = REPO_ROOT / rel
                    dest.parent.mkdir(parents=True, exist_ok=True)
                    if f.get('binary'):
                        dest.write_bytes(base64.b64decode(f['content']))
                    else:
                        dest.write_text(f.get('content', ''), encoding='utf-8')
                    written.append(rel)
                self._json(200, {'ok': True, 'written': written})
            except Exception as e:
                self._json(500, {'ok': False, 'error': str(e)})
        else:
            self._json(404, {'ok': False, 'error': 'Not found'})

    def _json(self, code, payload):
        body = json.dumps(payload).encode()
        self.send_response(code)
        self._cors_headers()
        self.send_header('Content-Type', 'application/json')
        self.send_header('Content-Length', str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _cors_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')

    def log_message(self, fmt, *args):
        # Suppress noisy GET logs, keep errors
        if args and str(args[1]) not in ('200', '304'):
            super().log_message(fmt, *args)


if __name__ == '__main__':
    os.chdir(REPO_ROOT)
    server = http.server.HTTPServer(('', PORT), Handler)
    print(f'  Jekyll Post Builder server')
    print(f'  Repo root : {REPO_ROOT}')
    print(f'  Open      : http://localhost:{PORT}/_tools/new-post-builder.html')
    print(f'  Ctrl+C to stop\n')
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print('\nStopped.')
