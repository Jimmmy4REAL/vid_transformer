# FizzBuzz Web App

This is a simple web application that prints the numbers from 1 to 100 according to the FizzBuzz rules. It replaces multiples of 3 with "Fizz," multiples of 5 with "Buzz," and multiples of both 3 and 5 with "FizzBuzz."

## Getting Started

To run this project, you have two options:

1. Run the project using Python and React (without Docker).
2. Run the project using Docker Compose.

Please choose the method that suits your preference and environment.

### Option 1: Python and React (without Docker)

#### Prerequisites

Make sure you have the following installed on your system:

- Node.js
- npm
- Python (version 3.x)

#### Frontend Setup

1. Open a terminal and navigate to the `frontend` directory.
2. Install frontend dependencies:

```bash
npm install
```
3. Start the React development server:

```bash
npm start
```
The frontend will be running at http://localhost:3000.

#### Backend Setup

1. Open another terminal and navigate to the root directory of the project.
2. Install backend dependencies:

```bash
pip install Flask
```
3. Start the Python backend API:

The backend API will be running at http://127.0.0.1:8080/fizzbuzz.

### Option 2: Docker compose

#### Prerequisites

Make sure you have the following installed on your system:

- Docker and Docker Compose installed on your system.

#### Run the Application

1. Open a terminal and navigate to the root directory of the project (where the docker-compose.yml file is located).

2. Run the following command to build and start the Docker containers:

```bash
docker-compose up
```

The frontend will be accessible at http://localhost:3000.

## Usage
Open your web browser and visit http://localhost:3000 to see the FizzBuzz list displayed on the webpage.
