from django.db import models
from point_use.managers.pointmanager import PointManager

class Point(models.Model):
    mbr_id = models.CharField(max_length = 10)
    point_knd_cd = models.CharField(max_length = 3)
    point_amt = models.IntegerField()

    objects = PointManager()

    def __str__(self):
        return '%s, %s, %s' % (self.mbr_id, self.point_knd_cd, self.point_amt)

    class Meta:
        app_label = 'point_use'
        db_table = 'MBR_MEMPNT_TRN'