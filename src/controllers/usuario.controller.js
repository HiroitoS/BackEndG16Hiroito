import { conexion } from "../conectores.js";
import { registroUsuario, loginUsuario } from "../dto/usuario.dto.js";
import bcryptjs from "bcryptjs";
import jwt from 'jsonwebtoken'


export const registro = async (req, res) =>{
    const validacion = registroUsuario.validate(req.body)

    if(validacion.error){
        return res.status(400).json({
            message:'Error al registrar al usuario',
            content: validacion.error
        })
    }

    const salt= await bcryptjs.genSalt()

    // ahora combinamos el salt con la password para que no retorne el hash de la password
    const passwordHashed = await bcryptjs.hash(validacion.value.password, salt)

    const nuevoUsuario = await conexion.usuario.create({

        // le pasamos todo el CONTENIDO (..) de nuestra validacion .value y luego le modificamos la password
        // esto tiene que ir al final porque si lo ponemos al comienzo se sobreescriba con lo que esta en
        // validacion.value 
        data: { ...validacion.value, password: passwordHashed}
    })

    return res.status(201).json({
        message: 'Usuario creado exitosamente',
        content: nuevoUsuario
    })

}

export const login = async (req, res) =>{
    const validacion = loginUsuario.validate(req.body)

    if(validacion.error){
        return res.status(400).json({
            message:'Error al hacer el login',
            content: validacion.error
        })

    }


    const { correo, password} = validacion.value

    const usuarioEncontrado = await conexion.usuario.findFirstOrThrow({where: { correo } })


    const esLaPassword = await bcryptjs.compare(password, usuarioEncontrado.password)

    if(esLaPassword){
        // generar la token de acceso
        // sign > firmar >  sirve para crear una nueva token
        // expiresIn > un numero o un string, si le pasamos un numero este sera el valor en segundos y si le 
        //pasamos un string este puede ser de los siguientes formatos ' i day' |    '10 days' | '1hr '| 24 horas        jwt.sign({usuarioId: usuarioEncontrado.id}, process.env.JWT_SECRET__KEY, { expiresIn })
        const token = jwt.sign({usuarioId: usuarioEncontrado.id, tipo:usuarioEncontrado.tipoUsuario}, 
            process.env.JWT_SECRET_KEY, { expiresIn:'8h'})

        return res.json({
            message: 'Bienvenido',
            content: token
        })
    } else{
        return res.status(400).json({
            message: 'Credenciales incorrectas'
        })
    }
}