# Generated by Django 3.2 on 2021-04-19 13:00

import tiptap.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("tiptap", "0002_alter_note_content"),
    ]

    operations = [
        migrations.AddField(
            model_name="note",
            name="blueprint",
            field=tiptap.fields.TipTapTextField(null=True),
        ),
    ]