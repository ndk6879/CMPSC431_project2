from django.db import models

class Patient(models.Model):
    FirstName = models.CharField(max_length=200)
    LastName = models.CharField(max_length=200)

class Address(models.Model):
    address_id = models.CharField(max_length=200) # Field name made lowercase.
    zipcode = models.IntegerField()
    street_num = models.IntegerField()
    street_name = models.CharField(max_length=225)

    # class Meta:
    #     managed = False
    #     db_table = 'Address'


class Buyers(models.Model):
    email = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    gender = models.CharField(max_length=200)
    age = models.IntegerField()
    home_address_id = models.CharField(max_length=200)
    billing_address_id = models.CharField(max_length=200)

    # class Meta:
    #     managed = False
    #     db_table = 'Buyers'


class Categories(models.Model):
    category_name = models.CharField(max_length=200)
    parent_category = models.CharField(max_length=200)

    # class Meta:
    #     managed = False
    #     db_table = 'Categories'


class CreditCards(models.Model):
    credit_card_num = models.CharField(max_length=200)
    card_code = models.IntegerField()
    expire_month = models.IntegerField()
    expire_year = models.IntegerField()
    card_type = models.CharField(max_length=200)
    owner_email = models.CharField(max_length=200)# Field name made lowercase.

    # class Meta:
    #     managed = False
    #     db_table = 'Credit_Cards'


class LocalVendors(models.Model):
    email = models.CharField(max_length=200)  # Field name made lowercase.
    business_name = models.CharField(max_length=200) # Field name made lowercase.
    business_address_id = models.CharField(max_length=200)  # Field name made lowercase.
    customer_service_number = models.CharField(max_length=200) # Field name made lowercase.

    # class Meta:
    #     managed = False
    #     db_table = 'Local_Vendors'


class Orders(models.Model):
    transaction_id = models.IntegerField()  # Field name made lowercase.
    seller_email = models.CharField(max_length=200) # Field name made lowercase.
    listing_id = models.IntegerField()  # Field name made lowercase.
    buyer_email = models.CharField(max_length=200)  # Field name made lowercase.
    date = models.CharField(max_length=200)  # Field name made lowercase.
    quantity = models.IntegerField()  # Field name made lowercase.
    payment = models.IntegerField()  # Field name made lowercase.

    # class Meta:
    #     managed = False
    #     db_table = 'Orders'


class ProductListings(models.Model):
    seller_email = models.CharField(max_length=200)  # Field name made lowercase.
    listing_id = models.IntegerField(unique=True)  # Field name made lowercase.
    category = models.CharField(max_length=200) # Field name made lowercase.
    title = models.CharField(max_length=200)  # Field name made lowercase.
    product_name = models.CharField(max_length=200) # Field name made lowercase.
    product_description = models.TextField()  # Field name made lowercase.
    price = models.TextField()  # Field name made lowercase.
    quantity = models.IntegerField()  # Field name made lowercase.

    # class Meta:
    #     managed = False
    #     db_table = 'Product_Listings'
    #     unique_together = (('seller_email', 'listing_id'),)


class Rating(models.Model):
    buyer_email = models.CharField(max_length=200) # Field name made lowercase.
    seller_email = models.CharField(max_length=200)  # Field name made lowercase.
    date = models.CharField(max_length=200) # Field name made lowercase.
    rating = models.IntegerField()  # Field name made lowercase.
    rating_desc = models.TextField()  # Field name made lowercase.

    # class Meta:
    #     managed = False
    #     db_table = 'Rating'
    #     unique_together = (('buyer_email', 'seller_email', 'date'),)


class Reviews(models.Model):
    buyer_email = models.CharField(max_length=200)  # Field name made lowercase.
    seller_email = models.CharField(max_length=200)  # Field name made lowercase.
    listing_id = models.IntegerField()  # Field name made lowercase.
    review_desc = models.CharField(max_length=200) # Field name made lowercase.

    # class Meta:
    #     managed = False
    #     db_table = 'Reviews'
    #     unique_together = (('buyer_email', 'seller_email', 'listing_id'),)


class Sellers(models.Model):
    email = models.CharField(max_length=200)
    routing_number = models.CharField(max_length=200)
    account_number = models.IntegerField()
    balance = models.IntegerField()

    # class Meta:
    #     managed = False
    #     db_table = 'Sellers'


class Users(models.Model):
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
#     REQUIRED_FIELDS = ''
#     USERNAME_FIELD = ''
#
#     class Meta:
#         managed = False
#         db_table = 'Users'


class ZipcodeInfo(models.Model):
    zipcode = models.IntegerField()
    city = models.CharField(max_length=200)
    state_id = models.CharField(max_length=200)
    population = models.IntegerField()
    density = models.FloatField()
    county_name = models.CharField(max_length=200)
    timezone = models.CharField(max_length=200)

    # class Meta:
    #     managed = False
    #     db_table = 'Zipcode_Info'
