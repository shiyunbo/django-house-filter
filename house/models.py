from django.db import models

# Create your models here.


class City(models.TextChoices):
    BEIJING = 'bj', '北京'
    SHANGHAI = 'sh', '上海'
    SHENZHEN = 'sz', '深圳'
    GUANGZHOU = 'gz', '广州'
    HANGZHOU = 'hz', '杭州'


class Bedroom(models.TextChoices):
    B1 = '1', '1室1厅'
    B2 = '2', '2室1厅'
    B3 = '3', '3室1厅'
    B4 = '4', '4室2厅'


class Area(models.TextChoices):
    A1 = '1', '<50平米'
    A2 = '2', '50-70平米'
    A3 = '3', '70-90平米'
    A4 = '4', '90-140平米'
    A5 = '5', '>140平米'


class Floor(models.TextChoices):
    LOW = 'l', '低楼层'
    MIDDLE = 'm', '中楼层'
    HIGH = 'h', '高楼层'


class Direction(models.TextChoices):
    EAST = 'e', '东'
    SOUTH = 's', '南'
    WEST = 'w', '西'
    NORTH = 'n', '北'


class Community(models.Model):
    name = models.CharField(max_length=60, verbose_name='小区')
    city = models.CharField(max_length=2, choices=City.choices, verbose_name="城市")
    add_date = models.DateTimeField(auto_now_add=True, verbose_name="发布日期")
    mod_date = models.DateTimeField(auto_now=True, verbose_name="修改日期")

    class Meta:
        verbose_name = "小区"
        verbose_name_plural = "小区"

    def __str__(self):
        return self.name


class House(models.Model):
    description = models.CharField(max_length=108, verbose_name="描述")
    community = models.ForeignKey('Community', on_delete=models.CASCADE, verbose_name="小区")
    bedroom = models.CharField(max_length=1, choices=Bedroom.choices, verbose_name="房型")
    direction = models.CharField(max_length=2, choices=Direction.choices, verbose_name="朝向")
    floor = models.CharField(max_length=1, choices=Floor.choices, verbose_name="楼层")
    area = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="面积(平方米)")
    area_class = models.CharField(max_length=1, null=True, blank=True, choices=Area.choices, verbose_name="面积")
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="价格(万元)")
    add_date = models.DateTimeField(auto_now_add=True, verbose_name="发布日期")
    mod_date = models.DateTimeField(auto_now=True, verbose_name="修改日期")

    class Meta:
        verbose_name = "二手房"
        verbose_name_plural = "二手房"

    def __str__(self):
        return '{}.{}'.format(self.description, self.community)

    def save(self, *args, **kwargs):
        if self.area < 50:
            self.area_class = Area.A1
        elif 50 <= self.area < 70:
            self.area_class = Area.A2
        elif 70 <= self.area < 90:
            self.area_class = Area.A3
        elif 90 <= self.area < 140:
            self.area_class = Area.A4
        else:
            self.area_class = Area.A5

        super().save(*args, **kwargs)





