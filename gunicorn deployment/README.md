# Django app deployment with Gunicorn and Nginx
## Installing Packages
we need to install multiple packages for setting up a django project with gunicorn, virtual envirment and nginx. we need the following packages  for making our environment ready.
- python
- python-venv
- nginx
- postgres
- curl

To install the necessary packages :
```sh
sudo apt update
sudo apt install python3-venv python3-dev libpq-dev postgresql postgresql-contrib nginx curl
```

## Setting virtual environment
In your project directory, you need to setting virtual environment to separate your django project environment from your native environment.

```sh
python3 -m venv myprojectenv # setting new virtual environment
source myprojectenv/bin/activate # activate the virtual environment
deactivate # deactivate the virtual environment
```
installing packages on virtual environment 

```sh
pip install django gunicorn psycopg2-binary
```
## Starting a django project 
```sh
python3 manage.py runserver # general way to start django project
gunicorn --bind 0.0.0.0:8000 myproject.wsgi # way to start django project with gunicorn
```
It necessary to activate venv before starting a django project

## Creating system socket and service for gunicorn
The Gunicorn socket will be created at boot and will listen for connections. When a connection occurs, systemd will automatically start the Gunicorn process to handle the connection.

### gunicorn  system socket file
```sh
sudo nano /etc/systemd/system/gunicorn.socket
```

```sh
[Unit]
Description=gunicorn socket

[Socket]
ListenStream=/run/gunicorn.sock

[Install]
WantedBy=sockets.target
```

create and open a systemd service file for Gunicorn with sudo privileges in your text editor. The service filename should match the socket filename with the exception of the extension:

### Creating system service file
```sh
sudo nano /etc/systemd/system/gunicorn.service
```

```sh
[Unit]
Description=gunicorn daemon
Requires=gunicorn.socket
After=network.target

[Service]
User=django-user      # need to configure 
Group=www-data
WorkingDirectory=/home/django-user/myprojectdir
ExecStart=/home/django-user/myprojectdir/myprojectenv/bin/gunicorn \
          --access-logfile - \
          --workers 3 \
          --bind unix:/run/gunicorn.sock \
          myproject.wsgi:application

[Install]
WantedBy=multi-user.target

```
When you have completed and checked your file, you can run the following commands to start your systemd file:
```sh
sudo systemctl start gunicorn.socket
sudo systemctl enable gunicorn.socket
sudo systemctl status gunicorn
```
#### Important Alert 
Every time you make changes to your python files, if you want to add or update any project file - you will need to restart the systemd files with the following commands:

```sh
sudo systemctl daemon-reload
sudo systemctl restart gunicorn
```

If the output shows an error, you probably misconfigured something, so check the logs to find out. Run the following command to see the Gunicorn logs: 
```sh
sudo journalctl -u gunicorn
```

### Chages on settings.py
```sh
DEBUG = False
ALLOWED_HOSTS = ['*']
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
```

### Static files
 The collectstatic command copies the static files from all applications and saves them in the STATIC_ROOT directory. Open a terminal and run the following command:

```sh
python manage.py collectstatic
```

## COnfiguring Nginx
```sh
sudo nano /etc/nginx/sites-available/myproject
```
```sh
server {
	listen 80;
	server_name 192.168.1.107;

	location = /favicon.ico { access_log off; log_not_found off; }
	location /static {
    	autoindex on;
    	alias /home/django/myprojectdir/static;
	}

	location / {
    	include proxy_params;
    	proxy_pass http://unix:/run/gunicorn.sock;
	}
}
```
Be sure to change the IP here to the one you are using. When finished, save and close the file. We can now enable the file by linking it to the sites-enabled directory:

```sh
sudo ln -s /etc/nginx/sites-available/djang_website /etc/nginx/sites-enabled
```
Test your Nginx configuration for syntax errors by typing:

```sh 
sudo nginx -t
```

If no errors are reported, go ahead and restart Nginx by typing:
```sh
sudo systemctl restart nginx
```

you need to open up your firewall to normal traffic on port 80. Since you no longer need access to the development server, you can remove the rule to open port 8000 as well:

```sh
sudo ufw delete allow 8000
sudo ufw allow 'Nginx Full'
```


