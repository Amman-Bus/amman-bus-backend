from django.db.models.fields.files import ImageField
from django.db import models
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image,ImageDraw

# Create your models here.
class QRC(models.Model):
    name= models.CharField(max_length=150)
    code= models.ImageField(blank=True , upload_to='code')

    def __str__(self) -> str:
        return self.name

    def save(self, *args, **kwargs) :
        qr_image = qrcode.make(self.name)
        canvas= Image.new('RGB',(310,310), 'white')
        canvas.paste(qr_image)
        file_name= f'{self.name}.png'
        stream =BytesIO()
        canvas.save(stream, 'PNG')
        self.code.save(file_name,File(stream), save=False)
        canvas.close()
        super().save(*args,**kwargs)
        
        


