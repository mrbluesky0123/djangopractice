from django.db import models
from django.db.models import Q

class CardManager(models.Manager):
    
    def get_card_status(self, crd_no):
        try:
            crd_sts = self.filter(crd_no=crd_no).values_list('crd_sts', flat=True)[0]
        except IndexError:
            crd_sts = None

        return crd_sts

    def get_mbr_id_by_crd_no(self, crd_no):
        try:
            mbr_id = self.filter(crd_no=crd_no).values_list('mbr_id', flat=True)[0]
        except:
            mbr_id = None

        return mbr_id