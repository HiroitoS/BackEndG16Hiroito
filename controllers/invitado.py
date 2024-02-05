from flask_restful import Resource, request

class InvitadosController(Resource):
    # el metodo tiene que ser en minisculas sino no lo reconocera
    def post(self):
        print('Ingreso al post')
        request.get_json()# {dni: 44685621, telefono: 913801465}
        return{
            'message': 'Invitado creado exitosamente'
        }
    
