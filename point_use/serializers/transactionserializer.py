from rest_framework import serializers
from point_use.models import Transaction

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = (
            'ans_cd', 
            'ans_msg', 
            'aprv_dy', 
            'aprv_tm', 
            'rep_aprv_no', 
            'deal_amt', 
            'rmn_pnt'
        )