# CTFd-Nginx-LetsEncrypt

This project provides a fully configurable and automated setup for deploying [CTFd](https://github.com/CTFd/CTFd) with Nginx and Let's Encrypt using Docker and Ansible. The setup is designed to be portable and configurable via code.

## Features
- Fully automated deployment of CTFd with Nginx as a reverse proxy
- Automatic SSL certificate generation and renewal with Let's Encrypt
- Completely configurable via Ansible for seamless setup and portability
- Modular and adaptable for different environments
- Automatic setup with variables

## Requirements
- Docker
- Docker Compose
- Ansible (for automated deployment)

## Installation

1. Clone this repository:
   ```sh
   git clone https://github.com/ViperBlackSkull/Ansible-CTFd/
   cd CTFd-Nginx-LetsEncrypt
   ```

2. Configure the `.env` file with your domain and email for Let's Encrypt.

3. Run the Ansible playbook:
   ```sh
   ansible-playbook deploy.yml
   ```

4. Access your CTFd instance via `https://yourdomain.com`.

## Credits
This repository is based on the original work by [chrisandoryan](https://github.com/chrisandoryan/CTFd-Nginx-LetsEncrypt). Special thanks to them for their contributions to the CTF community.

## License
See the `LICENSE` file for more details.
