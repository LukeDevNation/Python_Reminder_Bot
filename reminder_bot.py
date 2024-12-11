import time
from datetime import datetime, timedelta
from plyer import notification

# Función para convertir la cadena de texto de la fecha en un objeto datetime
def parse_date(day, month, year, hour, minute):
    try:
        return datetime(year, month, day, hour, minute)
    except ValueError as e:
        print(f"\033[91mError al parsear la fecha: {e}\033[0m")
        return None

# Función para agregar recordatorio
def add_reminder(reminders, reminder_text, reminder_time, repeat):
    reminder = {"text": reminder_text, "time": reminder_time, "repeat": repeat}
    reminders.append(reminder)

# Función para eliminar recordatorio
def remove_reminder(reminders, index):
    try:
        reminders.pop(index)
        print("\033[92mRecordatorio eliminado correctamente.\033[0m")
    except IndexError:
        print("\033[91mError: No se encontró el recordatorio.\033[0m")

# Función para verificar y mostrar los recordatorios
def check_reminders(reminders):
    while True:
        now = datetime.now()
        for reminder in reminders[:]:
            if reminder["time"] <= now:
                notification.notify(
                    title="Recordatorio",
                    message=reminder["text"],
                    timeout=10  # La notificación durará 10 segundos
                )
                
                if reminder["repeat"]:
                    reminder["time"] = reminder["time"] + timedelta(minutes=10)  # Repite cada 10 minutos
                else:
                    reminders.remove(reminder)  # Eliminar el recordatorio una vez disparado
        time.sleep(60)  # Comprobamos cada minuto

# Función para mostrar el menú principal
def show_main_menu():
    print("\n\033[95m====================================\033[0m")
    print("\033[94m¡Bienvenido al Bot de Recordatorios!\033[0m")
    print("\033[92mSeleccione una opción:\033[0m")
    print("1. Crear un nuevo recordatorio")
    print("2. Ver mis recordatorios")
    print("3. Eliminar un recordatorio")
    print("4. Salir")
    print("\033[95m====================================\033[0m")

# Función principal
def main():
    reminders = []

    while True:
        show_main_menu()

        option = input("\033[93mIngrese una opción (1-4): \033[0m")
        
        if option == "1":
            # Crear un nuevo recordatorio
            print("\n\033[96mCreando un nuevo recordatorio...\033[0m")
            reminder_text = input("\033[94mIngrese el texto del recordatorio: \033[0m")
            if reminder_text.lower() == "salir":
                break

            try:
                # Ingreso de fecha
                day = int(input("\033[94mIngrese el día del recordatorio (1-31): \033[0m"))
                month = int(input("\033[94mIngrese el mes del recordatorio (1-12): \033[0m"))
                year = int(input("\033[94mIngrese el año del recordatorio (ej. 2024): \033[0m"))
                hour = int(input("\033[94mIngrese la hora del recordatorio (0-23): \033[0m"))
                minute = int(input("\033[94mIngrese los minutos del recordatorio (0-59): \033[0m"))
                
                reminder_time = parse_date(day, month, year, hour, minute)
                if reminder_time is None:
                    continue  # Si la fecha es inválida, vuelve a mostrar el menú

                # Verificación si es repetitivo o no
                repeat_input = input("\033[94m¿El recordatorio es repetitivo cada 10 minutos? (sí/no): \033[0m").lower()
                repeat = repeat_input == "sí"

                # Agregar el recordatorio
                add_reminder(reminders, reminder_text, reminder_time, repeat)
                print(f"\033[92mRecordatorio añadido: '{reminder_text}' para {reminder_time}\033[0m")
                
                time.sleep(1)

            except Exception as e:
                print(f"\033[91mError al agregar el recordatorio. Asegúrate de que los datos sean correctos: {e}\033[0m")
                continue

        elif option == "2":
            # Ver los recordatorios
            if reminders:
                print("\n\033[93mTus recordatorios actuales son:\033[0m")
                for idx, reminder in enumerate(reminders, 1):
                    print(f"{idx}. {reminder['text']} - {reminder['time']}")
            else:
                print("\033[91mNo tienes recordatorios en este momento.\033[0m")
            time.sleep(1)

        elif option == "3":
            # Eliminar un recordatorio
            if reminders:
                print("\n\033[93mSelecciona el número del recordatorio que deseas eliminar o escribe 'cancelar' para volver al menú:\033[0m")
                for idx, reminder in enumerate(reminders, 1):
                    print(f"{idx}. {reminder['text']} - {reminder['time']}")
                user_input = input("\033[94mNúmero del recordatorio a eliminar: \033[0m")
                
                if user_input.lower() == "cancelar":
                    print("\033[91mOperación de eliminación cancelada.\033[0m")
                    continue
                
                try:
                    reminder_idx = int(user_input) - 1
                    remove_reminder(reminders, reminder_idx)
                except ValueError:
                    print("\033[91mPor favor, ingresa un número válido.\033[0m")
            else:
                print("\033[91mNo tienes recordatorios para eliminar.\033[0m")
            time.sleep(1)

        elif option == "4":
            # Salir del programa
            print("\033[92m¡Gracias por usar el Bot de Recordatorios! Hasta pronto.\033[0m")
            break

        else:
            print("\033[91mOpción inválida. Por favor, ingresa una opción válida (1-4).\033[0m")
            time.sleep(1)

    # Comienza a comprobar los recordatorios (esto se ejecutará después de salir del menú principal)
    check_reminders(reminders)

if __name__ == "__main__":
    main()
