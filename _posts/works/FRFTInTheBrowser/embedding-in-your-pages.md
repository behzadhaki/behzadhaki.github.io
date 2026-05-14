<style>
/* ── Controls row ─────────────────────────────────────────── */
.frft-embeds .fe-controls {
  display:flex; align-items:center; gap:8px; flex-wrap:wrap;
  background:rgba(255,255,255,0.04);
  border:1px solid rgba(255,255,255,0.1);
  border-radius:8px; padding:10px 14px;
}
.frft-embeds .fe-controls label {
  font-size:11px; color:var(--global-text-color-light); white-space:nowrap;
}
.frft-embeds .fe-controls input[type="number"],
.frft-embeds .fe-controls input[type="text"] {
  width:56px; background:#1c1c1c; border:1px solid rgba(255,255,255,0.15);
  border-radius:5px; padding:4px 7px; font-size:12px; color:#d0d0d0; outline:none;
}
.frft-embeds .fe-controls input:focus { border-color:rgba(255,255,255,0.4); }
.frft-embeds .fe-controls select {
  background:#1c1c1c; border:1px solid rgba(255,255,255,0.15);
  border-radius:5px; padding:4px 7px; font-size:12px; color:#d0d0d0;
  outline:none; cursor:pointer;
}
.frft-embeds .fe-controls select:focus { border-color:rgba(255,255,255,0.4); }
.frft-embeds .fe-controls select:disabled,
.frft-embeds .fe-controls input:disabled { opacity:0.35; cursor:not-allowed; }
.frft-embeds .fe-controls button {
  padding:5px 14px;
  background:transparent; color:rgba(255,255,255,0.65);
  border:1px solid rgba(255,255,255,0.22);
  border-radius:6px; font-size:12px; font-weight:500; cursor:pointer;
  transition:background 0.15s, border-color 0.15s;
}
.frft-embeds .fe-controls button:hover {
  background:rgba(255,255,255,0.1); border-color:rgba(255,255,255,0.38);
}

