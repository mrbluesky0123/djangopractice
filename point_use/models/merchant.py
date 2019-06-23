from django.db import models
from point_use.managers.merchantmanager import MerchantManager

class Merchant(models.Model):
    
    mbrsh_pgm_id = models.CharField(max_length = 1)
    mcht_no = models.CharField(max_length = 8)
    mcht_nm = models.CharField(max_length = 40)
    biz_no = models.CharField(max_length = 10)
    mcht_fg = models.CharField(max_length = 1)
    crdt_sts = models.CharField(max_length = 20)
    cpn_clos_dy = models.CharField(max_length = 8)
    
    objects = MerchantManager()

    def __str__(self):
        return '%s, %s' % (self.mcht_no, self.crdt_sts)

    class Meta:
        app_label = 'point_use'
        db_table = 'MCT_MASTER_MST'

'''
=============================================================
| MBRSH_PGM_ID | varchar(1)  | NO   |     | NULL    |       |
| MCHT_NO      | varchar(8)  | NO   |     | NULL    |       |
| MCHT_NM      | varchar(40) | YES  |     | NULL    |       |
| BIZ_NO       | varchar(10) | YES  |     | NULL    |       |
| MCHT_FG      | varchar(1)  | YES  |     | NULL    |       |
| CRDT_STS     | varchar(2)  | YES  |     | NULL    |       |
| CPN_CLOS_DY  | varchar(8)  | YES  |     | NULL    |       |
=============================================================
'''