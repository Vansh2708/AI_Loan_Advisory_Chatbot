from django.db import models

from users.models import User
class Loan(models.Model):
    LOAN_TYPES=(('home','Home Loan'),('personal','Personal Loan'),('car','Car Loan'),('education','Education Loan')
                )
    STATUS_CHOICES=(
        ('pending','Pending'),
        ('approved','Approved'),
        ('rejected','Rejected'),
    )
    
    user=models.ForeignKey(
        User,on_delete=models.CASCADE,related_name='loans'
    )
    
    loan_type=models.CharField(
        max_length=20,
        choices=LOAN_TYPES
    )
    amount=models.FloatField()
    intrest_rate=models.FloatField(default=10)
    tenure_years=models.IntegerField()
    status=models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending'
    )
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.user.username}-{self.loan_type}"
