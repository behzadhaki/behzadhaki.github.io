// Must run in <head> to prevent flash of wrong theme.
// Dark mode is the compiled-CSS default (no data-theme attribute).
// Light mode is activated by setting data-theme="light".

let toggleTheme = (theme) => {
  setTheme(theme === "light" ? "dark" : "light");
};

let setTheme = (theme) => {
  transTheme();
  setHighlight(theme);
  if (theme === "light") {
    document.documentElement.setAttribute("data-theme", "light");
  } else {
    document.documentElement.removeAttribute("data-theme");
  }
  localStorage.setItem("theme", theme === "light" ? "light" : "dark");
};

let setHighlight = (theme) => {
  var light = document.getElementById("highlight_theme_light");
  var dark  = document.getElementById("highlight_theme_dark");
  if (!light || !dark) return;
  if (theme === "light") {
    light.media = "";
    dark.media  = "none";
  } else {
    dark.media  = "";
    light.media = "none";
  }
};

let transTheme = () => {
  document.documentElement.classList.add("transition");
  window.setTimeout(() => {
    document.documentElement.classList.remove("transition");
  }, 400);
};

let initTheme = (stored) => {
  if (stored === "light") {
    setTheme("light");
  } else if (!stored || stored === "null") {
    // No stored preference — respect system setting, default to dark otherwise
    var preferLight = window.matchMedia && window.matchMedia("(prefers-color-scheme: light)").matches;
    setTheme(preferLight ? "light" : "dark");
  } else {
    setTheme("dark");
  }
};

initTheme(localStorage.getItem("theme"));
