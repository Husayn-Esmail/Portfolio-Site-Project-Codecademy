// debated creating the secondary nav with js as well. 
// let secondary_nav = ['Python', 'C', 'Swift', 'HTML/CSS'];



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

    set name(newName) {
        this.__name = newName;
    }

    set images(images) {
        this.__images = images;
    }

    set description(newDescription) {
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

    set prog_language(new_prog_language) {
        this.__prog_language = new_prog_language;
    }

    set projects(new_projects) {
        this.__projects = new_projects;
    }

    add_project(new_project) {
        this.__projects.push(new_project);
    }
}

class DisplayTechnology {
    // pass
    constructor(technologyObject, pathToImages) {        
        this.technology = technologyObject;
        this.path = pathToImages;
        this.projects = technologyObject.projects;
    }

    get technology() {
        return this.technology;
    }

    set technology(new_technology) {
        this.technology = new_technology;
    }

    displayHeading(div) {
        /**
         * accepts a div as an argument.
         * appends a heading (based on the programming language specified in
         * the technology) to the div passed. returns null
         */
        let newHeading = document.createElement('h2');
        newHeading.innerHTML = this.technology.prog_language;
        // need to set css classes or ids
        newHeading.id = this.technology.prog_language;
        // add newHeading to div
        div.appendChild(newHeading);
        return null
    }

    createSubheadingElement(project) {
        /**
         * Accepts a Project object as input.
         * returns a subheading element for said project which can then be
         * added to the dom when necessary.
         */
        const subheading = document.createElement('h3');
        subheading.innerHTML = this.project.name;
        subheading.className = 'project-subheading';
        return subheading;
    }

    createImageElements(project) {
        /**
         * Iterates through a projects images and creates an element for each
         * one with a class of project-image.
         * returns a div containing image elements.
         */
        let subdiv = document.createElement('div');
        subdiv.className = 'images';
        const images = project.images;
        const project_name = project.name;
        // iterate through images and create img elements
        for (image_name in images) {
            new_img = document.createElement('img');
            image_path = `${this.path}/${project_name}/${image_name}`;
            new_img.src = image_path;
            new_img.className = 'project-image';
            subdiv.appendChild(new_img);
        }
    }

    // create a function that processes the projects in this technology.
    // Call helper functions to display/get the resources to display such
    // elements.
}


function parseItemsInList(listToBeParsed) {
    let parsed_projects = [];

    for (let i = 0; i < listToBeParsed.length; i++) {
        parsed_projects.push(JSON.parse(listToBeParsed[i]));
    }

    return parsed_projects;
}

function pyObjectToJsObject(parsed_projects) {
    let technologies = [];

    // convert python objects provided by server into Technology and Project
    // Objects
    for (let i = 0; i < parsed_projects.length; i++) {
        const prog_lang = parsed_projects[i]._ProjectsTechnology__prog_language;
        const obj_projects = parsed_projects[i]._ProjectsTechnology__projects;
        const newTech = new Technology(prog_lang);
        // iterate through projects and create Project objects
        for (let j = 0; j < obj_projects.length; j++) {
            const proj_name = obj_projects[j]._Project__name;
            const proj_images = obj_projects[j]._Project__images;
            const proj_desc = obj_projects[j]._Project__description;
            const proj_obj = new Project(proj_name, proj_images);
            proj_obj.description = proj_desc;
            newTech.add_project(proj_obj);
        }
        technologies.push(newTech);
    }
    console.log(technologies);
    return technologies;
}

let parsed_objects = parseItemsInList(projects_from_server)
let technologies = pyObjectToJsObject(parsed_objects)
// export { Project, Technology };