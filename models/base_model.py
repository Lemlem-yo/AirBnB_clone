"""
Base class that will be the foundation for Airbnb project
"""

import uuid
from datetime import datetime

class BaseModel:
	"""Base class for all classes"""

	def __init__(self):
		"""
		Initialise 3 public instance attributes
		Task 3 version
		"""
		self.id = uuid.uuid4()
		self.created_at = datetime.now()
		self.updated_at = datetime.now()

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
		to the current datetime
		"""
		self.updated_at = datetime.now()

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