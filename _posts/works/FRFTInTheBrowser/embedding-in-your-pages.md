
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
.frft-embeds .fe-bottom-row .fe-frame-wrap { flex-shrink:0; margin-top:0; order:1; }
.frft-embeds .fe-bottom-row .fe-code-wrap  { flex:1; min-width:0; margin-top:0; overflow-y:auto; order:2; }

/* ── Mobile: stack code above widget ─────────────────────── */
@media (max-width: 700px) {
  .frft-embeds .fe-bottom-row { flex-direction:column; }
  .frft-embeds .fe-bottom-row .fe-code-wrap  { order:1; }
  .frft-embeds .fe-bottom-row .fe-frame-wrap { order:2; overflow:hidden; }
}

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

Adjust the parameters for each widget below, then click **Apply** to update the live preview and generate a ready-to-paste `<iframe>` embed snippet with those values baked in as defaults.

## FT Spectrum

Shows the magnitude spectrum of the full signal (32768-sample window). Switch between Exact, Hann, and Rect windowing directly inside the embedded widget.

**Exact** snaps the signal frequency to the nearest DFT bin, then computes the spectrum analytically from the known harmonic series of each waveform. The result is mathematically ideal: spikes land at exact bin positions with absolute silence between them — no windowing artefacts, no spectral leakage. **Hann** and **Rect** use the standard FFT path; Hann suppresses leakage at the cost of a wider main lobe, while Rect gives the narrowest peaks but leaks when the frequency falls between bins.

<div class="frft-embeds">
<div class="fe-controls">
  <label>Width</label>
  <input type="number" id="fe7-w" value="600" min="200" step="10">
  <label>Height</label>
  <input type="number" id="fe7-h" value="220" min="100" step="10">
  <label>Waveform</label>
  <select id="fe7-wave">
    <option value="sweep" selected>Freq sweep</option>
    <option value="sine">Sine</option>
    <option value="triangle">Triangle</option>
    <option value="sawtooth">Sawtooth</option>
    <option value="square">Square</option>
  </select>
  <label id="fe7-freq-lbl">Freq (Hz)</label>
  <input type="number" id="fe7-freq" value="440" min="20" max="20000" disabled>
  <label>Win</label>
  <select id="fe7-win">
    <option value="exact" selected>Exact</option>
    <option value="hann">Hann</option>
    <option value="rect">Rectangular</option>
  </select>
  <label>Mode</label>
  <select id="fe7-interactive">
    <option value="1" selected>Interactive</option>
    <option value="0">Static</option>
  </select>
  <button onclick="feApply7()">Apply</button>
</div>
<div class="fe-bottom-row">
<div class="fe-frame-wrap">
  <iframe id="fe7-frame" class="reframe-off" width="600" height="220"></iframe>
</div>
<div class="fe-code-wrap">
  <pre id="fe7-code"></pre>
  <button class="fe-copy-btn" onclick="feCopy('fe7-code',this)">⧉</button>
</div>
</div>
</div>

## Listen to FT Directly

Displays the real part, imaginary part, or magnitude of the Fourier Transform of the selected signal. Hit **Play** to hear what the FT *sounds like*: the selected component is played back as audio while a playhead scrubs left-to-right from −fNyq to +fNyq. The x-axis switches from frequency to time during playback, then reverts when playback stops. A Hann window is always applied.

Switch between **Re**, **Im**, and **Mag** to explore FT structure: for a real signal, Re[FT] is even-symmetric and Im[FT] is odd-symmetric around DC; |FT| is always even. Try a 440 Hz sine — the imaginary part shows two clean spikes, and the audio is a pair of impulses.

