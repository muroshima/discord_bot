#!/usr/bin/env python3
# -*- coding: utf_8 -*-
"""実行スクリプト"""
import discord
import requests
import json
from module.env import discord_settings, slack_settings

intents = discord.Intents.default()
client = discord.Client(intents=intents)

# https://xp-cloud.jp/blog/2023/11/29/183351
# @client.event
# async def on_ready():
#     """チャンネル情報を表示"""
#     for channel in client.get_all_channels():
#         print(channel.name + "," + str(channel.id))

@client.event
async def on_voice_state_update(user, before, after):
    if before.channel != after.channel:
        if after.channel is not None and after.channel.id == discord_settings.DISCORD_VOICE_CHANEL:
            data = {
                "text": "<!channel> " + f"<https://discord.com/channels/1138686065130078312/1138686065734070356|{after.channel.name}>に" + user.display_name + "が参加しました",
            }
            requests.post(slack_settings.SLACK_WEB_HOOK_URL, json.dumps(data))
        elif after.channel is None:
            data = {
                "text": "<!channel> " + f"<https://discord.com/channels/1138686065130078312/1138686065734070356|{before.channel.name}>から" + user.display_name + "が退出しました",
            }
            requests.post(slack_settings.SLACK_WEB_HOOK_URL, json.dumps(data))

if __name__ == "__main__":
    client.run(discord_settings.DISCORD_TOKEN)
