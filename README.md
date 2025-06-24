# Portfolio Project Codecademy

This project is part of the codecademy full-stack engineer course. The goal of
the project is to create a website using HTML, CSS that shows off some of my
work so far. It's requirements are that it has a homepage that shows projects
as well as another page with contact information. The website should be
responsive and have at least one interactive element implemented using
javascript. I will be using all of those things and will likely be using flask
or django as a proper web backend.

## For my future reference...

How to develop within this project.

There is an auto deployment hook in the "proj" folder on the server (post-recieve)

Use tmux to inspect the server status when you ssh in.

make all changes in dev branch (local development)

then merge dev into production branch

then run

```bash
git push live production
```

which will call the hook and push directly to the server.

You can basically choose whenever you want to merge dev into main. I'd say ideally after you've come up with a good major version push.
