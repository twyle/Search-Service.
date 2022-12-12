output "rds_endpoint" {
  description = "The connection endpoint"
  value       = data.aws_db_instance.database.endpoint
}