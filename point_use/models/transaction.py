from django.db import models

class Transaction(models.Model):
    ans_cd = models.CharField(max_length = 4, default = '')
    ans_msg = models.CharField(max_length = 20, default = '')
    aprv_dy = models.CharField(max_length = 8)
    aprv_tm = models.CharField(max_length = 6)
    rep_aprv_no = models.CharField(max_length=9)
    deal_amt = models.IntegerField()
    rmn_pnt = models.IntegerField(default=0)

    class Meta:
        app_label = 'point_use'
        db_table = 'APR_DEALTR_TRN'