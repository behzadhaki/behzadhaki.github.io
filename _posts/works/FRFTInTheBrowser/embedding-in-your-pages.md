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
  width:72px; background:#1e1e2e; border:1px solid rgba(255,255,255,0.15);
  border-radius:5px; padding:4px 7px; font-size:12px; color:#cdd6f4; outline:none;
}
.frft-embeds .fe-controls input:focus { border-color:#4a9eff; }
.frft-embeds .fe-controls select {
  background:#1e1e2e; border:1px solid rgba(255,255,255,0.15);
  border-radius:5px; padding:4px 7px; font-size:12px; color:#cdd6f4;
  outline:none; cursor:pointer;
}
.frft-embeds .fe-controls select:focus { border-color:#4a9eff; }
.frft-embeds .fe-controls select:disabled,
.frft-embeds .fe-controls input:disabled { opacity:0.35; cursor:not-allowed; }
.frft-embeds .fe-controls button {
  padding:5px 14px; background:#4a9eff; color:#fff; border:none;
  border-radius:6px; font-size:12px; font-weight:600; cursor:pointer;
}
.frft-embeds .fe-controls button:hover { background:#2d84f0; }

/* ── Embed code block ─────────────────────────────────────── */
.frft-embeds .fe-code-wrap {
  position:relative; background:#1e1e2e; border-radius:8px;
  padding:10px 42px 10px 12px; margin-top:0.5rem;
}
.frft-embeds .fe-code-wrap pre {
  font-family:"SF Mono","Fira Code",Consolas,monospace;
  font-size:11px; line-height:1.55; color:#cdd6f4 !important;
  white-space:pre; overflow-x:auto; margin:0;
  background:transparent !important;
}
.frft-embeds .fe-copy-btn {
  position:absolute; top:7px; right:7px;
  background:#313244; border:none; border-radius:5px;
  color:#cdd6f4; cursor:pointer; padding:4px 7px;
  font-size:13px; line-height:1; transition:background 0.15s;
}
.frft-embeds .fe-copy-btn:hover  { background:#45475a; }
.frft-embeds .fe-copy-btn.copied { background:#a6e3a1; color:#1e1e2e; }

/* ── Live preview frame ───────────────────────────────────── */
.frft-embeds .fe-frame-wrap {
  display:block; width:fit-content; margin-top:0.5rem;
  background:#1a1a1a; border-radius:8px;
}
.frft-embeds .fe-frame-wrap iframe { display:block; border:none; }

/* ── Light-mode overrides ─────────────────────────────────── */
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
  background:#1e1e2e !important;
}
</style>

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
<div class="fe-code-wrap">
  <pre id="fe1-code"></pre>
  <button class="fe-copy-btn" onclick="feCopy('fe1-code',this)">⧉</button>
</div>
<div class="fe-frame-wrap">
  <iframe id="fe1-frame" class="reframe-off" width="600" height="220"></iframe>
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
<div class="fe-code-wrap">
  <pre id="fe2-code"></pre>
  <button class="fe-copy-btn" onclick="feCopy('fe2-code',this)">⧉</button>
</div>
<div class="fe-frame-wrap">
  <iframe id="fe2-frame" class="reframe-off" width="600" height="220"></iframe>
</div>
</div>

## Alpha (α) Sweep

Interactive slider that sweeps the fractional order α — shows how the spectrum rotates from time to frequency domain.

<div class="frft-embeds">
<div class="fe-controls">
  <label>Width</label>
  <input type="number" id="fe3-w" value="700" min="300" step="10">
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
<div class="fe-code-wrap">
  <pre id="fe3-code"></pre>
  <button class="fe-copy-btn" onclick="feCopy('fe3-code',this)">⧉</button>
</div>
<div class="fe-frame-wrap">
  <iframe id="fe3-frame" class="reframe-off" width="700" height="300"></iframe>
</div>
</div>

## Overlap-Add Visualiser

Shows how block-processing artefacts change with different block sizes and overlap factors.

<div class="frft-embeds">
<div class="fe-controls">
  <label>Width</label>
  <input type="number" id="fe4-w" value="700" min="300" step="10">
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
<div class="fe-code-wrap">
  <pre id="fe4-code"></pre>
  <button class="fe-copy-btn" onclick="feCopy('fe4-code',this)">⧉</button>
</div>
<div class="fe-frame-wrap">
  <iframe id="fe4-frame" class="reframe-off" width="700" height="250"></iframe>
</div>
</div>

<script>
(function () {
  const DEMO_BASE  = '/assets/web/frft/demos/';
  const EMBED_BASE = 'https://behzadhaki.com/assets/web/frft/demos/';

  function g(id) { return document.getElementById(id); }

  function buildCode(file, params, w, h) {
    const src = EMBED_BASE + file + '?' + params;
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
    const w = Math.max(300, parseInt(g('fe3-w').value) || 700);
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
    const w = Math.max(300, parseInt(g('fe4-w').value) || 700);
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
})();
</script>
