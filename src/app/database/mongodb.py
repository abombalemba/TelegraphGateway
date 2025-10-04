import pymongo


class MongoDB:
	connection = 'mongodb://localhost:27017/'

	def __init__(self) -> None:
		self.client = None
		self.database = None

	def connect(self) -> None:
		try:
			self.client = pymongo.MongoClient(self.connection)
			self.database = self.client['telegraph_gateway']

		except Exception as ex:
			print(ex)

	def close(self) -> None:
		try:
			if self.client:
				self.client.close()

				self.client = None
				self.database = None

		except Exception as ex:
			print(ex)

	def is_connected(self) -> bool:
		try:
			if self.client:
				self.client.admin.command('ping')
				return True
			return False
		except Exception as ex:
			return False


mongo = MongoDB()
mongo.connect()
print(mongo.is_connected())
mongo.close()
print(mongo.is_connected())

