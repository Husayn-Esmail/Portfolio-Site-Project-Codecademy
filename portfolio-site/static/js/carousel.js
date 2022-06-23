// debated creating the secondary nav with js as well. 
// let secondary_nav = ['Python', 'C', 'Swift', 'HTML/CSS'];

class Project {
    constructor(name, images) {
        this.__name = name;
        this.__images = images;
        this.__description = "";
        this.__path = "";
    }

    get name() {
        return this.__name;
    }

    get images() {
        return this.__images;
    }

    get description() {
        return this.__description;
    }

    get path() {
        return this.__path;
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

    set path(newPath) {
        this.__path = newPath; 
    }

    getImagePaths() {
        let paths = [];
        for (let image in this.images) {
            const img_path = `${this.path}/${this.name}`;
            paths.push(img_path);
        }
        return paths;
    }

    // TODO: Set the path later on in the functions
    // TODO: refactor functions to use the new Project Object
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
    constructor(technologyObject, pathToImages) {        
        this._technology = technologyObject;
        this.path = pathToImages;
        this._projects = technologyObject.projects;
        this.images = [];
    }

    get technology() {
        return this._technology;
    }

    get projects() {
        return this._projects;
    }

    set technology(new_technology) {
        this._technology = new_technology;
    }

    displayHeading(div) {
        /**
         * accepts a div as an argument.
         * appends a heading (based on the programming language specified in
         * the technology) to the div passed. returns null
         */
        let newHeading = document.createElement('h2');
        newHeading.innerHTML = this._technology.prog_language;
        // need to set css classes or ids
        newHeading.id = this._technology.prog_language;
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
        subheading.innerHTML = project.name;
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
        for (let i = 0; i < images.length; i++) {
            const new_img = document.createElement('img');
            const image_path = `${this.path}/${project_name}/${images[i]}`;
            new_img.src = image_path;
            new_img.classList.add('project-image');
            new_img.classList.add("hide");
            subdiv.appendChild(new_img);
        }
        return subdiv;
    }

    createDescriptionElement(project) {
        const subdiv = document.createElement('div');
        const proj_description = project.description;
        const new_p = document.createElement('p');
        new_p.className = 'project-description';
        new_p.innerText = proj_description;
        subdiv.appendChild(new_p);
        return subdiv;
    }

    populateNavButton(button, content) {
        // sets the button symbol, a class and a click event.
        button.innerHTML = content;
        button.className = "nav-button";
        // click event needs to change.
        button.addEventListener('click', (event) => {
            // pass
        });
        return null;
    }

    displayNavButtons(div) {
        let left = document.createElement('p');
        let right = document.createElement('p');
        this.populateNavButton(left, '<', div);
        this.populateNavButton(right, '>', div);
        div.appendChild(left);
        div.appendChild(right);
    }

    // create a function that processes the projects in this technology.
    // Call helper functions to display/get the resources to display such
    // elements.
    displayProjects(projects, div) {
        for (let i = 0; i < projects.length; i++) {
            const project = projects[i];
            const subheading = this.createSubheadingElement(project);
            const nav_img_div = document.createElement("div");
            const img_elements = this.createImageElements(project);
            const proj_name = project.name;
            const newObj = {[proj_name]: img_elements};
            this.images.push(newObj);
            // removes hide class because all images hidden upon instantiation
            img_elements.firstChild.classList.remove("hide");
            nav_img_div.appendChild(img_elements);    
            this.displayNavButtons(nav_img_div);
            nav_img_div.className = "nav-img-div"
            const description = this.createDescriptionElement(project);
            div.appendChild(subheading);
            div.appendChild(nav_img_div);
            div.appendChild(description);
        }
    }

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
    // console.log(technologies);
    return technologies;
}

let parsed_objects = parseItemsInList(projects_from_server)
let technologies = pyObjectToJsObject(parsed_objects)

// div encapsulating the carousel
const main_div = document.createElement('div');
main_div.className = "carousel";

//  iterate through technologies to generate the html
let displayObjects = [];
const basePath = "static/img/"
for (let i = 0; i < technologies.length; i++) {
    // create container for each technology
    const subdiv = document.createElement('div');
    subdiv.className = 'tech-container';
    // get path to images
    const path_to_images = basePath + technologies[i].prog_language;
    // display the technology
    const displayTech = new DisplayTechnology(technologies[i], path_to_images);
    displayTech.displayHeading(subdiv);
    const projects = technologies[i].projects;
    displayTech.displayProjects(projects, subdiv);
    // add technology div to encapsulating container
    main_div.appendChild(subdiv);
    // store new objects
    displayObjects.push(displayTech);
}

for (let object in displayObjects){ 
    console.log(displayObjects[object]);
}

// add container of technologies to the projects section.
document.getElementById('projects').appendChild(main_div);

// TODO: figure out how to export my classes...