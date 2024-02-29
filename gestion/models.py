from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin,BaseUserManager


TipoPlatoOpciones = [
    ('entrada', 'ENTRADA'),
    ('plato_de_fondo', 'PLATO DE FONDO'),
    ('postre', 'POSTER')
]

# sirve par apoder indicar como vamos a manejar a nuestro usuario en el proyecto 
class ManejoUsuario(BaseUserManager):
    def create_superuser(self, nombre, correo, password):
        if not correo:
            raise ValueError('El usuario tiene que tener correo')
        
        # metodo propio de auth_user y sirve ara poner el correo todo en minuscula quitar espacios en blanco 
        # al comienzo y final
        corre_normalizado=self.normalize_email(correo)
        nuevo_usuario=self.model(correo=correo, nombre=nombre)
        nuevo_usuario.set_password(password)

        nuevo_usuario.is_superuser = True
        nuevo_usuario.is_staff = True
        # ahora procedo a guardar mi nuevo usuario
        nuevo_usuario.save()

# vamos a utilizar el modelo auth_user proviniente del panel administrativo
#PermissionsMixin > sirve para indcarle a nuestro proyecto que ahora esta tabala tmb se la encargada
# de manejar el sistema de permisos, es decir ahi se centran todos los permisos que demos a nuestro a nuestra
# aplicacion en el panel administrativo
        
class Cheff(AbstractBaseUser, PermissionsMixin):
    #permite modificar por completo mi tabla auth
    id= models.AutoField(primary_key=True, null=False)
    nombre = models.TextField(null=False)


    correo= models.EmailField(unique=True, null=False)
        # si vamos a configurar la password si o si tiene que llamarse password 
    password = models.TextField(null=False)

        #para que siga funcionando el panel administrativo de django tenemos que configurar las siguientes columnas
        # is_staff > surve para indicar que el usuario que estamos creando puede tener acceso al panel administrativo
    is_staff= models.BooleanField(default=False)
        #is_active > sirve para indicar si el usuario tiene acceso o no al panel administrativo y este se puede cambiar si. por ejemplo le usuario deja de estar activo en la aplicacion

    is_active = models.BooleanField(default=True)
        # para poder realizar el logun en el panel administrativo tenemos que definir que columna se usuara como username
        #
    USERNAME_FIELD = 'correo'
        # sirve para pedirle al usuario al momento de crear un superusuario por la consola
        #python manage.py createsuperuser
        # no se debe declarar el atributo del username_field ni los campos password
    REQUIRED_FIELDS=['nombre']

    # vamos a modificar el comportamiento del atributo objects para que pueda aceptar una creacion de superusuario con consola

    objects = ManejoUsuario()

    class Meta:
        db_table='cheffs'




class Plato(models.Model):
    #https://docs.djangoproject.com/en/5.0/ref/models/fields/
    id = models.AutoField(primary_key=True, null=False)
    nombre = models.TextField(null=False)
    # width field y height_field sirve para indicar las dimensiones de la imagen pero estas dimensiones seran utilizadas si es que vamos a utiliar las templates
    # de django
    foto = models.ImageField()
    tipo = models.TextField(choices=TipoPlatoOpciones, 
                            default=TipoPlatoOpciones[0][0]
                            ) # entrada

    cheffId = models.ForeignKey(
        to=Cheff, db_column = 'cheff_id', on_delete=models.RESTRICT, null=True)
    
    class Meta:
        # https://docs.djangoproject.com/en/5.0/ref/models/options/
        # srive para indicar como se llamara la tabla en la base de datos
        db_table = 'platos'

class Ingrediente(models.Model):
    id= models.AutoField(primary_key=True, null=False)
    descripcion= models.TextField(null= False)
  # para crear una relacion entre dos modelos se usa el ForeignKey
    # to > sirve para indicar la referencia hacia la tabla con la cual crearemos la relacion
    # db_column > indicar como se va a llamar esta columna en la base de datos
    # on_delete > indicar como se va a comportar cuando se elimine el padre (Plato al cual pertenece)
    # CASCADE > si se elimina el plato, se eliminaran todos sus ingredientes
    # PROTECT > evita la eliminacion del plato si tiene ingredientes lanzado un error de tipo ProtectedError
    # RESTRICT > evita la eliminacion del plato si tiene ingredientes y lanza un error de tipo RestrictedError
    # SET_NULL > permite la eliminacion del plato y le cambia el valor a sus ingredientes a la columna plato_id a NULL (los deja huerfanos)
    # SET_DEFAULT > permite la eliminacion del plato y cambia el valor de la columna a un valor por defecto
    # DO_NOTHING > permite la eliminacion del plato y no cambia el valor del ingrediente del plato_id generando inconsistencia de datos
    # related_name > funciona muy similar al relationship xde lfask y eso significa que creara un atributo virutalen el modelo en el cual estemos creando la conexion
    platoId= models.ForeignKey(
        to= Plato, db_column = 'plato_id', on_delete=models.PROTECT, related_name= 'ingredientes')
    
    class Meta:
        db_table = 'ingredientes'



class Preparacion(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    descripcion = models.TextField(null=False)
    orden = models.TextField(null=False)
    platoId = models.ForeignKey(
        to=Plato, db_column = 'plato_id', on_delete=models.PROTECT, related_name='preparaciones')
   
    class Meta:
        db_table = 'preparaciones'

        # indicar cual sera el ordenamiento al momento de hacer unselect
        # ['orden']> indicar que ahora el ordenamiento sera en relacion al orden de manera ascendente
        #['-orden']> indicar que el ordenamiento sera de manera DESCENDENTE
        ordering = ['-orden']
        # el roden y el plato al cual pertenece esta preparacion jamas se puede repetir
        unique_together = [['orden','platoId']]


    # vamos a utilizar el modelo auth_user proviniente del panel adminsitrativo











