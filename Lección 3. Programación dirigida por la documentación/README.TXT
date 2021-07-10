1 .Crear entorno virtual:
    virtualenv Lec3_env
2. Entrar entorno virtual:
    source Lec3_env/bin/activate
    NOTA: Descativar entorno:
        deactivate
3. Instalar Sphinx:
    pip install Sphinx
4. Ejecutar sphinx:
    sphinx-quickstart
5. Generar ficheros de documentacion  aprtir del codigo fuente:
    sphinx-apidoc -f -o source . (source: donde esta el archivo conf.py)
    NOTA: 
        - Utilizamos la opción -f para sobrescribir cualquier fichero generado anteriormente.
        - Utilizamos la opción -o para indicarle la ruta donde queremos almacenar los ficheros de salida.
6. Generar la documentacion:
    make html
    NOTA: hay mas formatos de salida