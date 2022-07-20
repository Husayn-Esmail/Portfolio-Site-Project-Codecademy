// debated creating the secondary nav with js as well. 
// let secondary_nav = ['Python', 'C', 'Swift', 'HTML/CSS'];

class Project {
    constructor(name, images, description, path) {
        this.__name = name;
        this.__images = images;
        this.__description = description;
        this.__path = path;
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
        for (let i = 0; i < this.images.length; i++) {
            const img_path = `${this.path}/${this.images[i]}`;
            paths.push(img_path);
        }
        return paths;
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

class NavButtons {
    constructor(images_div) { 
        this.div = images_div;
        this.start = 0;
        this.end = this.div.children.length - 1;
        this.left = document.createElement('p');
        this.right = document.createElement('p');
    }

    setSymbols() {
        this.left.innerText = '<';
        this.right.innerText = '>';
    }

    setClasses() {
        this.left.className = "nav-button";
        this.right.className = "nav-button";
    }

    addFunctionality() {
        let position = this.start;
        // hide at start
        // hide at end
        if (position === this.start) {
            this.left.classList.add('hide');
        }
        this.left.addEventListener('click', (event) => {
            this.div.children[position].classList.add('hide');
            position -= 1;
            this.div.children[position].classList.remove('hide');
            // unhide button if moving from end
            if ((position + 1) === this.end) {
                this.right.classList.remove('hide');
            }
            if (position === this.start) {
                this.left.classList.add('hide');
            }
        });
        
        this.right.addEventListener('click', (event) => {
            // hide current, unhide next for a given div
            this.div.children[position].classList.add('hide');
            position += 1;
            this.div.children[position].classList.remove('hide');
            // unhide button if moving from start
            if ((position - 1) === this.start) {
                this.left.classList.remove('hide');
            }
            if (position === this.end) {
                this.right.classList.add("hide");
            }
        });
    }
}


class DisplayTechnology {
    constructor(technologyObject) {        
        this._technology = technologyObject;
        this._projects = technologyObject.projects;
        this.images = [];
    }

    get technology() {
        return this._technology;
    }

    get projects() {
        return this._projects;
    }

    createHeading() {
        /**
         * accepts a div as an argument.
         * appends a heading (based on the programming language specified in
         * the technology) to the div passed. returns null
         */
        let newHeading = document.createElement('h2');
        newHeading.innerHTML = this._technology.prog_language;
        newHeading.id = this._technology.prog_language;
        // add newHeading to div
        return newHeading
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

    
    createDescriptionElement(project) {
        const subdiv = document.createElement('div');
        const proj_description = project.description;
        const new_p = document.createElement('p');
        new_p.className = 'project-description';
        new_p.innerText = proj_description;
        subdiv.appendChild(new_p);
        return subdiv;
    }
    
    createNavButtons(images_div) {
        // init and add necessary properties to individual buttons
        let nav = new NavButtons(images_div);
        let left = nav.left;
        let right = nav.right;
        nav.setSymbols();
        nav.setClasses();
        nav.addFunctionality();
        // create a container for both buttons
        let div = document.createElement('div');
        div.className = 'nav-buttons-container';
        // create containers for each button
        const left_div = document.createElement('div');
        const right_div = document.createElement('div');
        left_div.className = "left";
        right_div.className = "right";
        left_div.appendChild(left);
        right_div.appendChild(right);
        // add nav buttons to the div
        div.appendChild(left_div);
        div.appendChild(right_div);
        return div;
    }
    
    createImageElements(project) {
        /**
         * Iterates through a projects images and creates an element for each
         * one with a class of project-image.
         * returns a div containing image elements.
         */
        let subdiv = document.createElement('div');
        subdiv.className = 'images';
        const images_paths = project.getImagePaths();
        // iterate through images and create img elements
        for (let i = 0; i < images_paths.length; i++) {
            const new_img = document.createElement('img');
            new_img.src = images_paths[i];
            new_img.classList.add('project-image');
            new_img.classList.add("hide");
            subdiv.appendChild(new_img);
        }
        return subdiv;
    }

    // create a function that processes the projects in this technology.
    // Call helper functions to display/get the resources to display such
    // elements.
    displayProjects(div) {
        const projects = this.projects
        for (let i = 0; i < projects.length; i++) {
            const project = projects[i];
            const subheading = this.createSubheadingElement(project);
            const nav_img_div = document.createElement("div");
            const img_elements = this.createImageElements(project);
            const nav = this.createNavButtons(img_elements);
            img_elements.appendChild(nav);
            const proj_name = project.name;
            const newObj = {[proj_name]: img_elements};
            this.images.push(newObj);
            // removes hide class because all images hidden upon instantiation
            img_elements.firstChild.classList.remove("hide");
            const description = this.createDescriptionElement(project);
            div.appendChild(subheading);
            div.appendChild(img_elements);
            div.appendChild(description);
        }
    }

    displayTechnology(main_div) {
        const div = document.createElement('div');
        div.className = 'tech-container';
        const heading = this.createHeading();
        div.appendChild(heading);
        this.displayProjects(div);
        main_div.appendChild(div);
    }

}


function parseItemsInList(listToBeParsed) {
    let parsed_projects = [];

    for (let i = 0; i < listToBeParsed.length; i++) {
        parsed_projects.push(JSON.parse(listToBeParsed[i]));
    }

    return parsed_projects;
}

function pyObjectToJsObject(parsed_projects, path) {
    let technologies = [];

    // convert python objects provided by server into Technology and Project
    // Objects
    for (let i = 0; i < parsed_projects.length; i++) {
        const prog_lang = parsed_projects[i]._ProjectsTechnology__prog_language;
        const obj_projects = parsed_projects[i]._ProjectsTechnology__projects;
        const newTech = new Technology(prog_lang);
        // iterate through projects and create Project objects
        for (let j = 0; j < obj_projects.length; j++) {
            // set vars to be added to Project object
            const proj_name = obj_projects[j]._Project__name;
            const proj_images = obj_projects[j]._Project__images;
            const proj_desc = obj_projects[j]._Project__description;
            const proj_path = `${path}/${prog_lang}/${proj_name}`;
            // create project object
            const proj_obj = new Project(proj_name, proj_images, proj_desc, proj_path);
            // add project to the technology
            newTech.add_project(proj_obj);
        }
        technologies.push(newTech);
    }
    return technologies;
}
// build and store objects
const base_path = 'static/img';
let parsed_objects = parseItemsInList(projects_from_server)
let technologies = pyObjectToJsObject(parsed_objects, base_path)

// div encapsulating the carousel
const main_div = document.createElement('div');
main_div.className = "technologies-container";

//  iterate through technologies to generate the html
let displayObjects = [];


for (let i = 0; i < technologies.length; i++) {
    const dispTech = new DisplayTechnology(technologies[i]);
    dispTech.displayTechnology(main_div);
    displayObjects.push(dispTech)
}

// add container of technologies to the projects section.
document.getElementById('projects').appendChild(main_div);

// TODO: figure out how to export my classes...
export default { DisplayTechnology, Project, Technology, NavButtons };