const assert = require("assert");
const { Project, Technology } = require("../portfolio-site/static/js/carousel");

describe("Test Project Class", () => {
    it('gets name', () => {
        expected = 'name'
        my_project = new Project('name', []);
        actual = my_project.name;
        assert.equal(expected, actual)
    });
    
    it('sets name', () => {
        new_name = "new_name";
        my_project = new Project('name', []);
        my_project.setName = new_name;
        expected = new_name;
        actual = my_project.name;
        assert.strictEqual(actual, expected);
    })

    
});