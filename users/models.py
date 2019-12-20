from django.db.models import Model, CharField, TextField, FloatField, \
    DateTimeField, ForeignKey, CASCADE


class User(Model):
    first_name = CharField(verbose_name='First name', max_length=50)
    middle_name = CharField(verbose_name='Middle name', max_length=50)
    last_name = CharField(verbose_name='Last name', max_length=50)
    phone = CharField(verbose_name='Phone', max_length=50)


class Service(Model):
    user = ForeignKey(User, verbose_name='User id', on_delete=CASCADE)
    car_model = CharField(verbose_name='Car model', max_length=100)
    description = TextField(verbose_name='Description')
    cost = FloatField(verbose_name='Cost')
    datetime = DateTimeField(verbose_name='Datetime', auto_now=True)
