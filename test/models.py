# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class ShopActivity(models.Model):
    cate_id = models.IntegerField()
    title = models.CharField(max_length=255)
    image = models.CharField(max_length=255, blank=True, null=True)
    c_image = models.CharField(max_length=255, blank=True, null=True)
    small_image = models.CharField(max_length=255, blank=True, null=True)
    small_c_image = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    url = models.CharField(max_length=255)
    content = models.TextField(blank=True, null=True)
    addtime = models.IntegerField()
    is_show = models.IntegerField()
    type = models.IntegerField()
    sort = models.IntegerField()
    cost_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    shop_id = models.IntegerField(blank=True, null=True)
    commission = models.IntegerField(blank=True, null=True)
    city = models.IntegerField(blank=True, null=True)
    starttime = models.IntegerField(blank=True, null=True)
    endtime = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    is_open = models.IntegerField(blank=True, null=True)
    type_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shop_activity'


class ShopActivityOrder(models.Model):
    order_id = models.AutoField(primary_key=True)
    order_sn = models.CharField(max_length=20)
    user_id = models.IntegerField()
    shop_id = models.IntegerField(blank=True, null=True)
    pay_status = models.IntegerField()
    mobile = models.CharField(max_length=60)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    real = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    commission = models.DecimalField(max_digits=10, decimal_places=2)
    add_time = models.IntegerField()
    status = models.IntegerField()
    pay_time = models.IntegerField()
    qrcode_starttime = models.IntegerField(blank=True, null=True)
    qrcode_endtime = models.IntegerField(blank=True, null=True)
    costcoupon_sn = models.CharField(max_length=50, blank=True, null=True)
    costcoupon_amount = models.IntegerField(blank=True, null=True)
    real_pay = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    pay_code = models.CharField(max_length=32, blank=True, null=True)
    appointtime = models.IntegerField(blank=True, null=True)
    activity_id = models.IntegerField(blank=True, null=True)
    attr_key_name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shop_activity_order'


class ShopActivityShop(models.Model):
    shop_id = models.IntegerField(blank=True, null=True)
    activity_id = models.IntegerField(blank=True, null=True)
    addtime = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shop_activity_shop'


class ShopAd(models.Model):
    position_id = models.IntegerField()
    name = models.CharField(max_length=255)
    image = models.CharField(max_length=255)
    url = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'shop_ad'


class ShopAdPosition(models.Model):
    name = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'shop_ad_position'


