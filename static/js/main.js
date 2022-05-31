// debated creating the secondary nav with js as well. 
// let secondary_nav = ['Python', 'C', 'Swift', 'HTML/CSS'];


const nav = document.getElementById('secondary').firstElementChild;
for (let i = 0; i < nav.children.length; i++) {
    // the elements within seocondary navigation
    console.log(nav.children[i].innerHTML);
    let div = document.createElement('div'); // creates a div to contain each image carousel
    let newNode = document.createElement('h2'); // creates the title element for the section 
    newNode.innerHTML = nav.children[i].innerHTML; // populates the title element 
    div.appendChild(newNode); // adds the title to the div
    document.body.appendChild(div); // inserts the div in the body
}
