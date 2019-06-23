from django.db import models
from point_use.managers.membermanager import MemberManager

class Member(models.Model):
    STATUS = (
        ('A', 'available member'),
        ('R', 'retired member'),
    )
    mbr_id = models.CharField(max_length = 10)
    name = models.CharField(max_length = 30)
    mdn_no = models.CharField(max_length = 12)
    birthday = models.CharField(max_length = 8)
    mbr_sts = models.CharField(max_length = 10, choices=STATUS)    # normal, retired, ...
    last_sales_date = models.DateTimeField()

    objects = MemberManager()

    def __str__(self):
        return '%s, %s, %s' % (self.mbr_id, self.name, self.mdn_no)

    class Meta:
        app_label = 'point_use'
        db_table = 'MBR_MASTER_MST'