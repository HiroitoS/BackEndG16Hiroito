import jwt  from "jsonwebtoken"
import { conexion } from "./conectores.js"


export const validarToken = (req, res, next) =>{

    const {authorization} = req.headers


    if(!authorization){
        return res.status(403).json({
            message: 'Se necesita una token para esta peticion'
        })
    }
    const token = authorization.split(' ')[1]// devolveria un arreglo 
    
    if(!token){
        return res.status(403).json({
            message: 'La token se tiene que enviar usando el formato <Bearer YOUR_TOKEN'
        })
    }

    try {
        const payload = jwt.verify(token, process.env.JWT_SECRET_KEY)
        req.user= payload// {usuarioId:'..., tipo: ADMIN}
        //Le indicamos que prosiga con los controladores que vienen luego de este middleware
        next()
    }
    catch(error){
        return res.status(400).json({
            message:'Token invalida',
            content: error.message
        })
    }

}
