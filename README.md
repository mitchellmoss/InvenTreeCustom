
Introduction
Configuration
Docker 
Introduction
Production
Development
Bare Metal 
Introduction
Installer
Production
Development
Serving Files
Data Backup
Migrating Data
Advanced Topics
Table of contents
Introduction
Database
Media Files
Web Server
Background Tasks
OS Requirements
Python Requirements
Invoke
Virtual Environment
Activating a Virtual Environment
InvenTree Source Code
Installation Guides
Docker
Bare Metal
Debug Mode
Potential Issues
Fast install

A quick-and-easy install can be done done with the following one-liner.

wget -qO install.sh https://get.inventree.org && bash install.sh
Read more about the installer.
Introduction¶
InvenTree can be self-hosted with minimal system requirements. Multiple database back-ends are supported, allowing for flexibility where required.

The InvenTree server ecosystem consists of the following components:

Database¶
A persistent database is required for data storage. InvenTree can be used with any of the following database backends:

PostgreSQL
MySQL / MariaDB
SQLite
SQLite

While SQLite provides a simpler setup and is useful for a development environment, we strongly recommend against using it for a production environment. Use PostgreSQL or MySQL instead

Database selection should be determined by your particular installation requirements.

Media Files¶
Uploaded media files (images, attachments, reports, etc) are stored to a persistent storage volume.

Web Server¶
The bulk of the InvenTree code base supports the custom web server application. The web server application services user requests and facilitates database access.

The webserver code also provides a first-party API for performing database query actions.

Once a database is setup, you need a way of accessing the data. InvenTree provides a "server" application out of the box, but this may not scale particularly well with multiple users. Instead, InvenTree can be served using a webserver such as Gunicorn. For more information see the deployment documentation.

Background Tasks¶
A separate application handles management of background tasks, separate to user-facing web requests.

OS Requirements¶
The InvenTree documentation assumes that the operating system is a debian based Linux OS. Some installation steps may differ for different systems.

Installing on Windows

Installation on Windows is not guaranteed to work (at all). To install on a Windows system, it is highly recommended that you install WSL, and then follow installation procedure from within the WSL environment.

Docker

Installation on any OS is simplified by following the docker setup guide.

Python Requirements¶
InvenTree runs on Python.

Python Version

InvenTree requires Python 3.9 (or newer). If your system has an older version of Python installed, you will need to follow the update instructions for your OS.

Invoke¶
InvenTree makes use of the invoke python toolkit for performing various administrative actions.

Invoke Version

InvenTree requires invoke version 2.0.0 or newer. Some platforms may be shipped with older versions of invoke!

Updating Invoke

To update your invoke version, run pip install -U invoke

To display a list of the available InvenTree administration actions, run the following commands from the top level source directory:

invoke --list
Virtual Environment¶
Installing the required Python packages inside a virtual environment allows a local install separate to the system-wide Python installation. While not strictly necessary, using a virtual environment is highly recommended as it prevents conflicts between the different Python installations.

You can read more about Python virtual environments here.

Virtual Environment

The installation instruction assume that a virtual environment is configured

cd into the InvenTree directory, and create a virtual environment with the following command:

python3 -m venv env
Activating a Virtual Environment¶
The virtual environment needs to be activated to ensure the correct python binaries and libraries are used. The InvenTree instructions assume that the virtual environment is always correctly activated.

To configure Inventree inside a virtual environment, cd into the inventree base directory and run the following command:

source env/bin/activate
Activate Virtual Environment

if

source env/bin/activate
is not working try
. env/bin/activate
This will place the current shell session inside a virtual environment - the terminal should display the (env) prefix.

InvenTree Source Code¶
InvenTree source code is distributed on GitHub, and the latest version can be downloaded (using Git) with the following command:

git clone https://github.com/inventree/inventree/
Alternatively, the source can be downloaded as a .zip archive.

Updating via Git

