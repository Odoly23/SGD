import os, hashlib
from uuid import uuid4

def membru_foto(instance, filename):
    upload_to = 'Membru_Foto/{}'.format(instance.nu_eleitoral)
    field = 'photo'
    ext = filename.split('.')[-1]
    if instance.pk:
        filename = '{}_{}.{}'.format(field, instance.nu_eleitoral, ext)
    else:
        filename = '{}_{}'.format(uuid4().hex, ext)
    return os.path.join(upload_to, filename)


