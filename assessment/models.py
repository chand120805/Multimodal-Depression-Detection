from django.db import models
from django.contrib.auth.models import User
from users.utils.encryption import encrypt_text, decrypt_text


class Assessment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # =========================
    # PHQ scores (encrypted)
    # =========================
    _q1 = models.TextField(db_column="q1")
    _q2 = models.TextField(db_column="q2")
    _q3 = models.TextField(db_column="q3")
    _q4 = models.TextField(db_column="q4")
    _q5 = models.TextField(db_column="q5")
    _q6 = models.TextField(db_column="q6")
    _q7 = models.TextField(db_column="q7")
    _q8 = models.TextField(db_column="q8")

    # =========================
    # TEXT answers (encrypted)
    # =========================
    _text1 = models.TextField(db_column="text1", blank=True, null=True)
    _text2 = models.TextField(db_column="text2", blank=True, null=True)
    _text3 = models.TextField(db_column="text3", blank=True, null=True)
    _text4 = models.TextField(db_column="text4", blank=True, null=True)
    _text5 = models.TextField(db_column="text5", blank=True, null=True)
    _text6 = models.TextField(db_column="text6", blank=True, null=True)
    _text7 = models.TextField(db_column="text7", blank=True, null=True)
    _text8 = models.TextField(db_column="text8", blank=True, null=True)

    total_score = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    # =========================
    # PHQ GETTERS/SETTERS
    # =========================
    def _get_int(self, value):
        return int(decrypt_text(value)) if value else None

    def _set_int(self, value):
        return encrypt_text(str(value)) if value is not None else None

    @property
    def q1(self): return self._get_int(self._q1)
    @q1.setter
    def q1(self, value): self._q1 = self._set_int(value)

    @property
    def q2(self): return self._get_int(self._q2)
    @q2.setter
    def q2(self, value): self._q2 = self._set_int(value)

    @property
    def q3(self): return self._get_int(self._q3)
    @q3.setter
    def q3(self, value): self._q3 = self._set_int(value)

    @property
    def q4(self): return self._get_int(self._q4)
    @q4.setter
    def q4(self, value): self._q4 = self._set_int(value)

    @property
    def q5(self): return self._get_int(self._q5)
    @q5.setter
    def q5(self, value): self._q5 = self._set_int(value)

    @property
    def q6(self): return self._get_int(self._q6)
    @q6.setter
    def q6(self, value): self._q6 = self._set_int(value)

    @property
    def q7(self): return self._get_int(self._q7)
    @q7.setter
    def q7(self, value): self._q7 = self._set_int(value)

    @property
    def q8(self): return self._get_int(self._q8)
    @q8.setter
    def q8(self, value): self._q8 = self._set_int(value)

    # =========================
    # TEXT GETTERS/SETTERS
    # =========================
    def _get_text(self, value):
        return decrypt_text(value) if value else None

    def _set_text(self, value):
        return encrypt_text(value) if value else None

    @property
    def text1(self): return self._get_text(self._text1)
    @text1.setter
    def text1(self, value): self._text1 = self._set_text(value)

    @property
    def text2(self): return self._get_text(self._text2)
    @text2.setter
    def text2(self, value): self._text2 = self._set_text(value)

    @property
    def text3(self): return self._get_text(self._text3)
    @text3.setter
    def text3(self, value): self._text3 = self._set_text(value)

    @property
    def text4(self): return self._get_text(self._text4)
    @text4.setter
    def text4(self, value): self._text4 = self._set_text(value)

    @property
    def text5(self): return self._get_text(self._text5)
    @text5.setter
    def text5(self, value): self._text5 = self._set_text(value)

    @property
    def text6(self): return self._get_text(self._text6)
    @text6.setter
    def text6(self, value): self._text6 = self._set_text(value)

    @property
    def text7(self): return self._get_text(self._text7)
    @text7.setter
    def text7(self, value): self._text7 = self._set_text(value)

    @property
    def text8(self): return self._get_text(self._text8)
    @text8.setter
    def text8(self, value): self._text8 = self._set_text(value)