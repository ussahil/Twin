import structlog # Structured logging libraray for py

def get_logger(cls:str):
  """
  This func returns a logger instance that's bound with the context of the class or module
  """
  return structlog.get_logger().bind(cls=cls)