from django.db import models
import pickle


class Setting(models.Model):
    key = models.CharField(max_length=100, unique=True)
    value = models.BinaryField()
    protocol = models.IntegerField(default=pickle.HIGHEST_PROTOCOL)

    def set(self, value):
        self.value = pickle.dumps(value, self.protocol)
        self.save()

    def get(self):
        return pickle.loads(self.value)

    def __str__(self):
        return self.key
