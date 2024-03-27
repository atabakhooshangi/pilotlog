from django.conf import settings

from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK
from rest_framework.viewsets import GenericViewSet

from pilotlog.utils.importer import ImporterFactory


class ImportExportAPIView(

    GenericViewSet
):
    permission_classes = [AllowAny]

    @action(methods=["GET"], detail=False)
    def importing(self, request, *args, **kwargs):
        importer = ImporterFactory.get_importer('pilotlog_mcc.json')
        # Can get called by caller method of the importer for a straight forward usage
        #   importer('pilotlog_mcc.json')

        data = importer.parser('pilotlog_mcc.json')
        formatted_data = importer.format_serializer(data)
        importer.do_import(formatted_data)
        return Response({"message": "Done"}, HTTP_200_OK)
