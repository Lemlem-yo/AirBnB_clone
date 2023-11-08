"""FileSorage Class"""

import json

class FileStorage:
	
	"""
	A class that serializes instances to a
	JSON file and deserializes JSON file to instances
	"""
	__file_path = "file.json"
	__objects = {}

	def all(self):
		"""Method to return the dictionary __objects"""
		return FileStorage.__objects
	
	def new(self, obj):
		"""Sets in __objects obj with a key value"""
		k = "{}.{}".format(obj.__class__.__name__, obj.id)
		FileStorage.__objects[k] = obj

	def save(self):
		"""Serialize __objects to the JSON file"""
		j = FileStorage.__objects.items()
		new_dict = {key: new_dict.to_dict() for key, value in j}
		with open(FileStorage.__file_path, 'w') as f:
			json.dump(new_dict, f)

	def reload(self):
		"""Deserialize json file to __objects"""
		try:
			with open(FileStorage.__file_path, 'r') as f:
				new_dict = json.load(f)

				for key, value in new_dict.items():
					class_name, obj_id = key.split('.')

					class_obj = globals()[class_name]
					
					obj_instance = class_obj(**value)
					FileStorage.__objects[key] = obj_instance

		except FileNotFoundError:
			pass