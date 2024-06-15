from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User

from berita.serializers import BiodataSerializer, KategoriSerializer, ArtikelSerializer
from berita.models import Kategori, Artikel
from pengguna.models import Biodata


@api_view(['GET'])
def api_author_list(request):
    user = Biodata.objects.all()
    serializer = BiodataSerializer(user, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def api_author_detail(request, id_author):
    try:
        author = Biodata.objects.get(id=id_author)
        serializer = BiodataSerializer(author, many=False)
        return Response(serializer.data)
    
    except:
        return Response({'massage:data author tidak ditemukan'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def api_kategori_list(request):
    kategori = Kategori.objects.all()
    serializer = KategoriSerializer(kategori, many=True)
    return Response(serializer.data)


@api_view(['GET','PUT'])
def api_kategori_detail(request, id_kategori):
    try:
        kategori = Kategori.objects.get(id=id_kategori)
    except:
        return Response({'massage:data kategori tidak ditemukan'}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        serializer = KategoriSerializer(kategori, many=False)
        return Response(serializer.data)
    

    elif request.method == "PUT":
        serializer = KategoriSerializer(kategori, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    else:
        pass



    
@api_view(['POST'])
def api_kategori_add(request):
    serializer = KategoriSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def api_artikel_list(request):
    key_token = "a7c9fd096f6084f1aa4c7898956c7450b8132f9b25f31d3d2104c0ea4e59abb9"

    token = request.headers.get('token')
    if token == None:
        return Response({'massage: masukkan token'}, status=status.HTTP_401_UNAUTHORIZED)
    
    if token != key_token:
    # token = Token.object.filter(token=token)
        return Response({'massage: masukkan token yang benar'}, status=status.HTTP_401_UNAUTHORIZED)
    
    artikel = Artikel.objects.all()
    serializer = ArtikelSerializer(artikel, many=True)
    data = {
        'count': artikel.count(),
        'rows': serializer.data
    }
    return Response(data)

@api_view(['GET', 'PUT', 'DELETE'])
def api_artikel_detail(request, id_artikel):
    try:
        artikel = Artikel.objects.get(id=id_artikel)
    
    except:
        return Response({'massage: data artikel tidak ditemukan'}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        serializer = ArtikelSerializer(artikel, many=False)
        return Response(serializer.data)
    
    elif request.method == "PUT":
        serializer = ArtikelSerializer(artikel, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
    elif request.method == "DELETE":
        artikel.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['POST'])
def api_artikel_add(request):
    serializer = ArtikelSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    