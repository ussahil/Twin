import uuid # Allow us to create unique identifiers
from typing import List, Optional # type Hinting

from pydantic import UUID4, BaseModel, ConfigDict, Field
# UUID4 - UUIDS follow version 4, Basemodel : User to create base , ConfigDict: Allows you to create Dict for configuration parameters , Field : Used to add addtional settings
from pymongo import errors
# Local imports
import core.logger_utils as logger_utils   # created thi
from core.db.mongo import connection
from core.errors import ImproperlyConfigured

_database = connection.get_database("twin")

logger = logger_utils.get_logger(__name__)


class BaseDocument(BaseModel):
  id: UUID4 = Field(default_factory=uuid.uuid4)
  
  model_config = ConfigDict(from_attributes=True,populate_by_name=True)
  
  @classmethod
  def from_mongo(cls,data:dict):
    """Convert "_id" (str object) into id (UUID object) """
    if not data:
      return data 
    
    id = data.pop("_id",None)
    return cls(**dict(data,id=id))
  
  def to_mongo(self,**kwargs) -> dict:
    """ Convert id (UUID object) into "_id" (str object) """
    