from django.shortcuts import render
from escola.models import Aluno, Curso, Matricula
from rest_framework import viewsets, generics 
from escola.serializer import(
                               AlunoSerializer, 
                               CursoSerializer, 
                               MatriculaSerializer, 
                               ListaMatriculaAlunoSerializer,
                               ListaAlunosMatriculadosSerializer
                             )
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated  

class AlunosViewSet(viewsets.ModelViewSet):
	queryset = Aluno.objects.all()
	serializer_class  = AlunoSerializer
	authentication_classes = [BasicAuthentication]
	permission_classes = [IsAuthenticated]

class CursosViewSet(viewsets.ModelViewSet):
	queryset = Curso.objects.all()
	serializer_class  = CursoSerializer
	authentication_classes = [BasicAuthentication]
	permission_classes = [IsAuthenticated]

class MatriculaViewSet(viewsets.ModelViewSet):
	queryset = Matricula.objects.all()
	serializer_class = MatriculaSerializer
	authentication_classes = [BasicAuthentication]
	permission_classes = [IsAuthenticated]

class ListaMatriculaAluno(generics.ListAPIView):
	def get_queryset(self):
		queryset = Matricula.objects.filter(aluno_id=self.kwargs['pk'])
		return queryset
	serializer_class = ListaMatriculaAlunoSerializer
	authentication_classes = [BasicAuthentication]
	permission_classes = [IsAuthenticated]


class ListaAlunoMatriculados(generics.ListAPIView):
	"""Listando alunos matriculados em um curso"""
	def get_queryset(self):
		queryset = Matricula.objects.filter(curso_id=self.kwargs['pk'])
		return queryset
	serializer_class =  ListaAlunosMatriculadosSerializer
	authentication_classes = [BasicAuthentication]
	permission_classes = [IsAuthenticated]

	