<div class="frft-embeds">
<div class="fe-controls">
  <label>Width</label>
  <input type="number" id="fe8-w" value="600" min="200" step="10">
  <label>Height</label>
  <input type="number" id="fe8-h" value="220" min="100" step="10">
  <label>Waveform</label>
  <select id="fe8-wave">
    <option value="sine" selected>Sine</option>
    <option value="triangle">Triangle</option>
    <option value="sawtooth">Sawtooth</option>
    <option value="square">Square</option>
    <option value="sweep">Freq sweep</option>
  </select>
  <label id="fe8-freq-lbl">Freq (Hz)</label>
  <input type="number" id="fe8-freq" value="440" min="20" max="20000">
  <label>Part</label>
  <select id="fe8-part">
    <option value="imag" selected>Imaginary</option>
    <option value="real">Real</option>
  </select>
  <label>Mode</label>
  <select id="fe8-interactive">
    <option value="1" selected>Interactive</option>
    <option value="0">Static</option>
  </select>
  <button onclick="feApply8()">Apply</button>
</div>
<div class="fe-bottom-row">
<div class="fe-frame-wrap">
  <iframe id="fe8-frame" class="reframe-off" width="600" height="220"></iframe>
</div>
<div class="fe-code-wrap">
  <pre id="fe8-code"></pre>
  <button class="fe-copy-btn" onclick="feCopy('fe8-code',this)">⧉</button>
</div>
</div>
</div>

## FRFT Rotation Diagram

Shows the FRFT output at 16 fractional orders simultaneously — four large panels at the cardinal positions (time, frequency, reversed-time, inverse-FT) and twelve small panels at intermediate α values arranged around a circle. Click any play button to hear the output at that order; an arrow in the centre tracks the active position.

<div class="frft-embeds">
<div class="fe-controls">
  <label>Width</label>
  <input type="number" id="fe5-w" value="600" min="200" step="10">
  <label>Waveform</label>
  <select id="fe5-wave">
    <option value="sine" selected>Sine</option>
    <option value="triangle">Triangle</option>
    <option value="sawtooth">Sawtooth</option>
    <option value="square">Square</option>
    <option value="sweep">Freq sweep</option>
  </select>
  <label id="fe5-freq-lbl">Freq (Hz)</label>
  <input type="number" id="fe5-freq" value="440" min="20" max="20000">
  <label>Win</label>
  <select id="fe5-win">
    <option value="hann" selected>Hann</option>
    <option value="rect">Rectangular</option>
  </select>
  <label>View</label>
  <select id="fe5-disp">
    <option value="wave" selected>Waveform</option>
    <option value="scope">Spectrogram</option>
  </select>
  <label>Δα</label>
  <select id="fe5-dalpha">
    <option value="0.333">1/3</option>
    <option value="0.25">1/4</option>
    <option value="0.5">1/2</option>
    <option value="1">1</option>
    <option value="2">2</option>
    <option value="dft">DFT</option>
  </select>
  <label>Mode</label>
  <select id="fe5-interactive">
    <option value="1" selected>Interactive</option>
    <option value="0">Static</option>
  </select>
  <button onclick="feApply5()">Apply</button>
</div>
<div class="fe-bottom-row">
<div class="fe-frame-wrap">
  <iframe id="fe5-frame" class="reframe-off" width="600" height="600"></iframe>
</div>
<div class="fe-code-wrap">
  <pre id="fe5-code"></pre>
  <button class="fe-copy-btn" onclick="feCopy('fe5-code',this)">⧉</button>
</div>
</div>
</div>

## FRFT Index Additivity

Demonstrates that FRFT(α₂) ∘ FRFT(α₁) = FRFT(α₁+α₂). The widget shows all four stages — input, intermediate (after α₁), sequential output (after α₂), and direct output (α₁+α₂) — and draws a dashed green equality line between the two outputs once computation completes. Click any panel to hear the audio at that stage.

