from rest_framework import serializers
from .models import Table, Reservation
from datetime import timedelta


class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = '__all__'


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'

    def validate(self, data):
        new_start = data['reservation_time']
        new_end = new_start + timedelta(minutes=data['duration_minutes'])
        table = data['table']

        # Фильтруем брони по тому же столику
        existing_reservations = Reservation.objects.filter(table=table)

        # Если обновляем объект, исключаем текущую бронь из проверки
        if self.instance:
            existing_reservations = existing_reservations.exclude(pk=self.instance.pk)

        for reservation in existing_reservations:
            existing_start = reservation.reservation_time
            existing_end = existing_start + timedelta(minutes=reservation.duration_minutes)

            # Проверка на пересечение
            if new_start < existing_end and new_end > existing_start:
                raise serializers.ValidationError(
                    f"Столик уже забронирован с {existing_start} до {existing_end}"
                )

        return data
