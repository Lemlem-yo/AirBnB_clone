"""
Base class that will be the foundation for Airbnb project
"""


import uuid
import models
from datetime import datetime


class BaseModel:
    """Base class for all classes"""

    def __init__(self, *args, **kwargs):
        """
        Initialise 3 public instance attributes
        use *args, **kwargs arguments for the constructor of a BaseModel
        """
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    newVal = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                    setattr(self, key, newVal)
                elif key == "__class__":
                    continue
                else:
                    setattr(self, key, value)

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
        Returns an easy-to-read string
        """
        clsName = self.__class__.__name__
        iD = self.id
        dI = self.__dict__
        return "[{}] ({}) {}".format(clsName, iD, dI)

    def save(self):
        """
        Update the public instance attribute updated_at
        to the current datetimecat test_base_model.py
        """
        models.storage.save()

    def to_dict(self):
        """
        Returns a dictionary containing all
        keys/values of __dict__ of the instance
        """
        returnDict = self.__dict__.copy()
        returnDict["__class__"] = self.__class__.__name__
        returnDict["created_at"] = self.created_at.isoformat()
        returnDict["updated_at"] = self.updated_at.isoformat()
        return returnDict
