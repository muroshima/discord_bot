#!/usr/bin/env python3
# -*- coding: utf_8 -*-

"""Discord用の環境変数"""

from pydantic_settings import BaseSettings


class DiscordSettings(BaseSettings):
    """Discord環境変数を取得する設定クラス"""
    DISCORD_TOKEN: str
    DISCORD_VOICE_CHANEL: int

class SlackSettings(BaseSettings):
    """Slackの環境変数を取得する設定クラス"""
    SLACK_WEB_HOOK_URL: str

discord_settings = DiscordSettings()
slack_settings = SlackSettings()