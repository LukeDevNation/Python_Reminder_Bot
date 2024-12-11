import time
from datetime import datetime, timedelta
from plyer import notification

# Función para convertir la cadena de texto de la fecha en un objeto datetime
def parse_date(day, month, year, hour, minute):
    return datetime(year, month, day, hour, minute)

# Función para agregar recordatorio
def add_reminder(reminders, reminder_text, reminder_time, repeat):
    reminder = {"text": reminder_text, "time": reminder_time, "repeat": repeat}
    reminders.append(reminder)

# Función para verificar y mostrar los recordatorios
def check_reminders(reminders):
    while True:
        now = datetime.now()
        for reminder in reminders:
            if reminder["time"] <= now:
                notification.notify(
                    title="Recordatorio",
                    message=reminder["text"],
                    timeout=10  # La notificación durará 10 segundos
                )
                
                if reminder["repeat"]:
                    reminder["time"] = reminder["time"] + timedelta(minutes=10)  # Repite cada 10 minutos
                else:
                    reminders.remove(reminder)
        time.sleep(60)  # Comprobamos cada minuto

# Función principal
def main():
    reminders = []

    # Mensaje de bienvenida y cómo salir
    print("\033[92m¡Bienvenido al Bot de Recordatorios!\033[0m")
    print("Para salir en cualquier momento, escribe 'salir'.")
    
    reminder_text = input("Ingrese el texto del recordatorio: ")
    if reminder_text.lower() == "salir":
        return  # Sale inmediatamente si el texto es "salir"
    
    try:
        # Ingreso de fecha
        day = int(input("Ingrese el día del recordatorio (1-31): "))
        month = int(input("Ingrese el mes del recordatorio (1-12): "))
        year = int(input("Ingrese el año del recordatorio (ej. 2024): "))
        hour = int(input("Ingrese la hora del recordatorio (0-23): "))
        minute = int(input("Ingrese los minutos del recordatorio (0-59): "))
        
        # Verificación si es repetitivo o no
        repeat_input = input("¿El recordatorio es repetitivo cada 10 minutos? (sí/no): ").lower()
        repeat = repeat_input == "sí"

        reminder_time = parse_date(day, month, year, hour, minute)
        
        # Agregar el recordatorio
        add_reminder(reminders, reminder_text, reminder_time, repeat)
        print(f"Recordatorio añadido: '{reminder_text}' para {reminder_time}")
        
        # El programa termina después de agregar el recordatorio
        return  # Salir del programa

    except Exception as e:
        print(f"Error al agregar el recordatorio. Asegúrate de que los datos sean correctos: {e}")
        return  # En caso de error, se sale del programa

    # Comienza a comprobar los recordatorios (esto no se ejecutará porque el programa terminará antes)
    check_reminders(reminders)

if __name__ == "__main__":
    main()
