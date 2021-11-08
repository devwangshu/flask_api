import json
import traceback
from pymongo import MongoClient
from scripts.constants import app_configurations


class MongoUtility(object):
    def __init__(self):
        try:
            self.db_init_flag = 0
            self.__mongo_OBJ__ = MongoClient(
                host="192.168.0.210",
                port=27017,
                # username=db_details["user_name"],
                # password=db_details["password"]
            )
        except Exception as e:
            raise Exception(str(e))

    def insert_one(self, json_data, database_name, collection_name):
        try:
            mongo_response = self.__mongo_OBJ__[database_name][collection_name].insert_one(json_data)
            return mongo_response.inserted_id
        except Exception as e:
            traceback.print_exc()
            raise Exception(str(e))

    def insert_many(self, json_data, collection_name, database_name):
        try:
            mongo_response = self.__mongo_OBJ__[database_name][collection_name].insert_many(json_data)
            json_mongo_response_object = json.loads(json.dumps(mongo_response))
            return json_mongo_response_object
        except Exception as e:
            traceback.print_exc()
            raise Exception(str(e))

    def read(self, json_data, database_name, collection_name):
        try:
            db = self.__mongo_OBJ__[database_name]
            mongo_response = db[collection_name].find(json_data)
            return mongo_response
        except Exception as e:
            traceback.print_exc()
            raise Exception(str(e))

    def read_without_inputjson(self, database_name, collection_name):
        try:
            db = self.__mongo_OBJ__[database_name]
            mongo_response = db[collection_name].find()
            return mongo_response
        except Exception as e:
            traceback.print_exc()
            raise Exception(str(e))

    def find_with_limit(self, json_data, database_name, collection_name):
        try:
            database_connection = self.__mongo_OBJ__[database_name]
            mongo_response = database_connection[collection_name].find(json_data)
            mongo_response1 = mongo_response.limit(1)
            return mongo_response1
        except Exception as e:
            traceback.print_exc()
            raise Exception(str(e))

    def find_with_condition(self, json_data, database_name, collection_name):
        try:
            database_connection = self.__mongo_OBJ__[database_name]
            mongo_response = database_connection[collection_name].find(json_data)
            return mongo_response
        except Exception as e:
            traceback.print_exc()
            raise Exception(str(e))

    def remove(self, json_data, database_name, collection_name):
        try:
            database_connection = self.__mongo_OBJ__[database_name]
            database_connection[collection_name].remove(json_data)
            return "success"
        except Exception as e:
            traceback.print_exc()
            raise Exception(str(e))

    def update_one(self, condition, json_data, database_name, collection_name):
        try:
            database_connection = self.__mongo_OBJ__[database_name]
            database_connection[collection_name].update_one(condition, {"$set": json_data})
            return "success"
        except Exception as e:
            traceback.print_exc()
            raise Exception(str(e))

    def update(self, condition, json_data, database_name, collection_name):
        try:
            database_connection = self.__mongo_OBJ__[database_name]
            database_connection[collection_name].update_one(condition, {"$set": json_data})
            return "success"
        except Exception as e:
            traceback.print_exc()
            raise Exception(str(e))

    def find_with_keyword(self, keyword, database_name, collection_name):
        try:
            database_connection = self.__mongo_OBJ__[database_name]
            mongo_response = database_connection[collection_name].find({}, {keyword: 1})
            return mongo_response
        except Exception as e:
            traceback.print_exc()
            raise Exception(str(e))

    def find_with_multiple_keyword(self, keyword1, keyword2, keyword3, keyword4, keyword5, database_name,
                                   collection_name):
        try:
            database_connection = self.__mongo_OBJ__[database_name]
            mongo_response = database_connection[collection_name].find({}, {keyword1: 1, keyword2: 1,
                                                                            keyword3: 1, keyword4: 1, keyword5: 1})
            return mongo_response
        except Exception as e:
            traceback.print_exc()
            raise Exception(str(e))

    def aggregate_query(self, json_data, database_name, collection_name):
        try:
            database_connection = self.__mongo_OBJ__[database_name]
            mongo_response = database_connection[collection_name].aggregate(json_data)
            return mongo_response
        except Exception as e:
            traceback.print_exc()
            raise Exception(str(e))

    def delete_many(self, json_data, database_name, collection_name):
        try:
            database_connection = self.__mongo_OBJ__[database_name]
            mongo_response = database_connection[collection_name].delete_many(json_data)
            return mongo_response
        except Exception as e:
            traceback.print_exc()
            raise Exception(str(e))

    def sort_records(self, field_name, database_name, collection_name, limit, query=None):
        try:
            database_connection = self.__mongo_OBJ__[database_name]
            if query is None:
                monogo_response = database_connection[collection_name].find().sort([(field_name, 1)]).limit(limit)
            else:
                monogo_response = database_connection[collection_name].find(query).sort([(field_name, 1)]).limit(limit)
            return monogo_response
        except Exception as e:
            traceback.print_exc()
            raise Exception(str(e))

    def skip_and_limit(self, database_name, collection_name, sort_field, skip_count, limit_count):
        try:
            database_connection = self.__mongo_OBJ__[database_name]
            mongo_response = database_connection[collection_name].find().sort([(sort_field, -1)]).skip(
                skip_count).limit(limit_count)
            return mongo_response
        except Exception as e:
            traceback.print_exc()
            raise Exception(str(e))

    def find_with_skip_and_limit_and_sort(self, json_data, database_name, collection_name, sort_field, skip_count,
                                          limit_count):
        try:
            database_connection = self.__mongo_OBJ__[database_name]
            mongo_response = database_connection[collection_name].find(json_data).sort([(sort_field, -1)]).skip(
                skip_count).limit(limit_count)
            return mongo_response
        except Exception as e:
            traceback.print_exc()
            raise Exception(str(e))

    def close_connection(self):
        try:
            if self.__mongo_OBJ__ is not None:
                self.__mongo_OBJ__.close()
        except Exception as e:
            raise Exception(str(e))
