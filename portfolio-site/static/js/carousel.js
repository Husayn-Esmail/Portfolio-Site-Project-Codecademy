// debated creating the secondary nav with js as well. 
// let secondary_nav = ['Python', 'C', 'Swift', 'HTML/CSS'];





// function myFunc(vars) {
//     console.log(vars);
//     let x = document.createElement('p');
//     x.innerHTML = vars;
//     document.body.appendChild(x);
//     return vars;
// }

class ProjectShowcase {
    constructor(prog_language) {
        // this._name = name;
        this._prog_language = prog_language;
        this._images = [];
        this._description = "";
    }

    // get name() {
    //     return this._name;
    // }

    get prog_language() {
        return this._prog_language;
    }
    
    get images() {
        return this._images;
    }

    get description() {
        return this._description;
    }

    set images(list_of_images) {
        this._images = list_of_images;
    }

    set description(text) {
        this._description = text;
    }

    addImageToList(image) {
        this._images.push(image);
    }

    displayHeading(div) {
        let newHeading = document.createElement('h2');
        newHeading.innerHTML = this._prog_language;
        div.appendChild(newHeading)
    }

    displayImages() {
        let div = document.createElement('div');
        for (let i = 0; i < this._images.length; i++) {
            let newImage = document.createElement('img');
            newImage.src = this._images[i];
            div.appendChild(newImage);
            document.body.appendChild(div);
        }
    }
}

const nav = document.getElementById('secondary').firstElementChild;
for (let i = 0; i < nav.children.length; i++) {
    // the elements within secondary navigation
    const language = nav.children[i].innerText;
    let div = document.createElement('div'); // creates a div to contain each image carousel
    showcase = new ProjectShowcase(language);
    for (key in images) {
        if (key.toLowerCase === language.toLowerCase) {
            showcase.images = images[key];
            break
        }
    }
    showcase.displayHeading(div)
    console.log(showcase);


    document.body.appendChild(div); // inserts the div in the body
}

/*
On navigation, depending on what button was clicked, the structure
of images within the ProjectShowcase objects should also be a
double linked list so that they know whether there is the ability
to go forwards or backwards. upon knowing that the head or tail is
null, the backward/forward buttons (respectively) should disappear.
*/

let y = document.createElement('p');
y.innerHTML = images;
document.body.appendChild(y);