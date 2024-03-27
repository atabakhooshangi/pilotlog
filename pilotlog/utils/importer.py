from abc import ABC, abstractmethod

from django.apps import apps

import json

# Base class for data extraction
from django.conf import settings
from django.db import IntegrityError, models


class BaseImporter(ABC):

    @abstractmethod
    def parser(self, file_name: str):
        raise NotImplementedError

    @abstractmethod
    def format_serializer(self, data):
        raise NotImplementedError

    @abstractmethod
    def do_import(self, data):
        raise NotImplementedError


# Extractor for JSON data
class JSONImporter(BaseImporter):
    JSON_BASE_DIR = settings.JSON_BASE_DIR

    def __init__(self):
        self.persister = JsonPersister()

    def parser(self, file_name: str):
        full_path = self.JSON_BASE_DIR + file_name
        try:
            with open(full_path, 'r', encoding='utf-8') as file:
                json_string = file.read()
                unescaped_json_string = json_string.encode().decode('unicode_escape')
                data = json.loads(unescaped_json_string)
            return data
        except FileNotFoundError as e:
            print("File not found:", file_name)
            raise e
        except json.JSONDecodeError as e:
            print("Error decoding JSON:", file_name)
            raise e
        except Exception as e:
            print("An error occurred:", e)
            raise e

    def format_serializer(self, data: list):
        if not isinstance(data, list):
            raise ValueError('Only list accepted')
        if len(data) == 0:
            return None

        for item in data:
            table_key = item['table']
            app_label = next((model._meta.app_label for model in apps.get_models() if model.__name__ == table_key), None)
            # meta_data = item['meta']

            # if table_key == 'Aircraft':
            #     print(table_key,app_label)
            item['table'] = f"{app_label}.{table_key}"

            # Append the meta data to the corresponding list
            # if app_label is not None:
            #     if key not in result_dict:result_dict[f"{app_label}.{table_key}"] = []
            #     result_dict[f"{app_label}.{table_key}"].append(meta_data)
        return data

    def do_import(self, formatted_data):
        return self.persister.persist_data(formatted_data)

    def __call__(self, file_name):
        """
        to import in a fast straight forward way!
        :param file_name:
        :return:
        """
        data = self.parser(file_name)
        formatted_data = self.format_serializer(data)
        return self.do_import(formatted_data)


class CSVImporter(BaseImporter):
    CSV_BASE_DIR = None

    def __init__(self):
        self.persister = CSVPersister()

    def parser(self, file_name: str):
        pass

    def format_serializer(self, data):
        pass

    def do_import(self, data):
        pass


class XMLImporter(BaseImporter):
    XML_BASE_DIR = None
    def __init__(self):
        self.persister = XmlPersister()
    def parser(self, file_name: str):
        pass

    def format_serializer(self, data):
        pass

    def do_import(self, data):
        pass


# Class for persisting data
class Persister(ABC):

    @abstractmethod
    def persist_data(self, data):
        pass


class JsonPersister(Persister):



    def persist_data(self, data):

        for i in data:
            # print(model_app)
            try:
                model:models.Model = apps.get_model(i.get('table'))
                meta_data = i.get('meta')
                model.objects.create(**meta_data)
                # bulk_models = []
                # for val in vals:
                #     bulk_models.append(model(**val))
                # model.objects.bulk_create(bulk_models)
            except IntegrityError:
                print(f'Could not load {i.get("table")}')
            except Exception as e:
                print(e)
        return 'data persisted'


class CSVPersister(Persister):
    def persist_data(self, data):
        pass


class XmlPersister(Persister):
    def persist_data(self, data):
        pass


class ImporterFactory:
    @staticmethod
    def get_importer(file_name: str) -> BaseImporter:
        # Detect the file format from the file extension
        file_extension = file_name.split('.')[-1].lower()

        supported_importers = {
            'json': JSONImporter(),
            'csv': CSVImporter(),
            'xml': XMLImporter(),
        }

        importer = supported_importers.get(file_extension)
        if importer is None:
            raise ValueError('The format is not supported yet')

        return importer
