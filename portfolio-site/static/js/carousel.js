// debated creating the secondary nav with js as well. 
// let secondary_nav = ['Python', 'C', 'Swift', 'HTML/CSS'];


// const new_images = images.json();
console.log(images);
console.log(things);

// function myFunc(vars) {
//     console.log(vars);
//     let x = document.createElement('p');
//     x.innerHTML = vars;
//     document.body.appendChild(x);
//     return vars;
// }

// class ProjectShowcase {
//     constructor(prog_language) {
//         // this._name = name;
//         this._prog_language = prog_language;
//         this._images = [];
//         this._description = "";
//     }

//     // get name() {
//     //     return this._name;
//     // }

//     get prog_language() {
//         return this._prog_language;
//     }
    
//     get images() {
//         return this._images;
//     }

//     get description() {
//         return this._description;
//     }

//     set images(list_of_images) {
//         this._images = list_of_images;
//     }

//     set description(text) {
//         this._description = text;
//     }

//     addImageToList(image) {
//         this._images.push(image);
//     }

//     displayHeading(div) {
//         let newHeading = document.createElement('h2');
//         newHeading.innerHTML = this.prog_language;
//         div.appendChild(newHeading)
//     }

//     displayImages(div) {
//         let subdiv = document.createElement('div');
//         for (let i = 0; i < this._images.length; i++) {
//             let newImage = document.createElement('img');
//             newImage.src = this._images[i];
//             subdiv.appendChild(newImage);
//             div.appendChild(subdiv); // add subdiv to parent div
//         }
//     }

//     #populateNavButton(button, content, div) {
//         // FIXME: returns the same list of images every time.
//         button.innerHTML = content;
//         button.className = "nav-button";
//         // let img = document.createElement('img');
//         let i = Math.floor(Math.random() * this.images.length);
//         // img.src = images[i];
//         console.log(i);
//         button.addEventListener('click', (event) => {
//             if (i === this.images.length){
//                 i = 0;
//             }
//             console.log(this.images[i++]);
//             // img.src = images[i++];
//         });
//         // div.appendChild(img);
//     }
//     createNavButtons(div) {
//         let left = document.createElement('p');
//         let right = document.createElement('p');
//         this.#populateNavButton(left, '<', div);
//         this.#populateNavButton(right, '>', div);
//         div.appendChild(left);
//         div.appendChild(right);
//     }
// }

// const nav = document.getElementById('secondary').firstElementChild;
// for (let i = 0; i < nav.children.length; i++) {
//     // the elements within secondary navigation
//     const language = nav.children[i].innerText;
//     let div = document.createElement('div'); // creates a div to contain each image carousel
//     showcase = new ProjectShowcase(language);
//     // FIXME: Need to pass image path so we can render images
//     // FIXME: returns the same list of images every time.
//     for (key in images) {
//         if (key.toLowerCase === language.toLowerCase) {
//             showcase.images = images[key];
//             break
//         }
//     }
//     showcase.displayHeading(div);
//     console.log(showcase);
//     showcase.createNavButtons(div);

//     document.body.appendChild(div); // inserts the div in the body
// }

/*
On navigation, depending on what button was clicked, the structure
of images within the ProjectShowcase objects should also be a
double linked list so that they know whether there is the ability
to go forwards or backwards. upon knowing that the head or tail is
null, the backward/forward buttons (respectively) should disappear.
*/

// let y = document.createElement('p');
// y.innerHTML = images;
// document.body.appendChild(y);


class Project {
    constructor(name, images) {
        this.__name = name;
        this.__images = images;
        this.__description = "";
    }

    get name() {
        return this.__name;
    }

    get images() {
        return this.__images;
    }

    get description() {
        return this.__images;
    }

    set setName(newName) {
        this.__name = newName;
    }

    set setImages(images) {
        this.__images = images;
    }

    set setDescription(newDescription) {
        this.__description = newDescription;
    }
}

class Technology {
    constructor(prog_language) {
        this.__prog_language = prog_language;
        this.__projects = [];
    }

    get prog_language() {
        return this.__prog_language;
    }

    get projects() {
        return this.__projects;
    }

    set set_prog_language(new_prog_language) {
        this.__prog_language = new_prog_language;
    }
}

module.exports = { Project, Technology }