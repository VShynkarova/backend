from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasksapp', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Task',
        ),
    ]
