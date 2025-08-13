const home_link = document.getElementById('home_link');
const bootcamp_link = document.getElementById('bootcamp_link');
const home_section = document.getElementById('home_section');
const bootcamp_section = document.getElementById('bootcamp_section');
const subir_feedback = document.getElementById("subir_feedback");

home_link.addEventListener('click', e => {
  e.preventDefault();
  home_section.style.display = 'block';
  bootcamp_section.style.display = 'none';
});

bootcamp_link.addEventListener('click', e => {
  e.preventDefault();
  home_section.style.display = 'none';
  bootcamp_section.style.display = 'block';
});

const aggBtn = document.getElementById('agg_btn');
const aggContenido = document.querySelector('.agg_contenido');
const aggWrapper = document.querySelector('.agg_wraper');

// Ocultar por defecto
aggContenido.style.display = 'none';

// Mostrar/ocultar al hacer clic en el botón
aggBtn.addEventListener('click', (e) => {
    e.stopPropagation(); // Evita que el click se propague al document
    const visible = aggContenido.style.display === 'block';
    aggContenido.style.display = visible ? 'none' : 'block';
});

// Cerrar al hacer clic fuera
document.addEventListener('click', (e) => {
    if (!aggWrapper.contains(e.target)) {
        aggContenido.style.display = 'none';
    }
});






