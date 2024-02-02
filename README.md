# BookWander

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-3.2-green)](https://www.djangoproject.com/)
[![Docker](https://img.shields.io/badge/Docker-19.03%2B-blue)](https://www.docker.com/)
[![AWS](https://img.shields.io/badge/AWS-Cloud-orange)](https://aws.amazon.com/)
[![Elasticsearch](https://img.shields.io/badge/Elasticsearch-7.0-blue)](https://www.elastic.co/)
[![Redis](https://img.shields.io/badge/Redis-6-red)](https://redis.io/)
[![Stripe](https://img.shields.io/badge/Stripe-Payment-brightgreen)](https://stripe.com/)
[![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-CI%2FCD-brightgreen)](https://github.com/features/actions)

## Overview

BookWander is a modern web application that transforms the way users experience books. It offers a seamless platform for discovering, purchasing, and managing eBooks. The application leverages advanced technologies to provide a personalized and efficient book-browsing experience.

## Architecture

The application is built using the following technologies:

- **Backend**: Django, Python
- **Frontend/UI**: HTML, CSS, JavaScript
- **Database**: PostgreSQL
- **Cloud Services**: AWS (Amazon S3)
- **Search Engine**: Elasticsearch
- **Caching Service**: Redis
- **Payment Processing**: Stripe
- **Containerization**: Docker

## Features

- **User Authentication**: Secure user registration and login.
- **Book Search**: Advanced search capabilities using Elasticsearch.
- **Recommendation Engine**: Personalized book recommendations based on user preferences.
- **Shopping Cart**: Seamless cart management with flexible update options.
- **Checkout and Payment**: Smooth payment processing using Stripe.
- **User Profile**: Customizable user profiles with purchase and search history.
- **Book Reviews**: Ability to rate and review books.

## API Endpoints

Detailed API documentation is available in the [API Documentation](API.md) file.

## Installation

Follow these steps to set up and run the BookWander application:

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/BookWander.git
    cd BookWander
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Set up the database:

    ```bash
    python manage.py migrate
    ```

4. Run the development server:

    ```bash
    python manage.py runserver
    ```

Visit [http://localhost:8000/](http://localhost:8000/) in your browser to access the application.

## Contributing

We welcome contributions! Check out the [Contribution Guidelines](CONTRIBUTING.md) to get started.

## License

This project is licensed under the [MIT License](LICENSE).
