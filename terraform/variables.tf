# core

variable "region" {
  description = "The AWS region to create resources in."
  default     = "us-east-1" 
}

# networking

variable "public_subnet_cidrs" {
  type        = list(string)
  description = "Public Subnet CIDR values"
  default     = ["10.0.1.0/24", "10.0.2.0/24"]
}

variable "availability_zones" {
  description = "Availability zones"
  type        = list(string)
  default     = ["us-east-1a", "us-east-1b"]
}

# load balancer

variable "health_check_path" {
  description = "Health check path for the default target group"
  default     = "/"
}

# ecs

variable "ecs_cluster_name" {
  description = "Name of the ECS cluster"
  default     = "development"
}

# key pair

variable "ssh_pubkey_file" {
  description = "Path to an SSH public key"
  default     = "~/.ssh/ec2-key.pub"
}

# ecs

variable "amis" {
  description = "Which AMI to spawn."
  default = {
    us-east-1 = "ami-0574da719dca65348"
  }
}
variable "instance_type" {
  default = "t2.micro"
}
variable "docker_image_url_flask" {
  description = "Docker image to run in the ECS cluster"
  default     = "lyleokoth/blog-service:latest"
}
variable "app_count" {
  description = "Number of Docker containers to run"
  default     = 2
}

