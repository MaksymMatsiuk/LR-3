from rest_framework import serializers
from ..models import Instrument, Order

class InstrumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instrument
        fields = ['name', 'description', 'price', 'stock_quantity', 'instrument_type', 'photo']

class OrderSerializer(serializers.ModelSerializer):
    instrument = InstrumentSerializer() 
    class Meta:
        model = Order
        fields = ['instrument', 'quantity', 'customer_name', 'customer_email', 'order_date']