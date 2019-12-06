# from django.db import models
# #
# #
# # # Create your models here.

# #
# #
# # class Product_Backlog_Item(models.Model):
# #     id_name = models.CharField(max_length=20, unique=True)
# #     title = models.CharField(max_length=200)
# #     detail = models.CharField(max_length=1000)
# #     story_point = models.DecimalField(max_digits=3, decimal_places=0)
# #     cumulative_story_point = models.DecimalField(max_digits=4, decimal_places=0)
# #     status = models.CharField(max_length=50)
# #     priority = models.DecimalField(max_digits=2, decimal_places=0)
# #
# #     def __str__(self):
# #         return self.id_name