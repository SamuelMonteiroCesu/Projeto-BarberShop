from django.db import models

class Procedure(models.Model):
    # 'procedure_id', 'name', ''active', 'time', 'price' 
    procedure_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    active = models.BooleanField(default=True)
    time = models.IntegerField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
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
    discount = models.FloatField(blank=True, null=True)
    tax = models.FloatField(blank=True, null=True)
    def __str__(self):
        return self.name




class BugBounty(models.Model):
    # 'bug_id', 'name', 'content', 'solved', 'created_at', 'description'
    bug_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    solved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    description = models.TextField()
    #DESCRICAO
    def __str__(self):
        return self.name
















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
#first_name, last_name, email, username, password, is_staff, is_active, is_superuser
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    username = models.CharField(unique=True, max_length=150)
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.first_name)



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





class Appointment(models.Model):
    #['client','professional','status','procedure','payment' ]
    client = models.ForeignKey(AuthUser, models.DO_NOTHING, related_name="clientss")
    professional = models.ForeignKey(AuthUser, models.DO_NOTHING, related_name="professionalss")
    status = models.ForeignKey(Status, models.DO_NOTHING)
    procedure = models.ForeignKey(Procedure, models.DO_NOTHING)
    payment = models.ForeignKey(Payment, models.DO_NOTHING)
    appdate = models.CharField(max_length=10)#format dd/mm/yyyy
    apphour = models.CharField(max_length=5)#format hh:mm
    total = models.IntegerField(blank = True, null = True)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return str(self.apphour)

    def get_apphour(self):
        return self.__apphour


class Schedule(models.Model):
    professional = models.ForeignKey(AuthUser, models.DO_NOTHING)
    begin = models.CharField(max_length=5)#format hh:mm
    end = models.CharField(max_length=5)#format hh:mm
    interval = models.IntegerField() #in minutes ex 10
    weekday = models.IntegerField() #0 = monday
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return "Begin: " + self.begin +"\nEnd: " + self.end+"\nInterval: " + str(self.interval)

class DayOff (models.Model):
    professional = models.ForeignKey(AuthUser, models.DO_NOTHING, blank = True, null = True)
    daydate = models.CharField(max_length=10)#format dd/mm/yyyy
    reason = models.CharField(max_length=255)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now=True)
    
