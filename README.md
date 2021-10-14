# Gas Station Queue

A scheduling platform intended to reduce traffic jam in an around a local Gas Station owned by JaffalGroup.

## Table of Content

- [Introduction](#introduction)
- [My Process](#my-process)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Links](#links)

## Introduction

- Due to the fuel shortage that hit Lebanon in the summer of 2021, Gas stations arounnd the country where overwhelmed by the huge demand for fuel by their customers accompanied by a significant drop in supply from Companies that supplied them with fuel. So, I contacted this local gas station and offered to make them a website that let the customers to schedule a specific time to fill up their cars with fuel and avoid jamming the station and reduce waiting time on the customer.

## Run Locally

Clone the project

```bash
  git clone https://github.com/HaithamKhadra/station_q.git
```

Go to the project directory

```bash
  cd station_q
```

Create django and a virtual environment

```bash
  python -m pip install pipenv
  pipenv install django==3.3
```

Now activate the virtual environment

```bash
  pipenv shell
```

Install dependencies (xlwt is a Library to create spreadsheet files)

```bash
  pipenv install xlwt
```

Start the server

```bash
  python manage.py runserver
```

## Features

- Responsive design.

## Tech Stack

- ### Tools used on the **Client side:**

  - **HTML**
  - **CSS**
  - **Bootstrap**
  - **Javascript (ES6+)**

- ### Tools used on the **Server side:**

  - **Python** - **Django**
  - **SQL** - **Sqlite3**

## Links

- [live Site URL](https://jaffalgroup.pythonanywhere.com)
