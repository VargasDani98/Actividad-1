def dd_to_dms(degrees):
  d = int(degrees)
  m = int((degrees - d) * 60)
  s = (degrees - d - m / 60) * 3600
  return d, m, s


def dms_to_dd(degrees, minutes, seconds):
  dd = degrees + minutes / 60 + seconds / 3600
  return dd


def conversion_dd_to_dms():
  latitude_dd = float(input("Ingrese el valor de la Latitud en DD: "))
  longitude_dd = float(input("Ingrese el valor de la Longitud en DD: "))

  latitude_dms = dd_to_dms(latitude_dd)
  longitude_dms = dd_to_dms(longitude_dd)

  print(
      f"\nEl valor de la Latitud es: {latitude_dms[0]}° {latitude_dms[1]}' {latitude_dms[2]:.4f}'' N"
  )
  print(
      f"El valor de la Longitud es: {longitude_dms[0]}° {longitude_dms[1]}' {longitude_dms[2]:.4f}'' W"
  )


def conversion_dms_to_dd():
  latitude_degrees = float(input("Ingrese el valor de la Latitud en grados: "))
  latitude_minutes = float(
      input("Ingrese el valor de los minutos de la Latitud: "))
  latitude_seconds = float(
      input("Ingrese el valor de los segundos de la Latitud: "))

  longitude_degrees = float(
      input("Ingrese el valor de la Longitud en grados: "))
  longitude_minutes = float(
      input("Ingrese el valor de los minutos de la Longitud: "))
  longitude_seconds = float(
      input("Ingrese el valor de los segundos de la Longitud: "))

  latitude_dd = dms_to_dd(latitude_degrees, latitude_minutes, latitude_seconds)
  longitude_dd = dms_to_dd(longitude_degrees, longitude_minutes,
                           longitude_seconds)

  print(f"\nEl valor de la Latitud en DD es: {latitude_dd}")
  print(f"El valor de la Longitud en DD es: {longitude_dd}")


def main():
  print("Seleccione el tipo de conversión que desea realizar:")
  print("1. DD a DMS")
  print("2. DMS a DD")

  opcion = input(">> ")

  if opcion == "1":
    conversion_dd_to_dms()
  elif opcion == "2":
    conversion_dms_to_dd()
  else:
    print("Opción no válida. Por favor, seleccione 1 o 2.")


if __name__ == "__main__":
  main()

