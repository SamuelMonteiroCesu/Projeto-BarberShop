from django.db import models


class Procedure(models.Model):
    # 'procedure_id', 'name', ''active', 'time', 'price' 
    procedure_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    active = models.BooleanField(default=True)
    time = models.IntegerField()
    price = models.FloatField()
    #DESCRICAO
    def __str__(self):
        return self.name
    


class Status(models.Model):
    status_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    active = models.BooleanField(default=True)
    def __str__(self):
        return self.name

class Payment(models.Model):
    # 'payment_id', 'name', 'active', 'discount','tax'
    payment_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    active = models.BooleanField(default=True)
    discount = models.FloatField()
    tax = models.FloatField()
    def __str__(self):
        return self.name


class Company(models.Model):
    # 'company_id', 'name', 'doc', 'zipcode', 'adress', 'number', 
    # 'complement', 'district', 'city', 'state', 'phone', 'cellphone', 'active'
    company_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    doc = models.CharField(max_length=14)
    zipcode = models.CharField(max_length=9)
    adress = models.CharField(max_length=100)
    number = models.CharField(max_length=10)
    complement = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    cellphone = models.CharField(max_length=20)
    active = models.BooleanField(default=True)
    def __str__(self):
        return self.name


class Employee(models.Model):
    # 'employee_id', 'company_fk', 'name', 'email', 'password', 'doc', 'phone', 'cellphone',
    # 'active', 'obs'
    employee_id = models.AutoField(primary_key=True)
    company_fk = models.ForeignKey(Company, models.DO_NOTHING)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    doc = models.CharField(max_length=11)
    phone = models.CharField(max_length=20)
    cellphone = models.CharField(max_length=20)
    active = models.BooleanField(default=True)
    obs = models.TextField()
    def __str__(self):
        return self.name


class Client(models.Model):
     # 'client_id', 'company_fk', 'name', 'email', 'birthday', 'dataJoined', 'doc', 'phone', 'cellphone',
     # 'zipcode', 'adress', 'number', 'complement', 'district', 'city', 'state', 'active', 'obs'
    client_id = models.AutoField(primary_key=True)
    company_fk = models.ForeignKey(Company, models.DO_NOTHING)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    birthday = models.DateField()
    dateJoined = models.DateTimeField(auto_now=True)
    doc = models.CharField(max_length=11)
    phone = models.CharField(max_length=20)
    cellphone = models.CharField(max_length=20)
    zipcode = models.CharField(max_length=9)
    adress = models.CharField(max_length=100)
    number = models.CharField(max_length=10)
    complement = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    active = models.BooleanField(default=True)
    obs = models.TextField()
    def __str__(self):
        return self.name























'''


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    first_name = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    action_flag = models.PositiveSmallIntegerField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
'''
