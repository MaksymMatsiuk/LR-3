from rest_framework import serializers
from ..models import Instrument, Order

# Serializer for the Instrument model
class InstrumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instrument
        fields = ['id', 'name', 'description', 'price', 'stock_quantity', 'instrument_type', 'photo']

# Serializer for the Order model
class OrderSerializer(serializers.ModelSerializer):
    instrument = InstrumentSerializer()  # Nested serializer to represent the instrument data  
    class Meta:
        model = Order
        fields = ['id', 'instrument', 'quantity', 'customer_name', 'customer_email', 'order_date']