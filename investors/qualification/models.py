from django.db import models


class Investor(models.Model):
    firstname = models.CharField("Имя", max_length=100)
    lastname = models.CharField("Фамилия", max_length=100)
    patronymic = models.CharField("Отчество", max_length=100)
    qualification_status = models.CharField(null=False, choices = (
            ('Identified', 'Identified'),
            ('Agreed', 'Agreed'),
            ('Qualificated', 'Qualificated'),
            ('Refused to qualify', 'Refused to qualify'),
        ),
        max_length=50)

    def __str__(self):
        return 'Инвестор: %s %s %s' % (self.firstname, self.lastname, self.patronymic)


class Passport(models.Model):
    firstname = models.CharField("Имя", max_length=100, null=True)
    lastname = models.CharField("Фамилия", max_length=100, null=True)
    patronymic = models.CharField("Отчество", max_length=100, null=True)
    birth_date = models.DateField(null=True)
    number = models.IntegerField("Номер", null=True)
    series = models.IntegerField("Серия", null=True)
    issued_by = models.CharField("Кем выдан", max_length=100, null=True)
    date_of_issue = models.DateField(null=True)
    registration_address = models.CharField("Адрес регистрации", max_length=100, null=True)
    department_code = models.CharField("Код подразделения", max_length=10, null=True)
    file = models.FileField(upload_to='media/', null=True)
    investor = models.ForeignKey(Investor, on_delete=models.PROTECT, related_name="passports", null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)


class Document(models.Model):
    name = models.CharField("Название", max_length=100)
    file = models.FileField(upload_to='media/', null=True)
    investor = models.ForeignKey(Investor, on_delete=models.PROTECT, related_name="documents")
    created_at = models.DateTimeField(auto_now_add=True)
