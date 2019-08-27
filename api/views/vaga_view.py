from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination
from ..services import vaga_service
from ..serializers import vaga_serializer
from ..entities import vaga

class VagaList(APIView):
    
    def get(self, request, format=None):
        #é possivel utilizar via deslocamento ou
        #paginacao = LimitOffsetPagination()
        #numero da pagina
        paginacao = PageNumberPagination()

        vagas = vaga_service.listar_vagas()
        resultado = paginacao.paginate_queryset(vagas, request)
        serializer = vaga_serializer.VagaSerializer(resultado, context={'request': request} , many=True)

        return paginacao.get_paginated_response(serializer.data)
        #return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = vaga_serializer.VagaSerializer(data=request.data)
        
        if serializer.is_valid():
            titulo = serializer.validated_data["titulo"]
            descricao = serializer.validated_data["titulo"]
            salario = serializer.validated_data["salario"]
            local = serializer.validated_data["local"]
            quantidade = serializer.validated_data["quantidade"]
            contato = serializer.validated_data["contato"]
            tipo_contratacao = serializer.validated_data["tipo_contratacao"]

            tecnologias = serializer.validated_data["tecnologias"]

            vaga_nova = vaga.Vaga(titulo=titulo, descricao=descricao, salario=salario, local=local,
                        quantidade=quantidade, contato=contato, tipo_contratacao=tipo_contratacao,
                        tecnologias=tecnologias)
            
            vaga_service.cadastrar_vaga(vaga_nova)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class VagaDetail(APIView):
    def get(self, request, id, format=None):
        vaga = vaga_service.listar_vaga_id(id)
        serializer = vaga_serializer.VagaSerializer(vaga)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, id, format=None):
        vaga_antiga = vaga_service.listar_vaga_id(id)
        serializer = vaga_serializer.VagaSerializer(vaga_antiga, data=request.data)
        
        if serializer.is_valid():
            titulo = serializer.validated_data["titulo"]
            descricao = serializer.validated_data["titulo"]
            salario = serializer.validated_data["salario"]
            local = serializer.validated_data["local"]
            quantidade = serializer.validated_data["quantidade"]
            contato = serializer.validated_data["contato"]
            tipo_contratacao = serializer.validated_data["tipo_contratacao"]

            tecnologias = serializer.validated_data["tecnologias"]

            vaga_nova = vaga.Vaga(titulo=titulo, descricao=descricao, salario=salario, local=local,
                        quantidade=quantidade, contato=contato, tipo_contratacao=tipo_contratacao,
                        tecnologias=tecnologias)

            vaga_service.editar_vaga(vaga_antiga, vaga_nova)

            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        vaga = vaga_service.listar_vaga_id(id)
        vaga_service.remover_vaga(vaga)
        return Response(status=status.HTTP_204_NO_CONTENT)
        

