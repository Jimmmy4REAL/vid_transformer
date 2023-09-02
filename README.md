# Video to Audio Converter Application

## Overview

This application is designed to convert video files into audio. It follows a microservices architecture, with the codebase organized into distinct services, each responsible for a specific aspect of the application. The main components include:

- **Authentication Service**: Handles user authentication and authorization, JWT was chosen.
- **Gateway Service**: Manages incoming requests and routes them to the appropriate microservice.
- **Converter Service**: Contains the core logic for video-to-audio conversion.
- **RabbitMQ Service**: Configures and manages RabbitMQ, serving as a message broker for asynchronous processing.

## Technologies Used

- **Web Framework**: Flask was chosen as the web framework for its ease of use and agility in development.
- **Data Storage**: MySQL is employed to store user authentication information, while MongoDB, specifically GridFS, is utilized to store both video and audio data. GridFS is particularly suited for handling large original videos while preserving their quality.
- **Asynchronous Processing**: RabbitMQ is used as a message broker to enable asynchronous processing, enhancing the application's scalability and elasticity.
- **Containerization**: Docker and Kubernetes are implemented to ensure the availability of replicated Converter Services, facilitating scaling up as needed.
- **Version Control**: Git is used to track application milestones.

## Getting Started

To run the application, follow these steps:

1. Build Docker images for the microservices.
2. Apply the Kubernetes configuration files to create replicas of the Converter Service.
3. Send requests to the application using your preferred method, such as `curl` or Postman.

