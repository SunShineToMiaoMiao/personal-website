from django.db import models


class CompressedTextField(models.TextField):
    """
    减少文本的长度，保存数据的时候压缩，读取的时候解压缩，如果发现压缩后更长，就用原文本直接存储
    """

    def from_db_value(self, value, expression, connection, context):
        """ 用于转化数据库中的字符到 Python的变量 """
        if not value:
            return value
        # noinspection PyBroadException
        try:
            return value.decode('base64').decode('bz2').decode('utf-8')
        except Exception:
            return value

    def to_python(self, value):
        """ 用于转化数据库中的字符到 Python的变量 """
        if not value:
            return value
        # noinspection PyBroadException
        try:
            return value.decode('base64').decode('bz2').decode('utf-8')
        except Exception:
            return value

    def get_prep_value(self, value):
        """  用于将Python变量处理后(此处为压缩）保存到数据库，使用和Django自带的 Field 一样。 """
        if not value:
            return value
        # noinspection PyBroadException
        try:
            value.decode('base64')
            return value
        except Exception:
            # noinspection PyBroadException
            try:
                return value.encode('utf-8').encode('bz2').encode('base64')
            except Exception:
                return value