<div class="frft-embeds">
<div class="fe-controls">
  <label>Width</label>
  <input type="number" id="fe6-w" value="600" min="200" step="10">
  <label>Height</label>
  <input type="number" id="fe6-h" value="400" min="200" step="10">
  <label>Waveform</label>
  <select id="fe6-wave">
    <option value="sine" selected>Sine</option>
    <option value="triangle">Triangle</option>
    <option value="sawtooth">Sawtooth</option>
    <option value="square">Square</option>
    <option value="sweep">Freq sweep</option>
  </select>
  <label id="fe6-freq-lbl">Freq (Hz)</label>
  <input type="number" id="fe6-freq" value="440" min="20" max="20000">
  <label>Win</label>
  <select id="fe6-win">
    <option value="hann" selected>Hann</option>
    <option value="rect">Rectangular</option>
  </select>
  <label>View</label>
  <select id="fe6-disp">
    <option value="wave" selected>Waveform</option>
    <option value="scope">Spectrogram</option>
  </select>
  <label>Demo</label>
  <select id="fe6-demo">
    <option value="additivity" selected>Additivity</option>
    <option value="inversion">Inversion</option>
  </select>
  <label id="fe6-a1-lbl">&alpha;&#x2081;</label>
  <input type="number" id="fe6-a1" value="0.5" min="-4" max="4" step="0.05" style="width:52px">
  <label id="fe6-a2-lbl">&alpha;&#x2082;</label>
  <input type="number" id="fe6-a2" value="0.75" min="-4" max="4" step="0.05" style="width:52px">
  <label>Mode</label>
  <select id="fe6-interactive">
    <option value="1" selected>Interactive</option>
    <option value="0">Static</option>
  </select>
  <button onclick="feApply6()">Apply</button>
</div>
<div class="fe-bottom-row">
<div class="fe-frame-wrap">
  <iframe id="fe6-frame" class="reframe-off" width="600" height="400"></iframe>
</div>
<div class="fe-code-wrap">
  <pre id="fe6-code"></pre>
  <button class="fe-copy-btn" onclick="feCopy('fe6-code',this)">⧉</button>
</div>
</div>
</div>

## Interactive FRFT

Full controls — let visitors change signal type, α order, block size and overlap directly in the widget. To pre-load your own audio file, add `url=` pointing to any same-origin path, e.g. `url=/assets/audio/my-file.mp3`. The widget fetches and decodes it automatically on load, and the file picker is hidden.

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
    <option value="triangle">Triangle</option>
    <option value="sawtooth">Sawtooth</option>
    <option value="square">Square</option>
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

