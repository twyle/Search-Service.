[
  {
    "name": "flask-app",
    "image": "${docker_image_url_flask}",
    "essential": true,
    "cpu": 10,
    "memory": 512,
    "links": [],
    "portMappings": [
      {
        "containerPort": 5000,
        "hostPort": 0,
        "protocol": "tcp"
      }
    ],
    "command": ["gunicorn", "-w", "3", "-b", ":5000", "manage:app"],
    "environment": [],
  }
]