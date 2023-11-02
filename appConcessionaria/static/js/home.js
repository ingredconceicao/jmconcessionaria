// let procura = document.querySelector('.caixa-procura');

// document.querySelector('#procura-icone').onclick = () => {
//     procura.classList.toggle('active');
// }

// function alerta(){
//     alert('Bem vindooo')
// }

let header = document.querySelector('header');

window.addEventListener('scroll' , () => {
    header.classList.toggle('shadow', window.scrollY > 0);
});