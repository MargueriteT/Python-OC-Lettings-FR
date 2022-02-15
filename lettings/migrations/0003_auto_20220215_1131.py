# Generated by Django 3.0 on 2022-02-15 10:31

from django.db import migrations, models


def update_contentypes(apps, schema_editor):
    """
    Updates content types.
    We want to have the same content type id, when the model is moved.
    """
    ContentType = apps.get_model('contenttypes', 'ContentType')
    db_alias = schema_editor.connection.alias
    # Move the ParentModel to app1
    qs = ContentType.objects.using(db_alias).filter(
        app_label='oc_lettings_site', model='Letting')
    qs.update(app_label='lettings')


def update_contentypes_reverse(apps, schema_editor):
    """
    Reverts changes in content types.
    """
    ContentType = apps.get_model('contenttypes', 'ContentType')
    db_alias = schema_editor.connection.alias
    # Move the TrackingAlert model to tracking
    qs = ContentType.objects.using(db_alias).filter(
        app_label='oc_lettings_site', model='Letting')
    qs.update(app_label='lettings')


class Migration(migrations.Migration):

    dependencies = [
        ('lettings', '0002_auto_20220215_1130'),
        ('oc_lettings_site', '0005_auto_20220215_1130')

    ]

    state_operations = [
        migrations.CreateModel(
            name='Letting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True,
                                        serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('address', models.OneToOneField(
                    on_delete=models.deletion.CASCADE, to='lettings.Address'))

            ],
        ),

    ]
    database_operations = [
        migrations.RunPython(update_contentypes, update_contentypes_reverse),
    ]
    operations = [
        migrations.SeparateDatabaseAndState(
            state_operations=state_operations,
            database_operations=database_operations
        ),
    ]