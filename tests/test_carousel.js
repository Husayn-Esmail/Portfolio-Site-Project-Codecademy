const assert = require("assert");
const { Project, Technology } = require("../portfolio-site/static/js/carousel");

describe("Test Project Class", () => {
    it('gets name', () => {
        const expected = 'name'
        let my_project = new Project(expected, []);
        const actual = my_project.name;
        assert.equal(expected, actual)
    });
    
    it('sets name', () => {
        const new_name = "new_name";
        let my_project = new Project('name', []);
        my_project.setName = new_name;
        const expected = new_name;
        const actual = my_project.name;
        assert.strictEqual(actual, expected);
    })

    it('gets images', () => {
        const images = ['one', 'two'];
        let my_project = new Project('name', images);
        const actual = my_project.images;
        const expected = images;
        assert.strictEqual(expected, actual);
    });
    
});