import os
import configparser
from typing import AbstractSet

from phonegram.config import constants


class SessionConfig(configparser.ConfigParser):
    def __init__(self):
        super().__init__()

    @staticmethod
    def create(filename: str):
        """
        Creates the SessionConfig object and reads the config file.

        :param filename: the name of the session config file
        :return: SessionConfig object
        """
        if not os.path.exists(filename):
            raise FileNotFoundError(f"Указанный файл '{filename}' конфигурации сессии не найден")

        # Read the config file
        session_config = SessionConfig()
        session_config.read(filename, encoding='utf-8')

        # Session strings may be omitted. Therefore, creates its section
        if not session_config.has_section(constants.SESSION_STRINGS_SECTION):
            session_config.add_section(constants.SESSION_STRINGS_SECTION)

        return session_config

    @property
    def api_id(self) -> int:
        """
        Returns api_id of a Telegram client from the session config file

        :return: (int) api_id
        """
        try:
            api_id = int(self.get(constants.CLIENT_CREDENTIALS_SECTION, 'API_ID'))
            return api_id
        except configparser.NoSectionError:
            raise configparser.Error(f"Конфигурационный файл сессии не содержит секции "
                                     f"{constants.CLIENT_CREDENTIALS_SECTION}, пожалуйста, добавьте её")
        except configparser.NoOptionError:
            raise configparser.Error("Конфигурационный файл сессии не содержит опции API_ID, пожалуйста, "
                                     "добавьте её")

    @property
    def api_hash(self) -> str:
        """
        Returns api_hash of a Telegram client from the session config file

        :return: (str) api_hash
        """
        try:
            return self.get(constants.CLIENT_CREDENTIALS_SECTION, 'API_HASH')
        except configparser.NoSectionError:
            raise configparser.Error(f"Конфигурационный файл сессии не содержит секции "
                                     f"{constants.CLIENT_CREDENTIALS_SECTION}, пожалуйста, добавьте её")
        except configparser.NoOptionError:
            raise configparser.Error("Конфигурационный файл сессии не содержит опции API_HASH, пожалуйста, "
                                     "добавьте её")

    @property
    def session_strings(self) -> AbstractSet[tuple[str, str]]:
        """
        Returns pair <user_id, session_string> from the session config file.
        This session string allow to authorize in the Telegram client.

        :return: (tuple[str, str]) pairs of <user_id, session_string> or None if it's empty
        """
        try:
            return strings if (strings := self[constants.SESSION_STRINGS_SECTION].items()) else None
        except configparser.NoSectionError:
            raise configparser.Error(f"Конфигурационный файл сессии не содержит секции "
                                     f"{constants.SESSION_STRINGS_SECTION}, пожалуйста, добавьте её")
