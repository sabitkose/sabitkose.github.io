title: Step By Step Guide To Setup A Blog Using Python/Pelican And Github Pages
date: 2021-01-04 22:20
modified: 2021-01-04 22:20
author: Sabit
category: Python
tags: python, pelican
summary: Step By Step Guide To Setup A Blog Using Python/Pelican And Github Pages


# Pelican: What is it?
Pelican is a static site generator written in Python. You can write your content directly with your editor of choice in reStructuredText or Markdown formats.

# GitHub Pages: What is it?
GitHub Pages is a static site hosting service that takes HTML, CSS, and JavaScript files straight from a repository on GitHub, optionally runs the files through a build process and publishes a website.

# Create your repository
Head over to GitHub and create a new public repository named username.github.io, where the username is your username on GitHub.

![GitHub Pages Create A New Repository](images/github-pages-create-a-new-repository.png)

# Clone the repository
Go to the folder where you want to store your project, and clone your repository.

```
git clone https://github.com/username/username.github.io
cd username.github.io.git

```

# Optional: Create a Virtual Environment using “venv.”
The venv module supports creating lightweight “virtual environments” with site directories, optionally isolated from system site directories.

```
python3 -m venv env
source env/bin/activate

```

# Install Pelican
Pelican, ghp-import and markdown must be installed on your machine by pip.

```
pip install pelican ghp-import Markdown

```

# Create a Pelican Project
Create a skeleton project via the pelican-quickstart command, which begins by asking some questions about your site.

```
pelican-quickstart


> Where do you want to create your new web site? [.]  
> What will be the title of this web site? Your Site Name
> Who will be the author of this web site? Your Name
> What will be the default language of this web site? [en]
> Do you want to specify a URL prefix? e.g., http://example.com   (Y/n) n
> Do you want to enable article pagination? (Y/n)
> How many articles per page do you want? [10]
> What is your time zone? [Europe/Paris] Turkey
> Do you want to generate a Fabfile/Makefile to automate generation and publishing? (Y/n) y
> Do you want an auto-reload & simpleHTTP script to assist with theme and site development? (Y/n) y
> Do you want to upload your website using FTP? (y/N) n
> Do you want to upload your website using SSH? (y/N) n
> Do you want to upload your website using Dropbox? (y/N) n
> Do you want to upload your website using S3? (y/N) n
> Do you want to upload your website using Rackspace Cloud Files? (y/N) n
> Do you want to upload your website using GitHub Pages? (y/N) y
> Is this your personal page (username.github.io)? (y/N) y

```


Pelican creates the docs in your directory.

![Pelican Directory](images/pelican-directory.png)

Your blog posts, photos, images, etc., will be in the content directory.

# Create the first post
Go to the content directory

```
cd content

```

Create a markdown file name "hello blog".

```
touch hello-blog.md

```

```
Title: My First Review
Date: 2010-12-03 10:20
Category: Review

Following is a review of my favorite mechanical keyboard.

```

# Publish to GitHub
There are two branches of the repository.
One of them is content. The branch keeps the Pelican configurations and raw files. 
The other branch is master, which keeps web content.

Push the local changes to the remote repository hosted on GitHub.
```
git checkout -b content
Switched to a new branch 'content'

```

```
git add .
git commit -m 'initial pelican commit to content'
git push origin content

```
Run the command to generate your site:
```
pelican content -o output -s publishconf.py

```
Use ghp-import to add the contents of the output directory to the master branch:
```
ghp-import -m "Generate Pelican site" --no-jekyll -b master output

```
Push the local master branch to the remote repository:
```
git push origin master

```
# Check GitHub Pages setting. 

Go to your repository settings, then pages.
Your GitHub Pages site is currently being built from the master branch
![GitHub Pages Settings](images/github-pages-settings.png)

# Result
That's magic, and your website is running, go to http://username.github.io

All the best!
