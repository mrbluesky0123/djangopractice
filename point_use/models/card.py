from django.db import models
from point_use.managers.cardmanager import CardManager

class Card(models.Model):
    crd_no = models.CharField(max_length = 16)
    mbr_id = models.CharField(max_length = 10)
    crd_sts = models.CharField(max_length = 20)     # normal, use_limited, ...
    crd_cd = models.CharField(max_length = 4)

    objects = CardManager()

    def __str__(self):
        return '%s, %s' % (self.mbr_id, self.crd_cd)

    class Meta:
        app_label = 'point_use'
        db_table = 'CRD_MASTER_MST'