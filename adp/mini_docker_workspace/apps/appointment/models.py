from django.db import models
from django.contrib.auth.models import User
import django.utils.timezone as timezone

# Create your models here.


class UserRole(models.Model):
    """
    user role( docker or patient）
    """
    _status_dict = ((0, 'patient'), (1, 'docker'))
    id = models.AutoField(max_length=10, primary_key=True)
    user_key = models.ForeignKey(User, null=True, blank=True, to_field="id", on_delete=models.CASCADE)
    role = models.IntegerField(choices=_status_dict, default=0)


class AppointmentStatus(models.Model):
    """
    appointment status, include cancelled, finished, toBegin, expired
    (取消，完成，待开始，过期失效）
    """
    id = models.AutoField(max_length=10, primary_key=True)
    message = models.CharField('patient feedback', max_length=128, null=True)


class AppointmentRecord(models.Model):
    """
    patient appointment record
    """
    id = models.AutoField(max_length=10, primary_key=True)
    patient = models.ForeignKey(User, null=True, blank=True, to_field="id", on_delete=models.CASCADE,
                                related_name="patient")
    docker = models.ForeignKey(User, null=True, blank=True, to_field="id", on_delete=models.CASCADE,
                               related_name="docker")
    start_time = models.DateTimeField('start time', max_length=6, null=False)
    end_time = models.DateTimeField('end time', max_length=6, null=False)
    load_time = models.DateTimeField('appointment time', null=False, default=timezone.now)
    operator_user = models.ForeignKey(User, null=True, blank=True, to_field="id", on_delete=models.CASCADE,
                                      related_name="operator")
    status = models.ForeignKey(AppointmentStatus, null=True, blank=True, to_field="id", on_delete=models.CASCADE,
                               related_name="status")


class CaseRecord(models.Model):
    """
    record patient case in each appointment
    """
    id = models.AutoField(max_length=10, primary_key=True)
    appoint_id = models.ForeignKey(AppointmentRecord, null=True, blank=True, to_field="id", on_delete=models.CASCADE,
                                   related_name="appoint")
    docker_feedback = models.CharField('docker feedback', max_length=4096, null=True)
    patient_feedback = models.CharField('patient feedback', max_length=4096, null=True)