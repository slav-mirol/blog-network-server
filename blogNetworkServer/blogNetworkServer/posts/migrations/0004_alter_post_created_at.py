# Generated by Django 4.2.3 on 2023-07-06 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_posttag_tag_comment_id_post_delete_postcomment_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(null=True),
        ),
    ]
