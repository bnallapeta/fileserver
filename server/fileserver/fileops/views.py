# from posix import ST_NOATIME
from fileops.models import Files
from fileops.serializers import FilesSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import BrowsableAPIRenderer, JSONRenderer, HTMLFormRenderer

from fileserver.settings import MEDIA_ROOT
import os
import collections


class FilesList(APIView):

    serializer_class = FilesSerializer
    renderer_classes = (BrowsableAPIRenderer, JSONRenderer, HTMLFormRenderer)

    def get(self, request, format=None):
        files = Files.objects.all()
        serializer = FilesSerializer(files, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = FilesSerializer(data=request.data)

        filename_to_be_added = str(request.FILES['fs_file'])

        try:
            file_to_be_added = Files.objects.filter(fs_file=filename_to_be_added)
        except:
            file_to_be_added = None

        if file_to_be_added is None:
            return Response({'message': 'Something went wrong. Please try again'}, status=status.HTTP_400_BAD_REQUEST)

        if file_to_be_added.exists() == False:
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response({'Response from the server': 'File with the same name already exists!'}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, format=None):
        serializer = FilesSerializer(data=request.data)

        #Get content from user uploaded file
        filename_to_be_added = str(request.FILES['fs_file'])
        file_from_user = request.FILES['fs_file'].read()
        data = ""
        for char in file_from_user:
            data = data + chr(char)

        content_from_user_file = []
        content_from_user_file.append(data.split(" "))

        #Get content from the file on the server
        filename_from_server = os.path.join(MEDIA_ROOT, filename_to_be_added)

        file_from_server = open(filename_from_server, 'r')
        content_from_server_file = []
        for i in file_from_server.readlines():
            content_from_server_file.append(i.strip().split(" "))
        file_from_server.close()


        #Check if file with same name exists 
        try:
            file_to_be_added = Files.objects.filter(fs_file=filename_to_be_added)
        #except catches any unexpected error encountered while running the above query
        except:
            file_to_be_added = None            

        #If unexpected error is encountered, then return the below message
        if file_to_be_added is None:
            return Response({'Response from the server': 'Something went wrong. Please try again'}, status=status.HTTP_400_BAD_REQUEST)

        #If file does not exist, then create a new file and add the content
        if file_to_be_added.exists() == False:
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)

        #If file exists, compare the content inside each file; based on the result, update the file on the server or return a message that the file and the contents are same
        if content_from_user_file == content_from_server_file:
            return Response({'message': 'File with the same name and content already exists!'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            file_to_be_deleted = Files.objects.get(fs_file=filename_to_be_added)
            file_to_be_deleted.delete()
            file_path = os.path.join(MEDIA_ROOT, filename_to_be_added)

            os.remove(file_path) 
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)                           

    def delete(self, request, format=None):
        filename_to_be_deleted = request.GET.get('fs_file','')
        
        try:
            file_to_be_deleted = Files.objects.get(fs_file=filename_to_be_deleted)
        except:
            file_to_be_deleted = None
        
        try:
            file_to_be_deleted.delete()
            file_path = os.path.join(MEDIA_ROOT, filename_to_be_deleted)
            
            os.remove(file_path)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except:
            return Response({'Response from the server': 'File cannot be deleted!'}, status=status.HTTP_400_BAD_REQUEST)


class FilesDetail(APIView):
    def get_object(self, pk):
        try:
            return Files.objects.get(pk=pk)
        except Files.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        files = self.get_object(pk)
        serializer = FilesSerializer(files)
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        files = self.get_object(pk)
        files.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class FilesWordCount(APIView):
    def get(self, request, format=None):
        files = Files.objects.all()
        content_from_file = []
        list_of_words = []
        for file in files:
            file_name = str(file.fs_file)
            file_path = os.path.join(MEDIA_ROOT, file_name)
            print(file_path)

            with open(file_path, 'r') as f:
                for i in f.readlines():
                    content_from_file.append(i.strip().split(" "))

        for li in content_from_file:
            for sl in li:
                list_of_words.append(sl)

        return Response({'Total number of words in all the files is': len(list_of_words)}, status=status.HTTP_200_OK)

class FilesFreqWordCount(APIView):
    def get(self, request, format=None):
        
        #Parsing the Params from request
        if request.GET.get('order',''):
            order_val = request.GET.get('order','')
        else:
            order_val = 'asc'

        #Get list of words in all files and store it into list_of_words array
        files = Files.objects.all()
        content_from_file = []
        list_of_words = []
        
        for file in files:
            file_name = str(file.fs_file)            
            file_path = os.path.join(MEDIA_ROOT, file_name)

            with open(file_path, 'r') as f:
                for i in f.readlines():
                    content_from_file.append(i.strip().split(" "))

        for li in content_from_file:
            for sl in li:
                list_of_words.append(sl)

        occurrences = collections.Counter(list_of_words)

        fw=[]
        if order_val == 'dsc':
            fw = occurrences.most_common()[:-11:-1]

        else:
            fw = occurrences.most_common(10)

        return Response({'Here are the freq words from all the files: ': fw}, status=status.HTTP_200_OK)        