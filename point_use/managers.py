from django.db import models
from django.db.models import Q

class MemberManager(models.Manager):
    
    def get_member(self, status):
        return self.filter(mbr_sts=status)

    def update_member_mdn_no(self, mbr_id, mdn_no):
        return self.filter(mbr_id=mbr_id).update(mdn_no=mdn_no)