Downloading the source code using Git is recommended, as it allows for simple updates when a new version of InvenTree is released.

Installation Guides¶
There are multiple ways to get an InvenTree server up and running, of various complexity (and robustness)!

Docker¶
The recommended method of installing InvenTree is to use docker. InvenTree provides out-of-the-box support for docker and docker compose, which provides a simple, reliable and repeatable pipeline for integration into your production environment.

Refer to the following guides for further instructions:

Docker development server setup guide
Docker production server setup guide
Bare Metal¶
If you do not wish to use the docker container, you will need to manually install the required packages and follow through the installation guide.

Refer to the following guides for further instructions:

Bare metal development server setup guide
Bare metal production server setup guide
Debug Mode¶
By default, the InvenTree web server is configured to run in DEBUG mode.

Running in DEBUG mode provides many handy development features, however it is strongly recommended NOT to run in DEBUG mode in a production environment. This recommendation is made because DEBUG mode leaks a lot of information about your installation and may pose a security risk.

So, for a production setup, you should set INVENTREE_DEBUG=false in the configuration options.

Potential Issues¶
Turning off DEBUG mode creates further work for the system administrator. In particular, when running in DEBUG mode, the InvenTree web server natively manages static and media files, which means that the InvenTree server can run "monolithically" without the need for a separate web server.

Read More

Refer to the Serving Files section for more details

February 1, 2024





<div align="center">
  <img src="images/logo/inventree.png" alt="InvenTree logo" width="200" height="auto" />
  <h1>InvenTree</h1>
  <p>Open Source Inventory Management System </p>

