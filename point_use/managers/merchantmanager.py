from django.db import models
from django.db.models import Q

class MerchantManager(models.Manager):
    
    def get_merchant_status(self, mcht_no):
        try:
            crdt_sts = self.filter(mcht_no=mcht_no).values_list('crdt_sts', flat=True)[0]
        except IndexError:
            crdt_sts = None

        return crdt_sts

    def get_merchant_flag(self, mcht_no):
        try:
            mcht_fg = self.filter(mcht_no=mcht_no).values_list('mcht_fg', flat=True)[0]
        except IndexError:
            mcht_fg = None

        return mcht_fg