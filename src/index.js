import express from 'express'
import * as Rutas from './router/index.js'

const servidor = express()

servidor.use(express.json())


servidor .use(Rutas.categoriaRouter)
servidor.use(Rutas.usuarioRouter)

servidor.listen(process.env.PORT, () => {
    console.log(`Servidor corriendo exitosamente en el puerto ${process.env.PORT}`)
})