class ShopAdmin(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    lasttime = models.IntegerField()
    ip = models.CharField(db_column='IP', max_length=32, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'shop_admin'


class ShopAdminLog(models.Model):
    admin_id = models.IntegerField(blank=True, null=True)
    log_info = models.CharField(max_length=255, blank=True, null=True)
    log_ip = models.CharField(max_length=30, blank=True, null=True)
    log_time = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shop_admin_log'


class ShopArticle(models.Model):
    cate_id = models.IntegerField()
    title = models.CharField(max_length=255)
    image = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    url = models.CharField(max_length=255)
    content = models.TextField(blank=True, null=True)
    addtime = models.IntegerField()
    is_show = models.IntegerField()
    type = models.IntegerField()
    sort = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'shop_article'


class ShopArticleCategory(models.Model):
    parent_id = models.IntegerField()
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'shop_article_category'


class ShopBackground(models.Model):
    position_id = models.IntegerField()
    name = models.CharField(max_length=255)
    image = models.CharField(max_length=255)
    url = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'shop_background'


class ShopCoupon(models.Model):
    phone = models.CharField(max_length=50)
    price = models.IntegerField()
    shop_id = models.IntegerField()
    open_id = models.CharField(max_length=128)
    addtime = models.IntegerField()
    status = models.IntegerField()
    starttime = models.IntegerField(blank=True, null=True)
    endtime = models.IntegerField(blank=True, null=True)
    user_id = models.CharField(max_length=20, blank=True, null=True)
    source = models.IntegerField(blank=True, null=True)
    amount = models.CharField(max_length=10, blank=True, null=True)
    coupon_sn = models.CharField(max_length=30, blank=True, null=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    order_id = models.CharField(max_length=50, blank=True, null=True)
    usetime = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shop_coupon'


class ShopEjoint(models.Model):
    name = models.CharField(max_length=150)
    mobile = models.CharField(max_length=50, blank=True, null=True)
    weixin = models.CharField(max_length=50, blank=True, null=True)
    content = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shop_ejoint'


class ShopFavour(models.Model):
    shop_id = models.CharField(max_length=255)
    user_id = models.CharField(max_length=11, blank=True, null=True)
    addtime = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shop_favour'


class ShopGoods(models.Model):
    goods_name = models.CharField(max_length=50)
    cate_id = models.IntegerField()
    type_id = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    cost_price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.CharField(max_length=255)
    weight = models.IntegerField()
    store_count = models.IntegerField()
    sales_sum = models.IntegerField()
    give_integral = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    sort = models.IntegerField()
    is_on_sale = models.IntegerField()
    is_recommend = models.IntegerField()
    is_hot = models.IntegerField()
    is_new = models.IntegerField()
    addtime = models.IntegerField()
    is_del = models.IntegerField()
    video = models.CharField(max_length=255, blank=True, null=True)
    shop_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shop_goods'


class ShopGoods1(models.Model):
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'shop_goods1'


class ShopGoodsAttrPrice(models.Model):
    goods_id = models.IntegerField()
    key = models.CharField(max_length=255)
    key_name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    cost_price = models.DecimalField(max_digits=10, decimal_places=2)
    store_count = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'shop_goods_attr_price'


class ShopGoodsAttrValue(models.Model):
    attr_id = models.IntegerField()
    value = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'shop_goods_attr_value'


class ShopGoodsAttribute(models.Model):
    type_id = models.IntegerField()
    name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'shop_goods_attribute'


class ShopGoodsCategory(models.Model):
    name = models.CharField(max_length=50)
    image = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shop_goods_category'


class ShopGoodsImages(models.Model):
    goods_id = models.IntegerField()
    image = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'shop_goods_images'


class ShopGoodsType(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'shop_goods_type'


class ShopIntegralGoods(models.Model):
    goods_name = models.CharField(max_length=50)
    image = models.CharField(max_length=255)
    small_image = models.CharField(max_length=255)
    integral = models.IntegerField()
    weight = models.IntegerField()
    store_count = models.IntegerField()
    content = models.TextField(blank=True, null=True)
    sort = models.IntegerField()
    is_on_sale = models.IntegerField()
    addtime = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=0)
    dtype = models.IntegerField()
    is_del = models.IntegerField()
    cate_id = models.IntegerField(blank=True, null=True)
    shop_id = models.IntegerField(blank=True, null=True)
    color = models.CharField(max_length=400, blank=True, null=True)
    spec = models.CharField(max_length=400, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shop_integral_goods'


class ShopIntegralGoodsCategory(models.Model):
    name = models.CharField(max_length=50)
    image = models.CharField(max_length=255, blank=True, null=True)
    sort = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shop_integral_goods_category'


class ShopIntegralGoodsImages(models.Model):
    goods_id = models.IntegerField()
    image = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'shop_integral_goods_images'


class ShopIntegralOrder(models.Model):
    order_sn = models.CharField(max_length=20)
    user_id = models.IntegerField()
    order_status = models.IntegerField()
    consignee = models.CharField(max_length=60)
    country = models.IntegerField()
    province = models.IntegerField()
    city = models.IntegerField()
    district = models.IntegerField()
    address = models.CharField(max_length=255)
    mobile = models.CharField(max_length=60)
    shipping_code = models.CharField(max_length=32, blank=True, null=True)
    shipping_name = models.CharField(max_length=120, blank=True, null=True)
    shipping_number = models.CharField(max_length=255, blank=True, null=True)
    shipping_time = models.IntegerField()
    goods_id = models.IntegerField()
    prize_id = models.IntegerField()
    goods_name = models.CharField(max_length=120)
    goods_num = models.SmallIntegerField()
    integral = models.IntegerField()
    add_time = models.IntegerField()
    type = models.IntegerField(blank=True, null=True)
    qrcode_starttime = models.IntegerField(blank=True, null=True)
    qrcode_endtime = models.IntegerField(blank=True, null=True)
    qrcode_sn = models.CharField(max_length=50, blank=True, null=True)
    shop_id = models.CharField(max_length=50, blank=True, null=True)
    attr = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shop_integral_order'


class ShopNews(models.Model):
    cate_id = models.IntegerField()
    title = models.CharField(max_length=255)
    image = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    url = models.CharField(max_length=255)
    content = models.TextField(blank=True, null=True)
    addtime = models.IntegerField()
    is_show = models.IntegerField()
    type = models.IntegerField()
    sort = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'shop_news'


class ShopOrder(models.Model):
    order_id = models.AutoField(primary_key=True)
    order_sn = models.CharField(max_length=20)
    user_id = models.IntegerField()
    shop_id = models.IntegerField(blank=True, null=True)
    pay_status = models.IntegerField()
    mobile = models.CharField(max_length=60)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    real = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    commission = models.DecimalField(max_digits=10, decimal_places=2)
    add_time = models.IntegerField()
    status = models.IntegerField()
    pay_time = models.IntegerField()
    source = models.IntegerField(blank=True, null=True)
    costpoint = models.IntegerField(blank=True, null=True)
    qrcode_starttime = models.IntegerField(blank=True, null=True)
    qrcode_endtime = models.IntegerField(blank=True, null=True)
    point_goodsid = models.IntegerField(blank=True, null=True)
    costcoupon_sn = models.CharField(max_length=50, blank=True, null=True)
    costcoupon_amount = models.IntegerField(blank=True, null=True)
    real_pay = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    pay_code = models.CharField(max_length=32, blank=True, null=True)
    appointtime = models.IntegerField(blank=True, null=True)
    size = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shop_order'


class ShopOrderCart(models.Model):
    user_id = models.IntegerField()
    goods_id = models.IntegerField()
    goods_name = models.CharField(max_length=120)
    goods_num = models.SmallIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    cost_price = models.DecimalField(max_digits=10, decimal_places=2)
    attr_key = models.CharField(max_length=64)
    attr_key_name = models.CharField(max_length=64)
    add_time = models.IntegerField()
    is_checked = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'shop_order_cart'


class ShopOrderComment(models.Model):
    order_id = models.IntegerField()
    goods_id = models.IntegerField()
    desc = models.CharField(max_length=255)
    star = models.IntegerField()
    add_time = models.IntegerField()
    star2 = models.IntegerField(blank=True, null=True)
    shop_id = models.IntegerField(blank=True, null=True)
    user_id = models.CharField(max_length=12, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shop_order_comment'


class ShopOrderGoods(models.Model):
    order_id = models.IntegerField()
    goods_id = models.IntegerField()
    goods_name = models.CharField(max_length=120)
    goods_num = models.SmallIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    cost_price = models.DecimalField(max_digits=10, decimal_places=2)
    give_integral = models.IntegerField()
    attr_key = models.CharField(max_length=128)
    attr_key_name = models.CharField(max_length=128)
    is_comment = models.IntegerField()
    prom_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'shop_order_goods'


class ShopOrderLog(models.Model):
    order_id = models.IntegerField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    real = models.DecimalField(max_digits=10, decimal_places=2)
    commission = models.DecimalField(max_digits=10, decimal_places=2)
    addtime = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'shop_order_log'


class ShopPoint(models.Model):
    phone = models.CharField(max_length=50)
    type = models.IntegerField()
    shop_id = models.IntegerField()
    open_id = models.CharField(max_length=128)
    addtime = models.IntegerField()
    status = models.IntegerField()
    sign = models.CharField(max_length=10, blank=True, null=True)
    amount = models.FloatField(blank=True, null=True)
    user_id = models.CharField(max_length=20, blank=True, null=True)
    source = models.IntegerField(blank=True, null=True)
    order_id = models.CharField(max_length=20, blank=True, null=True)
    invite_user_id = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shop_point'


class ShopQrcode(models.Model):
    phone = models.CharField(max_length=50)
    price = models.IntegerField()
    shop_id = models.IntegerField()
    open_id = models.CharField(max_length=128)
    addtime = models.IntegerField()
    status = models.IntegerField()
    starttime = models.IntegerField(blank=True, null=True)
    endtime = models.IntegerField(blank=True, null=True)
    user_id = models.CharField(max_length=20, blank=True, null=True)
    source = models.IntegerField(blank=True, null=True)
    qrcode_sn = models.CharField(max_length=30, blank=True, null=True)
    order_id = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shop_qrcode'


class ShopRbacPower(models.Model):
    name = models.CharField(max_length=255)
    parent_id = models.IntegerField()
    icon = models.CharField(max_length=255)
    controller = models.CharField(max_length=255)
    action = models.CharField(max_length=255)
    sort = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'shop_rbac_power'


class ShopRbacPowerRole(models.Model):
    power_id = models.IntegerField()
    role_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'shop_rbac_power_role'


class ShopRbacRole(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'shop_rbac_role'


class ShopRbacRoleAdmin(models.Model):
    admin_id = models.IntegerField()
    role_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'shop_rbac_role_admin'


class ShopRegion(models.Model):
    id = models.SmallIntegerField(primary_key=True)
    parent_id = models.SmallIntegerField()
    name = models.CharField(max_length=120)
    type = models.IntegerField()
    isable = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shop_region'


class ShopRegionCopy(models.Model):
    id = models.SmallIntegerField(primary_key=True)
    parent_id = models.SmallIntegerField()
    name = models.CharField(max_length=120)
    type = models.IntegerField()
    isable = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shop_region_copy'


class ShopServerOrder(models.Model):
    order_sn = models.CharField(max_length=32)
    store_id = models.IntegerField()
    server_id = models.IntegerField()
    user_id = models.IntegerField()
    need_settle = models.IntegerField()
    settle_money = models.DecimalField(max_digits=10, decimal_places=2)
    state = models.IntegerField()
    create_time = models.IntegerField()
    use_time = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'shop_server_order'


class ShopShipping(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=50)
    desc = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'shop_shipping'


class ShopShippingArea(models.Model):
    shipping_id = models.IntegerField()
    name = models.CharField(max_length=255)
    first_price = models.DecimalField(max_digits=10, decimal_places=2)
    add_price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'shop_shipping_area'


class ShopShippingAreaRegion(models.Model):
    shipping_area_id = models.IntegerField()
    region_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'shop_shipping_area_region'


class ShopShop(models.Model):
    shop_name = models.CharField(max_length=255)
    shop_phone = models.CharField(max_length=255)
    shop_address = models.CharField(max_length=255, blank=True, null=True)
    shop_logo = models.CharField(max_length=255, blank=True, null=True)
    shop_image = models.CharField(max_length=255, blank=True, null=True)
    shop_small_image = models.CharField(max_length=255, blank=True, null=True)
    shop_commission = models.IntegerField(blank=True, null=True)
    shop_lon = models.FloatField(blank=True, null=True)
    shop_lat = models.FloatField(blank=True, null=True)
    shop_content = models.TextField(blank=True, null=True)
    activity_content = models.TextField(blank=True, null=True)
    shop_time = models.CharField(max_length=200, blank=True, null=True)
    shop_user = models.IntegerField(blank=True, null=True)
    score = models.FloatField(blank=True, null=True)
    start_h = models.CharField(max_length=2, blank=True, null=True)
    start_m = models.CharField(max_length=2, blank=True, null=True)
    end_h = models.CharField(max_length=2, blank=True, null=True)
    end_m = models.CharField(max_length=2, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    shortname = models.CharField(max_length=200, blank=True, null=True)
    logo = models.CharField(max_length=200, blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    big_price = models.FloatField(blank=True, null=True)
    province = models.IntegerField(blank=True, null=True)
    city = models.IntegerField(blank=True, null=True)
    district = models.IntegerField(blank=True, null=True)
    shop_small_logo = models.CharField(max_length=255, blank=True, null=True)
    is_on_sale = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shop_shop'


class ShopShopApply(models.Model):
    shop_name = models.CharField(max_length=255)
    shop_phone = models.CharField(max_length=255)
    shop_address = models.CharField(max_length=255)
    shop_logo = models.CharField(max_length=255)
    shop_image = models.CharField(max_length=255)
    shop_commission = models.IntegerField()
    shop_lon = models.FloatField()
    shop_lat = models.FloatField()
    shop_content = models.TextField(blank=True, null=True)
    shop_time = models.CharField(max_length=200)
    shop_user = models.IntegerField()
    score = models.FloatField(blank=True, null=True)
    start_h = models.CharField(max_length=5, blank=True, null=True)
    start_m = models.CharField(max_length=5, blank=True, null=True)
    end_h = models.CharField(max_length=5, blank=True, null=True)
    end_m = models.CharField(max_length=5, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    shop_username = models.CharField(max_length=30, blank=True, null=True)
    province = models.IntegerField(blank=True, null=True)
    city = models.IntegerField(blank=True, null=True)
    district = models.IntegerField(blank=True, null=True)
    mobile = models.CharField(max_length=50, blank=True, null=True)
    password = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shop_shop_apply'


class ShopShopPower(models.Model):
    name = models.CharField(max_length=255)
    parent_id = models.IntegerField()
    icon = models.CharField(max_length=255)
    controller = models.CharField(max_length=255)
    action = models.CharField(max_length=255)
    sort = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'shop_shop_power'


class ShopShopUser(models.Model):
    shop_id = models.IntegerField()
    user = models.CharField(max_length=32)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    password = models.CharField(max_length=64)
    realname = models.CharField(max_length=255, blank=True, null=True)
    cardname = models.CharField(max_length=255, blank=True, null=True)
    shop_type = models.IntegerField()
    card = models.CharField(max_length=255, blank=True, null=True)
    addtime = models.IntegerField()
    lasttime = models.IntegerField()
    is_manager = models.IntegerField(blank=True, null=True)
    paycode = models.CharField(max_length=50, blank=True, null=True)
    power_id1 = models.IntegerField(blank=True, null=True)
    power_id2 = models.IntegerField(blank=True, null=True)
    power_id3 = models.IntegerField(blank=True, null=True)
    power_id4 = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shop_shop_user'


class ShopShopWalletInfo(models.Model):
    order_id = models.CharField(max_length=50, blank=True, null=True)
    user_id = models.CharField(max_length=50, blank=True, null=True)
    source = models.IntegerField(blank=True, null=True)
    openid = models.CharField(max_length=128)
    money_change = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    sign = models.CharField(max_length=1, blank=True, null=True)
    addtime = models.IntegerField(blank=True, null=True)
    nickname = models.CharField(max_length=50, blank=True, null=True)
    isable = models.IntegerField(blank=True, null=True)
    shop_id = models.CharField(max_length=30, blank=True, null=True)
    review = models.IntegerField(blank=True, null=True)
    wallet_sn = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shop_shop_wallet_info'


class ShopShopdetailLog(models.Model):
    user_id = models.IntegerField(blank=True, null=True)
    shop_id = models.IntegerField(blank=True, null=True)
    log_info = models.CharField(max_length=255, blank=True, null=True)
    log_ip = models.CharField(max_length=30, blank=True, null=True)
    addtime = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shop_shopdetail_log'


class ShopSms(models.Model):
    mobile = models.CharField(max_length=20, blank=True, null=True)
    value = models.CharField(max_length=200, blank=True, null=True)
    time = models.IntegerField(blank=True, null=True)
    content = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shop_sms'


class ShopStore(models.Model):
    store_id = models.AutoField(primary_key=True)
    head_pic = models.CharField(max_length=64)
    contact = models.CharField(max_length=64)
    mobile = models.CharField(max_length=20)
    name = models.CharField(max_length=128)
    address = models.CharField(max_length=255)
    lon = models.FloatField(blank=True, null=True)
    lat = models.FloatField(blank=True, null=True)
    license_pic = models.CharField(max_length=64)
    password = models.CharField(max_length=64)
    paycode = models.CharField(max_length=64)
    wallet = models.DecimalField(max_digits=10, decimal_places=2)
    commission_rate = models.IntegerField()
    province = models.SmallIntegerField()
    city = models.SmallIntegerField()
    state = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'shop_store'


class ShopStoreBankCard(models.Model):
    store_id = models.IntegerField()
    name = models.CharField(max_length=60)
    accountno = models.CharField(max_length=32)
    bankname = models.CharField(max_length=128)
    create_time = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'shop_store_bank_card'


class ShopStoreCashApply(models.Model):
    store_id = models.IntegerField()
    money = models.DecimalField(max_digits=10, decimal_places=2)
    card_id = models.IntegerField()
    create_time = models.IntegerField()
    update_time = models.IntegerField(blank=True, null=True)
    state = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'shop_store_cash_apply'


class ShopStoreWalletDetail(models.Model):
    store_id = models.IntegerField()
    order_id = models.IntegerField()
    buyer_id = models.IntegerField()
    sale_money = models.DecimalField(max_digits=10, decimal_places=2)
    money = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.IntegerField(blank=True, null=True)
    remark = models.CharField(max_length=255)
    create_time = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'shop_store_wallet_detail'


class ShopSystem(models.Model):
    title = models.CharField(max_length=255)
    keywords = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    logo = models.CharField(max_length=255)
    point_rate = models.IntegerField()
    commission_rate = models.IntegerField()
    mobile = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    jifen_cost = models.FloatField(blank=True, null=True)
    jifen_endtime = models.IntegerField(blank=True, null=True)
    jifen_chongzhi = models.FloatField(blank=True, null=True)
    jifen_invite = models.FloatField(blank=True, null=True)
    jifen_share = models.FloatField(blank=True, null=True)
    jifen_comment = models.FloatField(blank=True, null=True)
    jifen_max = models.FloatField(blank=True, null=True)
    coupon_point = models.IntegerField(blank=True, null=True)
    coupon_day = models.IntegerField(blank=True, null=True)
    coupon_value = models.IntegerField(blank=True, null=True)
    qrcode_day = models.IntegerField(blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    beiancode = models.CharField(max_length=100, blank=True, null=True)
    wechat = models.CharField(max_length=100, blank=True, null=True)
    company = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shop_system'


class ShopUser(models.Model):
    phone = models.CharField(max_length=50, blank=True, null=True)
    paypass = models.CharField(max_length=50, blank=True, null=True)
    nickname = models.CharField(max_length=250, blank=True, null=True)
    head_pic = models.CharField(max_length=255, blank=True, null=True)
    openid = models.CharField(max_length=128, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    addtime = models.IntegerField(blank=True, null=True)
    distributor_id = models.IntegerField(blank=True, null=True)
    distributor2_id = models.IntegerField(blank=True, null=True)
    is_first = models.IntegerField(blank=True, null=True)
    unionid = models.CharField(max_length=128, blank=True, null=True)
    xopenid = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shop_user'


class ShopUserAddress(models.Model):
    user_id = models.IntegerField()
    consignee = models.CharField(max_length=60)
    mobile = models.CharField(max_length=20)
    province = models.IntegerField()
    city = models.IntegerField()
    district = models.IntegerField()
    address = models.CharField(max_length=120)
    is_default = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'shop_user_address'


class ShopUserCopy(models.Model):
    phone = models.CharField(max_length=50)
    paypass = models.CharField(max_length=50)
    nickname = models.CharField(max_length=250, blank=True, null=True)
    head_pic = models.CharField(max_length=255)
    openid = models.CharField(max_length=128)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    addtime = models.IntegerField()
    distributor_id = models.IntegerField(blank=True, null=True)
    distributor2_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shop_user_copy'


class ShopWalletInfo(models.Model):
    order_id = models.CharField(max_length=50, blank=True, null=True)
    user_id = models.CharField(max_length=50, blank=True, null=True)
    source = models.IntegerField(blank=True, null=True)
    openid = models.CharField(max_length=128)
    money_change = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    sign = models.CharField(max_length=1, blank=True, null=True)
    addtime = models.IntegerField(blank=True, null=True)
    nickname = models.CharField(max_length=50, blank=True, null=True)
    isable = models.IntegerField(blank=True, null=True)
    shop_id = models.CharField(max_length=30, blank=True, null=True)
    wallet_sn = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shop_wallet_info'


class ShopWithdraw(models.Model):
    shop_id = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    realname = models.CharField(max_length=255)
    cardname = models.CharField(max_length=255)
    card = models.CharField(max_length=255)
    status = models.IntegerField()
    addtime = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'shop_withdraw'


class ShopWithdrawReview(models.Model):
    shop_id = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    realname = models.CharField(max_length=255)
    cardname = models.CharField(max_length=255)
    card = models.CharField(max_length=255)
    status = models.IntegerField()
    addtime = models.IntegerField()
    number = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shop_withdraw_review'


class ShopWrite(models.Model):
    phone = models.CharField(max_length=50)
    price = models.FloatField()
    shop_id = models.IntegerField()
    open_id = models.CharField(max_length=128)
    addtime = models.IntegerField()
    status = models.IntegerField()
    order_id = models.CharField(max_length=255, blank=True, null=True)
    order_sn = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shop_write'


class ShopWriteoffType(models.Model):
    shop_user_id = models.IntegerField()
    price = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'shop_writeoff_type'
