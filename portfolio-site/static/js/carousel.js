// debated creating the secondary nav with js as well. 
// let secondary_nav = ['Python', 'C', 'Swift', 'HTML/CSS'];

class ProjectShowcase {
    constructor(name, prog_language) {
        this._name = name;
        this._prog_language = prog_language;
        this._images = [];
        this._description = "";
    }

    get name() {
        return this._name;
    }

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

    displayHeading() {
        let div = document.createElement('div');
        let newNode = document.createElement('h2');
        newNode.innerHTML = this._name;
        div.appendChild(newNode)
    }

    displayImages() {
        let div = document.createElement('div');
        for (let i = 0; i < this._images.length; i++) {
            let newImage = document.createElement('img');
            newImage.src = this._images[i];
            div.appendChild(newImage);
        }
    }
}



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