/* ── Embed code block ─────────────────────────────────────── */
.frft-embeds .fe-code-wrap {
  position:relative; background:#1c1c1c; border-radius:8px;
  padding:10px 42px 10px 12px; margin-top:0.5rem;
}
.frft-embeds .fe-code-wrap pre {
  font-family:"SF Mono","Fira Code",Consolas,monospace;
  font-size:9px; line-height:1.5; color:#d0d0d0 !important;
  white-space:pre-wrap; word-break:break-all; margin:0;
  background:transparent !important;
}
.frft-embeds .fe-copy-btn {
  position:absolute; top:7px; right:7px;
  background:#2a2a2a; border:none; border-radius:5px;
  color:#d0d0d0; cursor:pointer; padding:4px 7px;
  font-size:13px; line-height:1; transition:background 0.15s;
}
.frft-embeds .fe-copy-btn:hover  { background:#444; }
.frft-embeds .fe-copy-btn.copied { background:#a6e3a1; color:#1e1e2e; }

/* ── Side-by-side row: widget left, code right ────────────── */
.frft-embeds .fe-bottom-row {
  display:flex; gap:1rem; align-items:stretch; margin-top:0.5rem;
}
.frft-embeds .fe-bottom-row .fe-frame-wrap { flex-shrink:0; margin-top:0; }
.frft-embeds .fe-bottom-row .fe-code-wrap  { flex:1; min-width:0; margin-top:0; overflow-y:auto; }

/* ── Live preview frame ───────────────────────────────────── */
.frft-embeds .fe-frame-wrap {
  display:block; width:fit-content;
  background:#1a1a1a; border-radius:8px;
}
.frft-embeds .fe-frame-wrap iframe { display:block; border:none; }

/* ── Global hosting bar ─────────────────────────────────── */
.fe-hosting-bar {
  display:flex; align-items:center; gap:10px; flex-wrap:wrap;
  background:rgba(255,255,255,0.04);
  border:1px solid rgba(255,255,255,0.1);
  border-radius:8px; padding:10px 14px; margin-bottom:1.2rem;
}
.fe-hosting-bar .fe-bar-title {
  font-size:11px; font-weight:700; letter-spacing:0.06em;
  text-transform:uppercase; color:var(--global-text-color-light); white-space:nowrap;
}
.fe-hosting-bar label { font-size:12px; color:var(--global-text-color-light); white-space:nowrap; }
.fe-hosting-bar select {
  background:#1c1c1c; border:1px solid rgba(255,255,255,0.15);
  border-radius:5px; padding:4px 7px; font-size:12px; color:#d0d0d0;
  outline:none; cursor:pointer;
}
.fe-hosting-bar select:focus { border-color:rgba(255,255,255,0.35); }
.fe-hosting-bar button {
  padding:5px 13px;
  background:transparent; color:rgba(255,255,255,0.65);
  border:1px solid rgba(255,255,255,0.22);
  border-radius:6px; font-size:12px; font-weight:500; cursor:pointer;
  transition:background 0.15s, border-color 0.15s;
}
.fe-hosting-bar button:hover:not(:disabled) {
  background:rgba(255,255,255,0.1); border-color:rgba(255,255,255,0.38);
}
.fe-hosting-bar button:disabled { opacity:0.5; cursor:default; }

/* ── Self-host instructions note ────────────────────────── */
.fe-selfhost-note {
  background:rgba(255,255,255,0.03);
  border:1px solid rgba(255,255,255,0.08);
  border-radius:8px; padding:12px 16px; margin-bottom:1.2rem;
  font-size:13px; line-height:1.6; color:var(--global-text-color);
}
.fe-selfhost-note strong { color:var(--global-text-color); }
.fe-selfhost-note code {
  background:rgba(255,255,255,0.08); border-radius:3px;
  padding:1px 5px; font-family:monospace; font-size:12px; color:inherit;
}
.fe-selfhost-note ol { margin:6px 0 0 18px; }

/* ── Light-mode overrides ─────────────────────────────────── */
html[data-theme='light'] .fe-hosting-bar {
  background:rgba(0,0,0,0.04); border-color:rgba(0,0,0,0.12);
}
html[data-theme='light'] .fe-hosting-bar select {
  background:#fff; border-color:rgba(0,0,0,0.18); color:#1a1827;
}
html[data-theme='light'] .fe-hosting-bar button {
  background:#e8e8ee; color:#1a1827; border-color:rgba(0,0,0,0.15);
}
html[data-theme='light'] .fe-hosting-bar button:hover:not(:disabled) { background:#d0d0da; }
html[data-theme='light'] .fe-selfhost-note {
  background:rgba(0,0,0,0.03); border-color:rgba(0,0,0,0.1);
}
html[data-theme='light'] .fe-selfhost-note code { background:rgba(0,0,0,0.07); }
html[data-theme='light'] .frft-embeds .fe-controls {
  background:rgba(0,0,0,0.04);
  border-color:rgba(0,0,0,0.12);
}
html[data-theme='light'] .frft-embeds .fe-controls input[type="number"],
html[data-theme='light'] .frft-embeds .fe-controls input[type="text"] {
  background:#fff; border-color:rgba(0,0,0,0.18); color:#1a1827;
}
html[data-theme='light'] .frft-embeds .fe-controls select {
  background:#fff; border-color:rgba(0,0,0,0.18); color:#1a1827;
}
/* Keep the code block dark in light mode (site overrides pre with !important) */
html[data-theme='light'] .frft-embeds .fe-code-wrap {
  background:#1c1c1c !important;
}
html[data-theme='light'] .frft-embeds .fe-controls button {
  color:rgba(0,0,0,0.6); border-color:rgba(0,0,0,0.22);
}
html[data-theme='light'] .frft-embeds .fe-controls button:hover {
  background:rgba(0,0,0,0.07); border-color:rgba(0,0,0,0.38);
}
html[data-theme='light'] .fe-hosting-bar button {
  background:#e8e8e8; color:#333; border-color:rgba(0,0,0,0.2);
}
html[data-theme='light'] .fe-hosting-bar button:hover:not(:disabled) { background:#d4d4d4; }
</style>

<div class="fe-hosting-bar">
  <span class="fe-bar-title">Hosting</span>
  <label>Mode</label>
  <select id="feHostMode">
    <option value="direct" selected>Linked to behzadhaki.com</option>
    <option value="selfhost">Self-host on your server</option>
  </select>
  <button id="feDownloadZip" style="display:none">⬇ Download Files</button>
</div>
<div class="fe-selfhost-note" id="feSelfhostNote" style="display:none">
  <strong>Self-hosting setup</strong>
  <ol>
    <li>Click <strong>⬇ Download Files</strong> above to get <code>frft-embeds.zip</code>.</li>
    <li>Extract the ZIP and copy the <code>web/</code> folder into your site's <code>assets/</code> directory so the path becomes <code>assets/web/frft/…</code>.</li>
    <li>Paste the embed snippet for each widget (shown below) into your page.</li>
  </ol>
</div>

## Interactive FRFT

Full controls — let visitors change signal type, α order, block size and overlap directly in the widget.

<div class="frft-embeds">
<div class="fe-controls">
  <label>Width</label>
  <input type="number" id="fe1-w" value="600" min="200" step="10">
  <label>Height</label>
  <input type="number" id="fe1-h" value="220" min="100" step="10">
  <label>Type</label>
  <select id="fe1-type">
    <option value="">(default)</option>
    <option value="sine">Sine</option>
    <option value="sweep">Sweep</option>
  </select>
  <label id="fe1-freq-lbl">Freq (Hz)</label>
  <input type="number" id="fe1-freq" value="440" min="20" max="20000">
  <label>Dur (s)</label>
  <input type="number" id="fe1-dur" value="3" min="1" max="600">
  <label>α</label>
  <input type="number" id="fe1-alpha" value="0.10" min="0" max="4" step="0.00001">
  <label>Block</label>
  <select id="fe1-block">
    <option value="">(default)</option>
    <option value="256">256</option><option value="512">512</option>
    <option value="1024">1024</option><option value="2048">2048</option>
    <option value="4096">4096</option><option value="8192">8192</option>
    <option value="16384">16384</option><option value="32768">32768</option>
    <option value="65536">65536</option><option value="131072">131072</option>
    <option value="all">All (Windowed)</option>
    <option value="all-nowin">All (No Window)</option>
  </select>
  <label>Overlap</label>
  <select id="fe1-overlap">
    <option value="">(default)</option>
    <option value="1">×1</option><option value="2">×2</option>
    <option value="4">×4</option><option value="8">×8</option>
    <option value="16">×16</option>
  </select>
  <label>Half-spec</label>
  <select id="fe1-halfspec">
    <option value="">(default)</option>
    <option value="0">No</option><option value="1">Yes</option>
  </select>
  <button onclick="feApply1()">Apply</button>
</div>
<div class="fe-bottom-row">
<div class="fe-frame-wrap">
  <iframe id="fe1-frame" class="reframe-off" width="600" height="220"></iframe>
</div>
<div class="fe-code-wrap">
  <pre id="fe1-code"></pre>
  <button class="fe-copy-btn" onclick="feCopy('fe1-code',this)">⧉</button>
</div>
</div>
</div>

## Non-interactive FRFT

Fixed parameters set at embed time — auto-plays on load, no controls shown to the visitor.

<div class="frft-embeds">
<div class="fe-controls">
  <label>Width</label>
  <input type="number" id="fe2-w" value="600" min="200" step="10">
  <label>Height</label>
  <input type="number" id="fe2-h" value="220" min="100" step="10">
  <label>Type</label>
  <select id="fe2-type">
    <option value="sweep" selected>Sweep</option>
    <option value="sine">Sine</option>
    <option value="file">File picker</option>
  </select>
  <label id="fe2-freq-lbl">Freq (Hz)</label>
  <input type="number" id="fe2-freq" value="440" min="20" max="20000">
  <label>Dur (s)</label>
  <input type="number" id="fe2-dur" value="10" min="1" max="600">
  <label>α</label>
  <input type="number" id="fe2-alpha" value="0.10" min="0" max="4" step="0.00001">
  <label>Block</label>
  <select id="fe2-block">
    <option value="256">256</option><option value="512">512</option>
    <option value="1024">1024</option><option value="2048">2048</option>
    <option value="4096">4096</option><option value="8192">8192</option>
    <option value="16384" selected>16384</option><option value="32768">32768</option>
    <option value="65536">65536</option><option value="131072">131072</option>
    <option value="all">All (Windowed)</option>
    <option value="all-nowin">All (No Window)</option>
  </select>
  <label>Overlap</label>
  <select id="fe2-overlap">
    <option value="1">×1</option><option value="2">×2</option>
    <option value="4" selected>×4</option><option value="8">×8</option>
    <option value="16">×16</option>
  </select>
  <label>Half-spec</label>
  <select id="fe2-halfspec">
    <option value="0" selected>No</option><option value="1">Yes</option>
  </select>
  <button onclick="feApply2()">Apply</button>
</div>
<div class="fe-bottom-row">
<div class="fe-frame-wrap">
  <iframe id="fe2-frame" class="reframe-off" width="600" height="220"></iframe>
</div>
<div class="fe-code-wrap">
  <pre id="fe2-code"></pre>
  <button class="fe-copy-btn" onclick="feCopy('fe2-code',this)">⧉</button>
</div>
</div>
</div>

## Alpha (α) Sweep

Interactive slider that sweeps the fractional order α — shows how the spectrum rotates from time to frequency domain.

<div class="frft-embeds">
<div class="fe-controls">
  <label>Width</label>
  <input type="number" id="fe3-w" value="600" min="300" step="10">
  <label>Height</label>
  <input type="number" id="fe3-h" value="300" min="200" step="10">
  <label>Window</label>
  <select id="fe3-win">
    <option value="hann" selected>Hann</option>
    <option value="rect">Rectangular</option>
  </select>
  <label>Half-spec</label>
  <select id="fe3-halfspec">
    <option value="0" selected>No</option><option value="1">Yes</option>
  </select>
  <label>Init Freq</label>
  <select id="fe3-freqidx">
    <option value="0" selected>100 Hz</option>
    <option value="1">500 Hz</option><option value="2">1k Hz</option>
    <option value="3">2k Hz</option><option value="4">5k Hz</option>
    <option value="5">7.5k Hz</option><option value="6">10k Hz</option>
  </select>
  <label>Init α</label>
  <input type="number" id="fe3-alpha" value="0" min="0" max="1" step="0.05">
  <button onclick="feApply3()">Apply</button>
</div>
<div class="fe-bottom-row">
<div class="fe-frame-wrap">
  <iframe id="fe3-frame" class="reframe-off" width="600" height="300"></iframe>
</div>
<div class="fe-code-wrap">
  <pre id="fe3-code"></pre>
  <button class="fe-copy-btn" onclick="feCopy('fe3-code',this)">⧉</button>
</div>
</div>
</div>

## Overlap-Add Visualiser

Shows how block-processing artefacts change with different block sizes and overlap factors.

<div class="frft-embeds">
<div class="fe-controls">
  <label>Width</label>
  <input type="number" id="fe4-w" value="600" min="300" step="10">
  <label>Height</label>
  <input type="number" id="fe4-h" value="250" min="200" step="10">
  <label>Freq (Hz)</label>
  <input type="number" id="fe4-freq" value="440" min="20" max="20000">
  <label>α (order)</label>
  <input type="number" id="fe4-alpha" value="0.50" min="0" max="4" step="0.01">
  <label>Block</label>
  <select id="fe4-block">
    <option value="1024">1024</option><option value="2048">2048</option>
    <option value="4096">4096</option><option value="8192">8192</option>
    <option value="16384">16384</option><option value="32768">32768</option>
    <option value="65536">65536</option>
    <option value="131072" selected>131072</option>
  </select>
  <label>Overlap</label>
  <select id="fe4-overlap">
    <option value="1">×1 (no OLA)</option><option value="2">×2</option>
    <option value="4" selected>×4</option><option value="8">×8</option>
  </select>
  <label>Half-spec</label>
  <select id="fe4-halfspec">
    <option value="0" selected>No</option><option value="1">Yes</option>
  </select>
  <button onclick="feApply4()">Apply</button>
</div>
<div class="fe-bottom-row">
<div class="fe-frame-wrap">
  <iframe id="fe4-frame" class="reframe-off" width="600" height="250"></iframe>
</div>
<div class="fe-code-wrap">
  <pre id="fe4-code"></pre>
  <button class="fe-copy-btn" onclick="feCopy('fe4-code',this)">⧉</button>
</div>
</div>
</div>

<script>
(function () {
  const DEMO_BASE         = '/assets/web/frft/demos/';
  const EMBED_BASE_DIRECT = 'https://behzadhaki.com/assets/web/frft/demos/';
  const EMBED_BASE_SELF   = '/assets/web/frft/demos/';

  function getEmbedBase() {
    const m = document.getElementById('feHostMode');
    return (m && m.value === 'selfhost') ? EMBED_BASE_SELF : EMBED_BASE_DIRECT;
  }

  function g(id) { return document.getElementById(id); }

  function buildCode(file, params, w, h) {
    const src = getEmbedBase() + file + '?' + params;
    return '<div style="width:100%; max-width:' + w + 'px;">\n' +
           '  <iframe src="' + src + '"\n' +
           '          style="width:100%; height:' + h + 'px; border:none; display:block"\n' +
           '          allow="autoplay">\n' +
           '  </iframe>\n' +
           '</div>';
  }

  function loadFrame(frameId, file, liveParams, w, h) {
    const fr = g(frameId);
    fr.width = w; fr.height = h;
    fr.src = DEMO_BASE + file + '?' + liveParams + '&v=' + Date.now();
  }

  window.feCopy = function(codeId, btn) {
    navigator.clipboard.writeText(g(codeId).textContent).then(() => {
      btn.textContent = '✓'; btn.classList.add('copied');
      setTimeout(() => { btn.textContent = '⧉'; btn.classList.remove('copied'); }, 1800);
    });
  };

  /* ── 1. Interactive ──────────────────────────────────────── */
  window.feApply1 = function () {
    const w = Math.max(200, parseInt(g('fe1-w').value) || 600);
    const h = Math.max(100, parseInt(g('fe1-h').value) || 220);
    g('fe1-w').value = w; g('fe1-h').value = h;
    const p = new URLSearchParams({ w, h });
    const type = g('fe1-type').value;
    if (type) p.set('type', type);
    if (type === 'sine') p.set('freq', g('fe1-freq').value);
    p.set('dur',   g('fe1-dur').value);
    p.set('alpha', g('fe1-alpha').value);
    const block = g('fe1-block').value;
    if (block)   p.set('blocksize', block);
    const overlap = g('fe1-overlap').value;
    if (overlap) p.set('overlap', overlap);
    const hs = g('fe1-halfspec').value;
    if (hs)      p.set('halfspec', hs);
    g('fe1-code').textContent = buildCode('embed_interactive_frft.html', p.toString(), w, h);
    loadFrame('fe1-frame', 'embed_interactive_frft.html', p.toString(), w, h);
    const isSine = type === 'sine';
    g('fe1-freq').disabled = !isSine;
    g('fe1-freq-lbl').style.opacity = isSine ? '1' : '0.4';
  };
  g('fe1-type').addEventListener('change', feApply1);
  feApply1();

  /* ── 2. Non-interactive ──────────────────────────────────── */
  window.feApply2 = function () {
    const w = Math.max(200, parseInt(g('fe2-w').value) || 600);
    const h = Math.max(100, parseInt(g('fe2-h').value) || 220);
    g('fe2-w').value = w; g('fe2-h').value = h;
    const type = g('fe2-type').value;
    const block = g('fe2-block').value;
    const isAll = block === 'all' || block === 'all-nowin';
    g('fe2-overlap').disabled = isAll;
    const isSine = type === 'sine';
    g('fe2-freq').disabled = !isSine;
    g('fe2-freq-lbl').style.opacity = isSine ? '1' : '0.4';
    const p = new URLSearchParams({ w, h,
      type, dur: g('fe2-dur').value, alpha: g('fe2-alpha').value,
      blocksize: block, overlap: isAll ? '1' : g('fe2-overlap').value,
      halfspec: g('fe2-halfspec').value,
    });
    if (isSine) p.set('freq', g('fe2-freq').value);
    g('fe2-code').textContent = buildCode('embed_non_interactive_frft.html', p.toString(), w, h);
    loadFrame('fe2-frame', 'embed_non_interactive_frft.html', p.toString(), w, h);
  };
  g('fe2-type').addEventListener('change', feApply2);
  g('fe2-block').addEventListener('change', feApply2);
  g('fe2-overlap').addEventListener('change', feApply2);
  g('fe2-halfspec').addEventListener('change', feApply2);
  feApply2();

  /* ── 3. Alpha sweep ──────────────────────────────────────── */
  window.feApply3 = function () {
    const w = Math.max(300, parseInt(g('fe3-w').value) || 600);
    const h = Math.max(200, parseInt(g('fe3-h').value) || 300);
    g('fe3-w').value = w; g('fe3-h').value = h;
    const p = new URLSearchParams({ w, h,
      win: g('fe3-win').value, halfspec: g('fe3-halfspec').value,
      freqidx: g('fe3-freqidx').value, alpha: g('fe3-alpha').value,
    });
    g('fe3-code').textContent = buildCode('embed_alpha_sweep_frft.html', p.toString(), w, h);
    loadFrame('fe3-frame', 'embed_alpha_sweep_frft.html', p.toString(), w, h);
  };
  feApply3();

  /* ── 4. OLA ──────────────────────────────────────────────── */
  window.feApply4 = function () {
    const w = Math.max(300, parseInt(g('fe4-w').value) || 600);
    const h = Math.max(200, parseInt(g('fe4-h').value) || 250);
    g('fe4-w').value = w; g('fe4-h').value = h;
    const p = new URLSearchParams({ w, h,
      freq: g('fe4-freq').value, alpha: g('fe4-alpha').value,
      blocksize: g('fe4-block').value, overlap: g('fe4-overlap').value,
      halfspec: g('fe4-halfspec').value,
    });
    g('fe4-code').textContent = buildCode('embed_ola_frft.html', p.toString(), w, h);
    loadFrame('fe4-frame', 'embed_ola_frft.html', p.toString(), w, h);
  };
  g('fe4-block').addEventListener('change', feApply4);
  g('fe4-overlap').addEventListener('change', feApply4);
  g('fe4-halfspec').addEventListener('change', feApply4);
  feApply4();

  /* ── Hosting mode (registered after all feApplyN are defined) ─────────── */
  const feHostMode     = g('feHostMode');
  const feSelfhostNote = g('feSelfhostNote');
  const feDownloadZip  = g('feDownloadZip');

  function syncHostUI() {
    const isSelf = feHostMode.value === 'selfhost';
    feSelfhostNote.style.display = isSelf ? 'block' : 'none';
    feDownloadZip.style.display  = isSelf ? '' : 'none';
  }
  feHostMode.addEventListener('change', function () {
    syncHostUI();
    feApply1(); feApply2(); feApply3(); feApply4();
  });
  syncHostUI();

  /* ── ZIP download ────────────────────────────────────────────────────── */
  const ZIP_FILES = [
    { src:'/assets/web/frft/demos/embed_interactive_frft.html',     dst:'web/frft/demos/embed_interactive_frft.html' },
    { src:'/assets/web/frft/demos/embed_non_interactive_frft.html', dst:'web/frft/demos/embed_non_interactive_frft.html' },
    { src:'/assets/web/frft/demos/embed_alpha_sweep_frft.html',     dst:'web/frft/demos/embed_alpha_sweep_frft.html' },
    { src:'/assets/web/frft/demos/embed_ola_frft.html',             dst:'web/frft/demos/embed_ola_frft.html' },
    { src:'/assets/web/frft/audio/frft-worker.js',                  dst:'web/frft/audio/frft-worker.js' },
    { src:'/assets/web/frft/wasm/dist/frft.js',                     dst:'web/frft/wasm/dist/frft.js' },
    { src:'/assets/web/frft/wasm/dist/frft.wasm',                   dst:'web/frft/wasm/dist/frft.wasm' },
  ];

  feDownloadZip.addEventListener('click', async function () {
    feDownloadZip.disabled = true; feDownloadZip.textContent = 'Fetching…';
    try {
      const entries = await Promise.all(ZIP_FILES.map(async function ({ src, dst }) {
        const res = await fetch(src);
        if (!res.ok) throw new Error(src + ' → HTTP ' + res.status);
        return { name: dst, data: new Uint8Array(await res.arrayBuffer()) };
      }));
      const zip = buildZip(entries);
      const url = URL.createObjectURL(new Blob([zip], { type:'application/zip' }));
      Object.assign(document.createElement('a'), { href:url, download:'frft-embeds.zip' }).click();
      URL.revokeObjectURL(url);
    } catch (err) {
      alert('Download failed: ' + err.message);
    } finally {
      feDownloadZip.disabled = false; feDownloadZip.textContent = '⬇ Download Files';
    }
  });

  /* ── Minimal store-only ZIP builder ────────────────────────────────────── */
  function crc32(data) {
    if (!crc32._t) {
      crc32._t = new Uint32Array(256);
      for (let i = 0; i < 256; i++) {
        let c = i;
        for (let j = 0; j < 8; j++) c = (c & 1) ? (0xEDB88320 ^ (c >>> 1)) : (c >>> 1);
        crc32._t[i] = c;
      }
    }
    let c = 0xFFFFFFFF;
    for (let i = 0; i < data.length; i++) c = crc32._t[(c ^ data[i]) & 0xFF] ^ (c >>> 8);
    return (c ^ 0xFFFFFFFF) >>> 0;
  }

  function buildZip(files) {
    const enc = function (s) { return new TextEncoder().encode(s); };
    const u32 = function (v, a, o) { a[o]=v&0xff; a[o+1]=(v>>8)&0xff; a[o+2]=(v>>16)&0xff; a[o+3]=(v>>24)&0xff; };
    const u16 = function (v, a, o) { a[o]=v&0xff; a[o+1]=(v>>8)&0xff; };
    const entries = [], cdir = [];
    let offset = 0;
    for (const { name, data } of files) {
      const nm = enc(name), crc = crc32(data), hdr = new Uint8Array(30 + nm.length);
      hdr.set([0x50,0x4b,0x03,0x04, 0x14,0, 0,0, 0,0, 0,0,0,0]);
      u32(crc, hdr, 14); u32(data.length, hdr, 18); u32(data.length, hdr, 22);
      u16(nm.length, hdr, 26); hdr.set(nm, 30);
      const cd = new Uint8Array(46 + nm.length);
      cd.set([0x50,0x4b,0x01,0x02, 0x14,0, 0x14,0, 0,0, 0,0, 0,0,0,0]);
      u32(crc, cd, 16); u32(data.length, cd, 20); u32(data.length, cd, 24);
      u16(nm.length, cd, 28); cd.set(nm, 46); u32(offset, cd, 42);
      entries.push(hdr, data); cdir.push(cd);
      offset += hdr.length + data.length;
    }
    const cdData = new Uint8Array(cdir.reduce(function (a, c) { return a + c.length; }, 0));
    let cdOff = 0; for (const c of cdir) { cdData.set(c, cdOff); cdOff += c.length; }
    const eocd = new Uint8Array(22);
    eocd.set([0x50,0x4b,0x05,0x06, 0,0, 0,0]);
    u16(files.length, eocd, 8); u16(files.length, eocd, 10);
    u32(cdData.length, eocd, 12); u32(offset, eocd, 16);
    const all = [...entries, cdData, eocd];
    const out = new Uint8Array(all.reduce(function (a, c) { return a + c.length; }, 0));
    let p = 0; for (const a of all) { out.set(a, p); p += a.length; }
    return out;
  }
})();
</script>