<!-- Badges -->
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)![GitHub tag (latest SemVer)](https://img.shields.io/github/v/tag/inventree/inventree)
![CI](https://github.com/inventree/inventree/actions/workflows/qc_checks.yaml/badge.svg)
[![Documentation Status](https://readthedocs.org/projects/inventree/badge/?version=latest)](https://inventree.readthedocs.io/en/latest/?badge=latest)
![Docker Build](https://github.com/inventree/inventree/actions/workflows/docker.yaml/badge.svg)
[![OpenSSF Best Practices](https://bestpractices.coreinfrastructure.org/projects/7179/badge)](https://bestpractices.coreinfrastructure.org/projects/7179)
[![Netlify Status](https://api.netlify.com/api/v1/badges/9bbb2101-0a4d-41e7-ad56-b63fb6053094/deploy-status)](https://app.netlify.com/sites/inventree/deploys)
[![DeepSource](https://app.deepsource.com/gh/inventree/InvenTree.svg/?label=active+issues&show_trend=false&token=trZWqixKLk2t-RXtpSIAslVJ)](https://app.deepsource.com/gh/inventree/InvenTree/)

[![Coveralls](https://img.shields.io/coveralls/github/inventree/InvenTree)](https://coveralls.io/github/inventree/InvenTree)
[![Crowdin](https://badges.crowdin.net/inventree/localized.svg)](https://crowdin.com/project/inventree)
![GitHub commit activity](https://img.shields.io/github/commit-activity/m/inventree/inventree)
[![Docker Pulls](https://img.shields.io/docker/pulls/inventree/inventree)](https://hub.docker.com/r/inventree/inventree)

![GitHub Org's stars](https://img.shields.io/github/stars/inventree?style=social)
[![Twitter Follow](https://img.shields.io/twitter/follow/inventreedb?style=social)](https://twitter.com/inventreedb)
[![Subreddit subscribers](https://img.shields.io/reddit/subreddit-subscribers/inventree?style=social)](https://www.reddit.com/r/InvenTree/)


<h4>
    <a href="https://demo.inventree.org/">View Demo</a>
  <span> · </span>
    <a href="https://docs.inventree.org/en/latest/">Documentation</a>
  <span> · </span>
    <a href="https://github.com/inventree/InvenTree/issues/new?template=bug_report.md&title=[BUG]">Report Bug</a>
  <span> · </span>
    <a href="https://github.com/inventree/InvenTree/issues/new?template=feature_request.md&title=[FR]">Request Feature</a>
  </h4>
</div>

<!-- About the Project -->
## :star2: About the Project

InvenTree is an open-source Inventory Management System which provides powerful low-level stock control and part tracking. The core of the InvenTree system is a Python/Django database backend which provides an admin interface (web-based) and a REST API for interaction with external interfaces and applications. A powerful plugin system provides support for custom applications and extensions.

Check out [our website](https://inventree.org) for more details.

<!-- Roadmap -->
### :compass: Roadmap

Want to see what we are working on? Check out the [roadmap tag](https://github.com/inventree/InvenTree/issues?q=is%3Aopen+is%3Aissue+label%3Aroadmap) and [horizon milestone](https://github.com/inventree/InvenTree/milestone/42).

<!-- Integration -->
### :hammer_and_wrench: Integration

InvenTree is designed to be **extensible**, and provides multiple options for **integration** with external applications or addition of custom plugins:

* [InvenTree API](https://docs.inventree.org/en/latest/api/api/)
* [Python module](https://docs.inventree.org/en/latest/api/python/python/)
* [Plugin interface](https://docs.inventree.org/en/latest/extend/plugins)
* [Third party tools](https://docs.inventree.org/en/latest/extend/integrate)

<!-- TechStack -->
### :space_invader: Tech Stack

<details>
  <summary>Server</summary>
  <ul>
    <li><a href="https://www.python.org/">Python</a></li>
    <li><a href="https://www.djangoproject.com/">Django</a></li>
    <li><a href="https://www.django-rest-framework.org/">DRF</a></li>
    <li><a href="https://django-q.readthedocs.io/">Django Q</a></li>
    <li><a href="https://django-allauth.readthedocs.io/">Django-Allauth</a></li>
  </ul>
</details>

<details>
<summary>Database</summary>
  <ul>
    <li><a href="https://www.postgresql.org/">PostgreSQL</a></li>
    <li><a href="https://www.mysql.com/">MySQL</a></li>
    <li><a href="https://www.sqlite.org/">SQLite</a></li>
    <li><a href="https://redis.io/">Redis</a></li>
  </ul>
</details>

<details>
  <summary>Client</summary>
  <ul>
    <li><a href="https://getbootstrap.com/">Bootstrap</a></li>
    <li><a href="https://jquery.com/">jQuery</a></li>
    <li><a href="https://bootstrap-table.com/">Bootstrap-Table</a></li>
  </ul>
</details>

<details>
<summary>DevOps</summary>
  <ul>
    <li><a href="https://hub.docker.com/r/inventree/inventree">Docker</a></li>
    <li><a href="https://crowdin.com/project/inventree">Crowdin</a></li>
    <li><a href="https://coveralls.io/github/inventree/InvenTree">Coveralls</a></li>
    <li><a href="https://app.deepsource.com/gh/inventree/InvenTree">DeepSource</a></li>
    <li><a href="https://packager.io/gh/inventree/InvenTree">Packager.io</a></li>
  </ul>
</details>

<!-- Getting Started -->
## 	:toolbox: Deployment / Getting Started

There are several options to deploy InvenTree.

<div align="center"><h4>
    <a href="https://docs.inventree.org/en/latest/start/docker/">Docker</a>
    <span> · </span>
    <a href="https://inventree.org/digitalocean"><img src="https://www.deploytodo.com/do-btn-blue-ghost.svg" alt="Deploy to DO" width="auto" height="40" /></a>
    <span> · </span>
    <a href="https://docs.inventree.org/en/latest/start/install/">Bare Metal</a>
</h4></div>

Single line install - read [the docs](https://docs.inventree.org/en/latest/start/installer/) for supported distros and details about the function:
```bash
wget -qO install.sh https://get.inventree.org && bash install.sh
```

Refer to the [getting started guide](https://docs.inventree.org/en/latest/start/install/) for a full set of installation and setup instructions.

<!-- Mobile App -->
## 	:iphone: Mobile App

InvenTree is supported by a [companion mobile app](https://docs.inventree.org/en/latest/app/app/) which allows users access to stock control information and functionality.

<div align="center"><h4>
    <a href="https://play.google.com/store/apps/details?id=inventree.inventree_app">Android Play Store</a>
     <span> · </span>
    <a href="https://apps.apple.com/au/app/inventree/id1581731101#?platform=iphone">Apple App Store</a>
</h4></div>

<!-- Contributing -->
## :wave: Contributing

Contributions are welcomed and encouraged. Please help to make this project even better! Refer to the [contribution page](CONTRIBUTING.md).

<!-- Translation -->
## :scroll: Translation

Native language translation of the InvenTree web application is [community contributed via crowdin](https://crowdin.com/project/inventree). **Contributions are welcomed and encouraged**.

<!-- Sponsor -->
## :money_with_wings: Sponsor

If you use InvenTree and find it to be useful, please consider [sponsoring the project](https://github.com/sponsors/inventree).

<!-- Acknowledgments -->
## :gem: Acknowledgements

We would like to acknowledge a few special projects:
 - [PartKeepr](https://github.com/partkeepr/PartKeepr) as a valuable predecessor and inspiration
 - [Readme Template](https://github.com/Louis3797/awesome-readme-template) for the template of this page

Find a full list of used third-party libraries in [our documentation](https://docs.inventree.org/en/latest/credits/).

## :heart: Support

<p>This project is supported by the following sponsors:</p>

<p align="center">
<a href="https://github.com/MartinLoeper"><img src="https://github.com/MartinLoeper.png" width="60px" alt="Martin Löper" /></a>
<a href="https://github.com/lippoliv"><img src="https://github.com/lippoliv.png" width="60px" alt="Oliver Lippert" /></a>
<a href="https://github.com/lfg-seth"><img src="https://github.com/lfg-seth.png" width="60px" alt="Seth Smith" /></a>
<a href="https://github.com/snorkrat"><img src="https://github.com/snorkrat.png" width="60px" alt="" /></a>
<a href="https://github.com/spacequest-ltd"><img src="https://github.com/spacequest-ltd.png" width="60px" alt="SpaceQuest Ltd" /></a>
<a href="https://github.com/appwrite"><img src="https://github.com/appwrite.png" width="60px" alt="Appwrite" /></a>
<a href="https://github.com/PricelessToolkit"><img src="https://github.com/PricelessToolkit.png" width="60px" alt="" /></a>
<a href="https://github.com/cabottech"><img src="https://github.com/cabottech.png" width="60px" alt="Cabot Technologies" /></a>
<a href="https://github.com/markus-k"><img src="https://github.com/markus-k.png" width="60px" alt="Markus Kasten" /></a>
</p>

<p>With ongoing resources provided by:</p>

<p align="center">
  <a href="https://inventree.org/digitalocean">
    <img src="https://opensource.nyc3.cdn.digitaloceanspaces.com/attribution/assets/SVG/DO_Logo_horizontal_blue.svg" width="201px" alt="Servers by Digital Ocean">
  </a>
  <a href="https://www.netlify.com"> <img src="https://www.netlify.com/v3/img/components/netlify-color-bg.svg" alt="Deploys by Netlify" /> </a>
  <a href="https://crowdin.com"> <img src="https://crowdin.com/images/crowdin-logo.svg" alt="Translation by Crowdin" /> </a>
</p>


<!-- License -->
## :warning: License

Distributed under the [MIT](https://choosealicense.com/licenses/mit/) License. See [LICENSE.txt](https://github.com/inventree/InvenTree/blob/master/LICENSE) for more information.
