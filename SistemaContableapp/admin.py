from django.contrib import admin
from .models import Project, Task,User,Advance
from .models import *
# Register your models here.
admin.site.register(Project)
admin.site.register(Task)
admin.site.register(User)
#admin.site.register(Bank_Account)
admin.site.register(Advance)
admin.site.register(Requisition)
admin.site.register(Legalization)
admin.site.register(Expense)
admin.site.register(Expense_balance)
admin.site.register(Charge_account)
admin.site.register(Exterior_payment)
admin.site.register(Following)
admin.site.register(Audit)