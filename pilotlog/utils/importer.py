import json
import logging
from abc import ABC, abstractmethod
from django.apps import apps
from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import IntegrityError, models, transaction

# Set up logging
logger = logging.getLogger(__name__)


class BaseImporter(ABC):

    @abstractmethod
    def parser(self, file_name: str):
        raise NotImplementedError

    @abstractmethod
    def format_serializer(self, data):
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
        except FileNotFoundError:
            logger.error("File not found: %s", file_name)
            raise
        except json.JSONDecodeError:
            logger.error("Error decoding JSON: %s", file_name)
            raise
        except Exception as e:
            logger.error("An error occurred: %s", e)
            raise

    def format_serializer(self, data: list):
        if not isinstance(data, list):
            raise ValueError('Only list accepted')
        if len(data) == 0:
            return None

        grouped_data = {}
        s = []
        for record in data:
            table_name = record['table'].lower()
            app_label = next((model._meta.app_label for model in apps.get_models() if model.__name__.lower() == table_name), None)
            if app_label and f"{app_label}.{table_name}" not in s:
                s.append(f"{app_label}.{table_name}")
            if app_label is not None:
                table_key = f"{app_label}.{table_name}"
                if table_key not in grouped_data:
                    grouped_data[table_key] = []
                grouped_data[table_key].append(record['meta'])
        print(s)
        return grouped_data

    def __call__(self, file_name):
        """
        to import in a fast straight forward way!
        :param file_name:
        :return:
        """
        data = self.parser(file_name)
        formatted_data = self.format_serializer(data)
        return self.persister.persist_data(formatted_data)


# Class for persisting data
class Persister(ABC):

    @abstractmethod
    def persist_data(self, data):
        pass


class JsonPersister:
    def persist_data(self, data):
        for model_path, entries in data.items():
            model = apps.get_model(model_path)
            objects_to_create = [model(**entry) for entry in entries]  # Initialize before the loop
            if objects_to_create:  # Proceed only if there are objects to create
                try:
                    with transaction.atomic():
                        model.objects.bulk_create(objects_to_create)
                    logger.info("Data import completed successfully for %s records.", len(objects_to_create))
                except Exception as e:
                    logger.error("Unexpected error persisting data for %s: %s", model_path, e)
            else:
                logger.info("No valid objects to create for %s.", model_path)
        return


class ImporterFactory:
    @staticmethod
    def get_importer(file_name: str) -> BaseImporter:
        """Factory method to get the appropriate importer based on file type."""
        file_extension = file_name.split('.')[-1].lower()

        supported_importers = {
            'json': JSONImporter(),
            # Any importer can be added later

        }

        importer = supported_importers.get(file_extension)
        if importer is None:
            raise ValueError("Unsupported file type: %s , supported types are %s", file_extension, supported_importers.keys())

        return importer
