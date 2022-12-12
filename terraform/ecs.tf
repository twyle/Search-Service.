resource "aws_ecs_cluster" "development" {
  name = "${var.ecs_cluster_name}-cluster"
}

resource "aws_launch_configuration" "ecs" {
  name                        = "${var.ecs_cluster_name}-cluster"
  image_id                    = lookup(var.amis, var.region)
  instance_type               = var.instance_type
  security_groups             = [aws_security_group.ecs.id]
  iam_instance_profile        = aws_iam_instance_profile.ecs.name
  key_name                    = aws_key_pair.development.key_name
  associate_public_ip_address = true
  user_data                   = "#!/bin/bash\necho ECS_CLUSTER='${var.ecs_cluster_name}-cluster' > /etc/ecs/ecs.config"
}

data "template_file" "app" {
  template = file("templates/flask_app.json.tpl")

  vars = {
    docker_image_url_flask = var.docker_image_url_flask
    region                  = var.region
  }
}

resource "aws_ecs_task_definition" "app" {
  family                = "flask-app"
  container_definitions = data.template_file.app.rendered
}

resource "aws_ecs_service" "development" {
  name            = "${var.ecs_cluster_name}-service"
  cluster         = aws_ecs_cluster.development.id
  task_definition = aws_ecs_task_definition.app.arn
  iam_role        = aws_iam_role.ecs-service-role.arn
  desired_count   = var.app_count
  depends_on      = [aws_alb_listener.ecs-alb-http-listener, aws_iam_role_policy.ecs-service-role-policy]

  load_balancer {
    target_group_arn = aws_alb_target_group.default-target-group.arn
    container_name   = "flask-app"
    container_port   = 5000
  }
}