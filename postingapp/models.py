from django.db import models

class Postal(models.Model):
    AREA_CD = models.AutoField(primary_key=True)
    DOM_CONS = models.CharField(max_length=60)
    DOM_BULK_CONS = models.CharField(max_length=60)
    COM_CONS = models.CharField(max_length=60)
    IND_CONS = models.CharField(max_length=60)
    CNG_CONS = models.CharField(max_length=60)
    OTHERS_CONS = models.CharField(max_length=60)
    TOT_CONS = models.CharField(max_length=60)
    AREA_DESCR = models.CharField(max_length=60)
    SUBZONE_DESCR = models.CharField(max_length=30)
    ZONE_DESCR =models.CharField(max_length=20)
    REGION_DESCR = models.CharField(max_length=20)
    UNIT_DESCR = models.CharField(max_length=30)
    GCV_STATION = models.CharField(max_length=20)
    GCV_S_NAME = models.CharField(max_length=40)
    PHYSICAL_SMS = models.CharField(max_length=20)
    PHYSICAL_SMS_DESCR = models.CharField(max_length=60)
    TBS = models.CharField(max_length=20)
    TBS_DESCR = models.CharField(max_length=60)
    PRS = models.CharField(max_length=20)
    PRS_DESCR = models.CharField(max_length=60)
    SYSTEM_DATE = models.CharField(max_length=60)

    class Meta:
        db_table = "postingapp"
