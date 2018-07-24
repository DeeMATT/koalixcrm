# -*- coding: utf-8 -*-
from rest_framework import viewsets
from koalixcrm.crm.reporting.task import Task, TaskSerializer
from koalixcrm.crm.reporting.taskstatus import TaskStatus, TaskStatusJSONSerializer
from koalixcrm.crm.documents.contract import Contract, ContractJSONSerializer
from koalixcrm.crm.reporting.project import Project, ProjectJSONSerializer
from rest_framework_xml.renderers import XMLRenderer
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from koalixcrm.crm.views.renderer import PDFRenderer


class TaskAsJSON(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows users to be viewed.
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    renderer_classes = (BrowsableAPIRenderer, XMLRenderer, JSONRenderer, PDFRenderer)
    filter_fields = ('project',)
    file_name = "this_is_the_TaskList.xml"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(TaskAsJSON, self).dispatch(*args, **kwargs)


class ContractAsJSON(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows users to be viewed.
    """
    queryset = Contract.objects.all()
    serializer_class = ContractJSONSerializer
    renderer_classes = (BrowsableAPIRenderer, XMLRenderer, JSONRenderer)

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ContractAsJSON, self).dispatch(*args, **kwargs)


class TaskStatusAsJSON(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows users to be viewed.
    """
    queryset = TaskStatus.objects.all()
    serializer_class = TaskStatusJSONSerializer
    renderer_classes = (BrowsableAPIRenderer, XMLRenderer, JSONRenderer)

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(TaskStatusAsJSON, self).dispatch(*args, **kwargs)


class ProjectAsJSON(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows users to be viewed.
    """
    queryset = Project.objects.all()
    serializer_class = ProjectJSONSerializer
    renderer_classes = (BrowsableAPIRenderer, XMLRenderer, JSONRenderer, PDFRenderer)
    file_name = "this_is_the_ProjectList.xml"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ProjectAsJSON, self).dispatch(*args, **kwargs)
