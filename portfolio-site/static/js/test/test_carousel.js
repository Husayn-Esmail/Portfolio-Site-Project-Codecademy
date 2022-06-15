const assert = require("assert");
const { Project, Technology } = require("../carousel");

describe("Test Project Class", () => {
    it('gets name', () => {
        expected = 'name'
        my_project = new Project('name', []);
        actual = my_project.name;
        assert.equal(expected, actual)
    });
});