# Generated by Django 4.2.2 on 2023-06-16 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0096_check_start_kw_alter_channel_kind"),
    ]

    operations = [
        migrations.AlterField(
            model_name="channel",
            name="kind",
            field=models.CharField(
                choices=[
                    ("apprise", "Apprise"),
                    ("call", "Phone Call"),
                    ("discord", "Discord"),
                    ("email", "Email"),
                    ("gotify", "Gotify"),
                    ("hipchat", "HipChat"),
                    ("linenotify", "LINE Notify"),
                    ("matrix", "Matrix"),
                    ("mattermost", "Mattermost"),
                    ("msteams", "Microsoft Teams"),
                    ("ntfy", "ntfy"),
                    ("opsgenie", "Opsgenie"),
                    ("pagerteam", "Pager Team"),
                    ("pagertree", "PagerTree"),
                    ("pd", "PagerDuty"),
                    ("po", "Pushover"),
                    ("pushbullet", "Pushbullet"),
                    ("rocketchat", "Rocket.Chat"),
                    ("shell", "Shell Command"),
                    ("signal", "Signal"),
                    ("slack", "Slack"),
                    ("sms", "SMS"),
                    ("spike", "Spike"),
                    ("telegram", "Telegram"),
                    ("trello", "Trello"),
                    ("victorops", "Splunk On-Call"),
                    ("webhook", "Webhook"),
                    ("whatsapp", "WhatsApp"),
                    ("zendesk", "Zendesk"),
                    ("zulip", "Zulip"),
                ],
                max_length=20,
            ),
        ),
    ]