Fixed parameters set at embed time — auto-plays on load, no controls shown to the visitor. To use your own audio file, add `url=` pointing to any same-origin path, e.g. `url=/assets/audio/my-file.mp3`. The file is fetched and decoded automatically — no file picker needed.

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
    <option value="triangle">Triangle</option>
    <option value="sawtooth">Sawtooth</option>
    <option value="square">Square</option>
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
  <label>Waveform</label>
  <select id="fe3-wave">
    <option value="sine" selected>Sine</option>
    <option value="triangle">Triangle</option>
    <option value="sawtooth">Sawtooth</option>
    <option value="square">Square</option>
  </select>
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
  <label>Waveform</label>
  <select id="fe4-wave">
    <option value="sine" selected>Sine</option>
    <option value="triangle">Triangle</option>
    <option value="sawtooth">Sawtooth</option>
    <option value="square">Square</option>
  </select>
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
  <label>Window</label>
  <select id="fe4-win">
    <option value="hann" selected>Hann</option>
    <option value="rect">Rectangular</option>
  </select>
  <label>Lock example</label>
  <select id="fe4-lock">
    <option value="0" selected>No</option>
    <option value="1">Yes</option>
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
    return '<div style="width:100%; max-width:' + w + 'px; background:#1a1a1a; border-radius:8px; overflow:hidden;">\n' +
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
    rescaleFrames();
  }

  function rescaleFrames() {
    document.querySelectorAll('.frft-embeds .fe-frame-wrap').forEach(function(wrap) {
      const iframe = wrap.querySelector('iframe');
      if (!iframe) return;
      const embed = wrap.closest('.frft-embeds');
      const controls = embed && embed.querySelector('.fe-controls');
      const available = controls ? controls.offsetWidth : (embed ? embed.clientWidth : 0);
      const iw = parseInt(iframe.getAttribute('width')) || 600;
      const ih = parseInt(iframe.getAttribute('height')) || 300;
      if (available > 0 && available < iw) {
        const scale = available / iw;
        iframe.style.transform = 'scale(' + scale + ')';
        iframe.style.transformOrigin = 'top left';
        wrap.style.width  = Math.round(iw  * scale) + 'px';
        wrap.style.height = Math.round(ih  * scale) + 'px';
      } else {
        iframe.style.transform = '';
        wrap.style.width  = '';
        wrap.style.height = '';
      }
    });
  }
  window.addEventListener('resize', rescaleFrames);

  window.feCopy = function(codeId, btn) {
    navigator.clipboard.writeText(g(codeId).textContent).then(() => {
      btn.textContent = '✓'; btn.classList.add('copied');
      setTimeout(() => { btn.textContent = '⧉'; btn.classList.remove('copied'); }, 1800);
    });
  };

  /* ── 8. Listen to FT Directly ──────────────────────────── */
  window.feApply8 = function () {
    const w = Math.max(200, parseInt(g('fe8-w').value) || 600);
    const h = Math.max(100, parseInt(g('fe8-h').value) || 220);
    g('fe8-w').value = w; g('fe8-h').value = h;
    const wave = g('fe8-wave').value;
    const hasFreq = wave !== 'sweep';
    g('fe8-freq').disabled = !hasFreq;
    g('fe8-freq-lbl').style.opacity = hasFreq ? '1' : '0.4';
    const interactive = g('fe8-interactive').value;
    const p = new URLSearchParams({ w, h, type: wave, part: g('fe8-part').value });
    if (hasFreq) p.set('freq', g('fe8-freq').value);
    if (interactive === '0') p.set('interactive', '0');
    g('fe8-code').textContent = buildCode('embed_ft_listen.html', p.toString(), w, h);
    loadFrame('fe8-frame', 'embed_ft_listen.html', p.toString(), w, h);
  };
  g('fe8-wave').addEventListener('change', feApply8);
  g('fe8-part').addEventListener('change', feApply8);
  g('fe8-interactive').addEventListener('change', feApply8);
  feApply8();

  /* ── 7. FT Spectrum ─────────────────────────────────────── */
  window.feApply7 = function () {
    const w = Math.max(200, parseInt(g('fe7-w').value) || 600);
    const h = Math.max(100, parseInt(g('fe7-h').value) || 220);
    g('fe7-w').value = w; g('fe7-h').value = h;
    const wave = g('fe7-wave').value;
    const hasFreq = wave !== 'sweep';
    g('fe7-freq').disabled = !hasFreq;
    g('fe7-freq-lbl').style.opacity = hasFreq ? '1' : '0.4';
    const interactive = g('fe7-interactive').value;
    const p = new URLSearchParams({ w, h, type: wave, win: g('fe7-win').value });
    if (hasFreq) p.set('freq', g('fe7-freq').value);
    if (interactive === '0') p.set('interactive', '0');
    g('fe7-code').textContent = buildCode('embed_fft_spectrum.html', p.toString(), w, h);
    loadFrame('fe7-frame', 'embed_fft_spectrum.html', p.toString(), w, h);
  };
  g('fe7-wave').addEventListener('change', feApply7);
  g('fe7-win').addEventListener('change', feApply7);
  g('fe7-interactive').addEventListener('change', feApply7);
  feApply7();

  /* ── 5. Rotation diagram ────────────────────────────────── */
  window.feApply5 = function () {
    const w = Math.max(200, parseInt(g('fe5-w').value) || 600);
    g('fe5-w').value = w;
    const dalpha     = g('fe5-dalpha').value;
    const interactive = g('fe5-interactive').value;
    const isStatic   = interactive === '0';
    // Auto-height: delta=2 → only left/right panels, crop empty top/bottom bands
    // Widget uses width as size reference for delta=2, so vertical extent ≈ 0.42w
    const ratio = parseFloat(dalpha) >= 2 ? 0.42 : 1.0;
    const h = Math.round(w * ratio) + (isStatic ? 30 : 0);
    const wave = g('fe5-wave').value;
    const hasFreq = wave !== 'sweep';
    g('fe5-wave').disabled = false;
    g('fe5-freq').disabled = !hasFreq;
    g('fe5-freq-lbl').style.opacity = hasFreq ? '1' : '0.4';
    const p = new URLSearchParams({ w, h, wave, disp: g('fe5-disp').value,
                                    dalpha, win: g('fe5-win').value });
    if (hasFreq) p.set('freq', g('fe5-freq').value);
    if (isStatic) p.set('interactive', '0');
    g('fe5-code').textContent = buildCode('embed_frft_rotation.html', p.toString(), w, h);
    loadFrame('fe5-frame', 'embed_frft_rotation.html', p.toString(), w, h);
  };
  g('fe5-wave').addEventListener('change', feApply5);
  g('fe5-win').addEventListener('change', feApply5);
  g('fe5-disp').addEventListener('change', feApply5);
  g('fe5-dalpha').addEventListener('change', feApply5);
  g('fe5-interactive').addEventListener('change', feApply5);
  feApply5();

  /* ── 6. Index Additivity ─────────────────────────────────── */
  function fe6SyncInversion() {
    const isInversion = g('fe6-demo').value === 'inversion';
    const a2el = g('fe6-a2');
    if (isInversion) {
      a2el.value = (-parseFloat(g('fe6-a1').value || 0)).toString();
      a2el.disabled = true;
      a2el.style.opacity = '0.5';
      g('fe6-a1-lbl').textContent = 'α';
      g('fe6-a2-lbl').textContent = '−α';
    } else {
      a2el.disabled = false;
      a2el.style.opacity = '1';
      g('fe6-a1-lbl').innerHTML = '&alpha;&#x2081;';
      g('fe6-a2-lbl').innerHTML = '&alpha;&#x2082;';
    }
  }
  window.feApply6 = function () {
    fe6SyncInversion();
    const w = Math.max(200, parseInt(g('fe6-w').value) || 750);
    const h = Math.max(200, parseInt(g('fe6-h').value) || 400);
    g('fe6-w').value = w;
    g('fe6-h').value = h;
    const interactive = g('fe6-interactive').value;
    const isStatic    = interactive === '0';
    const wave    = g('fe6-wave').value;
    const hasFreq = wave !== 'sweep';
    g('fe6-wave').disabled = false;
    g('fe6-freq').disabled = !hasFreq;
    g('fe6-freq-lbl').style.opacity = hasFreq ? '1' : '0.4';
    const isInversion = g('fe6-demo').value === 'inversion';
    const p = new URLSearchParams({
      w, h, wave, disp: g('fe6-disp').value,
      win: g('fe6-win').value,
      alpha1: g('fe6-a1').value,
      alpha2: g('fe6-a2').value,
    });
    if (hasFreq) p.set('freq', g('fe6-freq').value);
    if (isStatic) p.set('interactive', '0');
    if (isInversion) p.set('inversion', '1');
    g('fe6-code').textContent = buildCode('embed_frft_additivity.html', p.toString(), w, h);
    loadFrame('fe6-frame', 'embed_frft_additivity.html', p.toString(), w, h);
  };
  g('fe6-demo').addEventListener('change', feApply6);
  g('fe6-a1').addEventListener('change', feApply6);
  g('fe6-a1').addEventListener('input', function () {
    if (g('fe6-demo').value === 'inversion') {
      g('fe6-a2').value = (-parseFloat(this.value || 0)).toString();
    }
  });
  g('fe6-wave').addEventListener('change', feApply6);
  g('fe6-win').addEventListener('change', feApply6);
  g('fe6-disp').addEventListener('change', feApply6);
  g('fe6-interactive').addEventListener('change', feApply6);
  feApply6();

  /* ── 1. Interactive ──────────────────────────────────────── */
  window.feApply1 = function () {
    const w = Math.max(200, parseInt(g('fe1-w').value) || 600);
    const h = Math.max(100, parseInt(g('fe1-h').value) || 220);
    g('fe1-w').value = w; g('fe1-h').value = h;
    const p = new URLSearchParams({ w, h });
    const type = g('fe1-type').value;
    if (type) p.set('type', type);
    const hasFreq = type === 'sine' || type === 'triangle' || type === 'sawtooth' || type === 'square';
    if (hasFreq) p.set('freq', g('fe1-freq').value);
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
    g('fe1-freq').disabled = !hasFreq;
    g('fe1-freq-lbl').style.opacity = hasFreq ? '1' : '0.4';
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
    const hasFreq = type === 'sine' || type === 'triangle' || type === 'sawtooth' || type === 'square';
    g('fe2-freq').disabled = !hasFreq;
    g('fe2-freq-lbl').style.opacity = hasFreq ? '1' : '0.4';
    const p = new URLSearchParams({ w, h,
      type, dur: g('fe2-dur').value, alpha: g('fe2-alpha').value,
      blocksize: block, overlap: isAll ? '1' : g('fe2-overlap').value,
      halfspec: g('fe2-halfspec').value,
    });
    if (hasFreq) p.set('freq', g('fe2-freq').value);
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
      wave: g('fe3-wave').value, win: g('fe3-win').value,
      halfspec: g('fe3-halfspec').value,
      freqidx: g('fe3-freqidx').value, alpha: g('fe3-alpha').value,
    });
    g('fe3-code').textContent = buildCode('embed_alpha_sweep_frft.html', p.toString(), w, h);
    loadFrame('fe3-frame', 'embed_alpha_sweep_frft.html', p.toString(), w, h);
  };
  g('fe3-wave').addEventListener('change', feApply3);
  feApply3();

  /* ── 4. OLA ──────────────────────────────────────────────── */
  window.feApply4 = function () {
    const w = Math.max(300, parseInt(g('fe4-w').value) || 600);
    const h = Math.max(200, parseInt(g('fe4-h').value) || 250);
    g('fe4-w').value = w; g('fe4-h').value = h;
    const p = new URLSearchParams({ w, h,
      wave: g('fe4-wave').value, freq: g('fe4-freq').value,
      alpha: g('fe4-alpha').value, blocksize: g('fe4-block').value,
      overlap: g('fe4-overlap').value, halfspec: g('fe4-halfspec').value,
      win: g('fe4-win').value,
    });
    if (g('fe4-lock').value === '1') p.set('lock', '1');
    g('fe4-code').textContent = buildCode('embed_ola_frft.html', p.toString(), w, h);
    loadFrame('fe4-frame', 'embed_ola_frft.html', p.toString(), w, h);
  };
  g('fe4-wave').addEventListener('change', feApply4);
  g('fe4-block').addEventListener('change', feApply4);
  g('fe4-overlap').addEventListener('change', feApply4);
  g('fe4-halfspec').addEventListener('change', feApply4);
  g('fe4-win').addEventListener('change', feApply4);
  g('fe4-lock').addEventListener('change', feApply4);
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
    feApply8(); feApply7(); feApply5(); feApply6(); feApply1(); feApply2(); feApply3(); feApply4();
  });
  syncHostUI();

  /* ── ZIP download ────────────────────────────────────────────────────── */
  const ZIP_FILES = [
    { src:'/assets/web/frft/demos/embed_ft_listen.html',             dst:'web/frft/demos/embed_ft_listen.html' },
    { src:'/assets/web/frft/demos/embed_fft_spectrum.html',          dst:'web/frft/demos/embed_fft_spectrum.html' },
    { src:'/assets/web/frft/demos/embed_frft_rotation.html',         dst:'web/frft/demos/embed_frft_rotation.html' },
    { src:'/assets/web/frft/demos/embed_frft_additivity.html',       dst:'web/frft/demos/embed_frft_additivity.html' },
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
