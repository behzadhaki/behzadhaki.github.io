<style>
.byo-download-btn {
  display:inline-flex; align-items:center; gap:7px;
  padding:8px 18px;
  background:transparent; color:rgba(255,255,255,0.65);
  border:1px solid rgba(255,255,255,0.22);
  border-radius:7px; font-size:13px; font-weight:500; cursor:pointer;
  transition:background 0.15s, border-color 0.15s;
  margin-bottom:1.4rem;
}
.byo-download-btn:hover:not(:disabled) {
  background:rgba(255,255,255,0.1); border-color:rgba(255,255,255,0.38);
}
.byo-download-btn:disabled { opacity:0.5; cursor:default; }
html[data-theme='light'] .byo-download-btn {
  color:rgba(0,0,0,0.6); border-color:rgba(0,0,0,0.22);
}
html[data-theme='light'] .byo-download-btn:hover:not(:disabled) {
  background:rgba(0,0,0,0.07); border-color:rgba(0,0,0,0.38);
}
</style>

## Resources

The engine is written in C++ and compiled to WebAssembly. All usage examples and widgets are in plain JavaScript — no framework or bundler required.

<button class="byo-download-btn" id="byoDownloadBtn">⬇ Download FRFT engine files</button>

Three files are included in the ZIP:

| File | Size | Role |
|---|---|---|
| `wasm/dist/frft.js` | 45 KB | JS glue — loads and wraps the WASM module |
| `wasm/dist/frft.wasm` | 45 KB | Compiled FRFT engine |
| `audio/frft-worker.js` | 13 KB | Web Worker — runs processing off the main thread |

## Using the worker (recommended)

The worker keeps heavy computation off the UI thread. Drop the three files into your project and preserve their relative paths — `frft-worker.js` expects `../wasm/dist/frft.js` alongside it.

```js
// 1. Start the worker
const worker = new Worker('audio/frft-worker.js');

// 2. Load the WASM engine
worker.postMessage({
  type: 'init',
  jsUrl:       new URL('wasm/dist/frft.js', location.href).href,
  wasmBaseUrl: new URL('wasm/dist/', location.href).href,
});

// 3. Wait for ready, then process
worker.onmessage = ({ data }) => {
  if (data.type === 'ready') {
    worker.postMessage({
      type: 'process',
      samples:      myFloat32Array,   // mono audio samples
      alpha:        0.5,              // fractional order (0–4)
      bufSize:      16384,            // block size
      overlapFactor: 4,               // overlap (1, 2, 4, 8 …)
      halfSpectrum: false,
      jobId:        1,
    });
  }
  if (data.type === 'result') {
    const output = data.output;       // Float32Array — FRFT of the input
  }
  if (data.type === 'progress') {
    console.log('progress:', data.value); // 0..1
  }
};

// Cancel a running job at any time
worker.postMessage({ type: 'cancel' });
```

## Using the WASM module directly

For offline or non-audio use, load the module directly on the main thread:

```js
import FRFTModule from './wasm/dist/frft.js';

const Module = await FRFTModule();
const proc   = new Module.FRFTProcessor();

proc.prepare(512);

// Write input into WASM memory (zero-copy)
const inR = new Float64Array(Module.HEAPF64.buffer, proc.inputRealPtr(), 512);
inR.set(mySamples);

// Run FRFT
proc.process(512, /* alpha */ 0.5);

// Read result
const outR = new Float64Array(Module.HEAPF64.buffer, proc.outputRealPtr(), 512);
```

Or use the convenience wrapper (allocates internally):

```js
const result = proc.processArrays(realIn, imagIn, alpha);
// result.real → Float64Array
// result.imag → Float64Array
```

For the full build guide (recompiling from C++, Emscripten setup, AudioWorklet wiring) see [`web/README.md`](https://github.com/behzadhaki/FRFT_Max/blob/main/web/README.md) in the repo.

<script>
(function () {
  const ZIP_FILES = [
    { src: '/assets/web/frft/wasm/dist/frft.js',   dst: 'wasm/dist/frft.js'   },
    { src: '/assets/web/frft/wasm/dist/frft.wasm', dst: 'wasm/dist/frft.wasm' },
    { src: '/assets/web/frft/audio/frft-worker.js',dst: 'audio/frft-worker.js'},
  ];

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

  const btn = document.getElementById('byoDownloadBtn');
  if (btn) {
    btn.addEventListener('click', async function () {
      btn.disabled = true; btn.textContent = 'Fetching…';
      try {
        const entries = await Promise.all(ZIP_FILES.map(async function ({ src, dst }) {
          const res = await fetch(src);
          if (!res.ok) throw new Error(src + ' → HTTP ' + res.status);
          return { name: dst, data: new Uint8Array(await res.arrayBuffer()) };
        }));
        const zip = buildZip(entries);
        const url = URL.createObjectURL(new Blob([zip], { type: 'application/zip' }));
        Object.assign(document.createElement('a'), { href: url, download: 'frft-engine.zip' }).click();
        URL.revokeObjectURL(url);
      } catch (err) {
        alert('Download failed: ' + err.message);
      } finally {
        btn.disabled = false; btn.textContent = '⬇ Download FRFT engine files';
      }
    });
  }
})();
</script>
