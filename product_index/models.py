# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from ckeditor.fields import RichTextField


class App(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'app'


class Groups(models.Model):
    app = models.ForeignKey(App, related_name='groups', on_delete=models.CASCADE)
    name = models.CharField(max_length=35)
    description = models.TextField()
    type = models.IntegerField(choices=((1, 'Product'), (2, 'Disease')))
    image = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'groups'


class Category(models.Model):
    app = models.ForeignKey(App, models.DO_NOTHING)
    groups = models.ForeignKey(Groups, related_name='categories', on_delete=models.CASCADE)
    type = models.IntegerField(choices=[(1, 'Product'), (2, 'Disease')])
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'category'


class Disease(models.Model):
    app = models.ForeignKey(App, models.DO_NOTHING)
    groups = models.ForeignKey(Groups, models.DO_NOTHING, blank=True, null=True)
    category = models.ForeignKey(Category, related_name='diseases', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = RichTextField(blank=True)
    sub_title = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'disease'


class Product(models.Model):
    app = models.ForeignKey(App, models.DO_NOTHING)
    groups = models.ForeignKey(Groups, models.DO_NOTHING, blank=True, null=True)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    sub_title = models.CharField(max_length=255, blank=True, null=True)
    description = RichTextField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'product'


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
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

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
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

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


class FosUserGroup(models.Model):
    name = models.CharField(unique=True, max_length=180)
    roles = models.TextField()

    class Meta:
        managed = False
        db_table = 'fos_user_group'


class FosUserUser(models.Model):
    username = models.CharField(max_length=180)
    username_canonical = models.CharField(unique=True, max_length=180)
    email = models.CharField(max_length=180)
    email_canonical = models.CharField(unique=True, max_length=180)
    enabled = models.IntegerField()
    salt = models.CharField(max_length=255, blank=True, null=True)
    password = models.CharField(max_length=255)
    last_login = models.DateTimeField(blank=True, null=True)
    confirmation_token = models.CharField(unique=True, max_length=180, blank=True, null=True)
    password_requested_at = models.DateTimeField(blank=True, null=True)
    roles = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    date_of_birth = models.DateTimeField(blank=True, null=True)
    firstname = models.CharField(max_length=64, blank=True, null=True)
    lastname = models.CharField(max_length=64, blank=True, null=True)
    website = models.CharField(max_length=64, blank=True, null=True)
    biography = models.CharField(max_length=1000, blank=True, null=True)
    gender = models.CharField(max_length=1, blank=True, null=True)
    locale = models.CharField(max_length=8, blank=True, null=True)
    timezone = models.CharField(max_length=64, blank=True, null=True)
    phone = models.CharField(max_length=64, blank=True, null=True)
    facebook_uid = models.CharField(max_length=255, blank=True, null=True)
    facebook_name = models.CharField(max_length=255, blank=True, null=True)
    facebook_data = models.TextField(blank=True, null=True)
    twitter_uid = models.CharField(max_length=255, blank=True, null=True)
    twitter_name = models.CharField(max_length=255, blank=True, null=True)
    twitter_data = models.TextField(blank=True, null=True)
    gplus_uid = models.CharField(max_length=255, blank=True, null=True)
    gplus_name = models.CharField(max_length=255, blank=True, null=True)
    gplus_data = models.TextField(blank=True, null=True)
    token = models.CharField(max_length=255, blank=True, null=True)
    two_step_code = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fos_user_user'


class FosUserUserGroup(models.Model):
    user = models.OneToOneField('User', models.DO_NOTHING, primary_key=True)
    group = models.ForeignKey('UserGroup', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'fos_user_user_group'
        unique_together = (('user', 'group'),)


class MediaGallery(models.Model):
    name = models.CharField(max_length=255)
    context = models.CharField(max_length=64)
    default_format = models.CharField(max_length=255)
    enabled = models.IntegerField()
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'media__gallery'


class MediaGalleryMedia(models.Model):
    position = models.IntegerField()
    enabled = models.IntegerField()
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'media__gallery_media'


class MediaMedia(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    enabled = models.IntegerField()
    provider_name = models.CharField(max_length=255)
    provider_status = models.IntegerField()
    provider_reference = models.CharField(max_length=255)
    provider_metadata = models.TextField(blank=True, null=True)  # This field type is a guess.
    width = models.IntegerField(blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
    length = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    content_type = models.CharField(max_length=255, blank=True, null=True)
    content_size = models.IntegerField(blank=True, null=True)
    copyright = models.CharField(max_length=255, blank=True, null=True)
    author_name = models.CharField(max_length=255, blank=True, null=True)
    context = models.CharField(max_length=64, blank=True, null=True)
    cdn_is_flushable = models.IntegerField(blank=True, null=True)
    cdn_flush_identifier = models.CharField(max_length=64, blank=True, null=True)
    cdn_flush_at = models.DateTimeField(blank=True, null=True)
    cdn_status = models.IntegerField(blank=True, null=True)
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'media__media'


class User(models.Model):
    email = models.CharField(max_length=180)
    roles = models.TextField()
    password = models.CharField(max_length=255)
    username = models.CharField(max_length=180)
    username_canonical = models.CharField(unique=True, max_length=180)
    email_canonical = models.CharField(unique=True, max_length=180)
    enabled = models.IntegerField()
    salt = models.CharField(max_length=255, blank=True, null=True)
    last_login = models.DateTimeField(blank=True, null=True)
    confirmation_token = models.CharField(unique=True, max_length=180, blank=True, null=True)
    password_requested_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'


class UserGroup(models.Model):
    name = models.CharField(unique=True, max_length=180)
    roles = models.TextField()

    class Meta:
        managed = False
        db_table = 'user_group'
