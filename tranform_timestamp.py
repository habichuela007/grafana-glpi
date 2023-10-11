import datetime
import pytz

timestamp = 1696955646
zona_horaria = pytz.timezone('America/Guayaquil')  # UTC-5

fecha = datetime.datetime.fromtimestamp(timestamp, tz=zona_horaria)

print(f"Fecha y hora en UTC-5: {fecha}")
