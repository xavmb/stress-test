from locust import HttpUser, task, between
import random
import string

class AlertaStressTest(HttpUser):
    wait_time = between(1, 2)

    @task
    def create_alerta(self):
        # Generar datos aleatorios para la prueba
        etiqueta = random.choice(['Urgente', 'Importante', 'Normal'])
        descripcion = ''.join(random.choices(string.ascii_uppercase + string.digits, k=20))
        latitud = random.uniform(-90.0, 90.0)
        longitud = random.uniform(-180.0, 180.0)
        visibilidad = random.choice(['Contactos seguros', 'Verificados', 'Miembros'])
        
        # Datos del formulario
        data = {
            'nombre': descripcion,
            'ciudad': descripcion,
            'descripcion': descripcion,
            'imagen': 'https://th.bing.com/th/id/OIP.SEFbLrKFny0S8RQUUl1h0QHaEc?rs=1&pid=ImgDetMain',
            'direccion': descripcion,
            'ubicacion': {
                'coordinateX': {'latitude': latitud, 'longitude': longitud},
                'coordinateY': {'latitude': latitud, 'longitude': longitud}
            },
             'isActived': 0,
            'tipo_lugar': 'parqueadero',
            'servicio': descripcion,
            'isVerificado': 0,
            'longitud': 0,
            'tarifa': 0,
            'capacidad': 0

        }

        # Header con el token de autorización
        headers = {'Authorization': 'Token aed2b5007e3b3f4208b05e491009c678d1c536d2'}

        # Realizar la solicitud POST
        # Se va cambiando dependiendo del endpoint
        self.client.post('https://ecuaciclismoapp.pythonanywhere.com/api/lugar/new_lugar/', json=data, headers=headers)

