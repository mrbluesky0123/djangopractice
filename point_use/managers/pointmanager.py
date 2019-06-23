from django.db import models
from django.db.models import Q

class PointManager(models.Manager):
    
    def get_point(self, mbr_id):
        try:
            point = self.filter(mbr_id=mbr_id).values_list('point_amt', flat=True)[0]
        except IndexError:
            point = 0

        return point

    def update_point(self, mbr_id, point):
        rows = self.filter(mbr_id=mbr_id).update(point_amt=point)
        if rows <= 0:
            return -1
        return rows