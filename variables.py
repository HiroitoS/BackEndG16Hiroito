from flask_sqlalchemy import SQLAlchemy

# La conexion enre mi OR; y mi BAse de Datos
# No se recomienda tener mas de 1 conexion a la base de datos
conexion = SQLAlchemy()