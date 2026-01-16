AOS.init();

const toggle = document.getElementById("themeToggle");
const body = document.body;

toggle.onclick = () => {
  body.classList.toggle("bg-slate-900");
  body.classList.toggle("bg-white");
  body.classList.toggle("text-black");
};
