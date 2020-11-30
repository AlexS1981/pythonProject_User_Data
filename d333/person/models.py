from django.db import models
from rest_framework.utils import json
# Create your models here.


class Person(models.Model):
    name = models.CharField(max_length=20)
    surn = models.CharField(max_length=20)
    pasw1 = models.CharField(max_length=20)
    pasw2 = models.CharField(max_length=20)
    status = models.IntegerField()
    file_info = models.FileField()

    def __str__(self):
        return "{} / {} / {}".format(self.name, self.surn, self.file_info)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None, *args, **kwargs):
        super(Person, self).save(*args, **kwargs)
        str_fn = "file_data_{}.json".format(self.id)
        Person.objects.filter(pk=self.id).update(file_info=str_fn)
        dict_to_write = {
                            'name': self.name,
                            'surn': self.surn
                         }
        with open("person/user_data_files/{}".format(str_fn), 'w') as fw:
            fw.write('{\n')
            for key in dict_to_write:
                fw.write('\t')
                json.dump('{}'.format(key), fw)
                fw.write(': ')
                json.dump('{}'.format(dict_to_write.get(key)), fw)
                fw.write(',\n')
            fw.write('\t')
            json.dump('pasw', fw)
            fw.write(': ')
            json.dump('{}'.format(self.pasw1), fw)
            fw.write('\n}')
        fw.close()
