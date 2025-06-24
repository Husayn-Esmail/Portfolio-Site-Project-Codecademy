// const footer = document.createElement('footer');
// footer.className = "footer";
// const footer_div = document.createElement('div');

// footer.appendChild(div);
// document.getElementsByTagName('body').appendAfter = footer;

const footer = document.createElement("footer");
footer.className = "footer";
const div = document.createElement('div')
const p1 = document.createElement('p')
p1.textContent = "Copyright 2024";
const p2 = document.createElement('p')
p2.textContent = "Husayn Esmail";
div.className = "foot-content-container";
div.appendChild(p1);
div.appendChild(p2);
footer.appendChild(div)
document.getElementsByClassName('content')[0].append(footer)

