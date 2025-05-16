import uuid # Allow us to create unique identifiers
from typing import List, Optional # type Hinting

from pydantic import UUID4, BaseModel, ConfigDict, Field
# UUID4 - UUIDS follow version 4, Basemodel : User to create base , ConfigDict: Allows you to create Dict for configuration parameters , Field : Used to add addtional settings
from pymongo import errors
# Local imports
import core.logger_utils as logger_utils   # created thi
from core.db.mongo import connection
from core.errors import ImproperlyConfigured