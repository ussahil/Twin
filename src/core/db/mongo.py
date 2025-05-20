from pymongo import MongoClient 
from pymongo.errors import ConnectionFailure

from core.config import settings #Create this
from core.logger_utils import get_logger

logger = get_logger(__file__)

class MongoDatabaseConnector:
  """ Singleton class to connect to MongoDB Database."""
  _instance: MongoClient | None=None
  # _instance stores single mongo client Instance | this is used for type hinting
  def __new__(cls,*args,**kwargs):
    # With the new we are overwriting and ensuring that the same instance is returned every single time
    if cls._instance is None:
      try:
        cls._instance = MongoClient(settings.MONGO_DATABASE_HOST)
        logger.info(
          f"Connection to database with uri: {settings.MONGO_DATABASE_HOST} successful"
        )
      except ConnectionFailure:
        logger.error(f"Couldn't connect to the Database")
        
        raise 
    return cls._instance
  
  def get_database(self):
    assert self._instance , "Database connection not initialized"
    
    return self._instance[settings.MONGO_DATABASE_NAME]
  
  def close(self):
    if self._instance:
      self._instance.close()
      logger.info("Connection to database has been closed")
      
connection = MongoDatabaseConnector()