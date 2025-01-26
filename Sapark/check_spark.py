import os
import subprocess
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, avg, count, when

def check_spark_installation():
    try:
        # Verifica si PySpark está instalado
        import pyspark
        print("PySpark está instalado correctamente.")
    except ImportError:
        print("PySpark no está instalado. Por favor, instálalo con 'pip install pyspark'.")
        return

    # Configura las variables de entorno relacionadas con Spark y Java
    os.environ['SPARK_HOME'] = 'C:\\spark\\spark-3.5.4-bin-hadoop3\\spark-3.5.4-bin-hadoop3'
    os.environ['JAVA_HOME'] = 'C:\\Program Files\\Java\\jdk1.8.0_202'
    os.environ['PYSPARK_PYTHON'] = 'C:\\Python311\\python.exe'
    os.environ['PYSPARK_DRIVER_PYTHON'] = 'C:\\Python311\\python.exe'
    os.environ['PATH'] = os.pathsep.join([
        os.path.join(os.environ['SPARK_HOME'], 'bin'),
        os.path.join(os.environ['JAVA_HOME'], 'bin'),
        os.environ['PATH']
    ])

    # Verifica las variables de entorno relacionadas con Spark
    spark_home = os.getenv('SPARK_HOME')
    java_home = os.getenv('JAVA_HOME')
    pyspark_python = os.getenv('PYSPARK_PYTHON')
    pyspark_driver_python = os.getenv('PYSPARK_DRIVER_PYTHON')

    if spark_home:
        print(f"SPARK_HOME está configurado: {spark_home}")
    else:
        print("SPARK_HOME no está configurado. Asegúrate de configurarlo apuntando a tu instalación de Spark.")

    if java_home:
        print(f"JAVA_HOME está configurado: {java_home}")
    else:
        print("JAVA_HOME no está configurado. Asegúrate de configurarlo apuntando a tu instalación de Java.")

    if pyspark_python:
        print(f"PYSPARK_PYTHON está configurado: {pyspark_python}")
    else:
        print("PYSPARK_PYTHON no está configurado. Asegúrate de configurarlo apuntando a tu instalación de Python.")

    if pyspark_driver_python:
        print(f"PYSPARK_DRIVER_PYTHON está configurado: {pyspark_driver_python}")
    else:
        print("PYSPARK_DRIVER_PYTHON no está configurado. Asegúrate de configurarlo apuntando a tu instalación de Python.")

    # Imprime las variables de entorno para depuración
    print(f"PATH: {os.environ['PATH']}")

    # Verifica si 'spark-submit' funciona correctamente
    try:
        spark_submit_path = os.path.join(os.environ['SPARK_HOME'], 'bin', 'spark-submit.cmd')
        result = subprocess.run([spark_submit_path, '--version'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if result.returncode == 0:
            print("El comando 'spark-submit' está funcionando correctamente.")
            print(result.stdout)
        else:
            print("Hubo un problema al ejecutar 'spark-submit':")
            print(result.stderr)
    except FileNotFoundError:
        print("El comando 'spark-submit' no está disponible. Asegúrate de que Spark esté correctamente instalado y en el PATH.")
    except OSError as e:
        print(f"Error al ejecutar 'spark-submit': {e}")

def test_pyspark():
    # Inicia una sesión de Spark
    spark = SparkSession.builder \
        .appName("PySpark Test") \
        .getOrCreate()

    # Crea un DataFrame de prueba
    data = [
        ("Alice", 34, "F"),
        ("Bob", 45, "M"),
        ("Catherine", 29, "F"),
        ("David", 40, "M"),
        ("Eve", 35, "F"),
        ("Frank", 50, "M")
    ]
    columns = ["Name", "Age", "Gender"]
    df = spark.createDataFrame(data, columns)

    # Muestra el DataFrame original
    print("DataFrame original:")
    df.show()

    # Filtra el DataFrame para mostrar solo las filas donde la edad es mayor que 30
    df_filtered = df.filter(col("Age") > 30)
    print("DataFrame filtrado (Age > 30):")
    df_filtered.show()

    # Calcula y muestra la edad promedio
    df_avg_age = df.agg(avg(col("Age")).alias("Average Age"))
    print("Edad promedio:")
    df_avg_age.show()

    # Cuenta el número de personas por género
    df_gender_count = df.groupBy("Gender").agg(count("Name").alias("Count"))
    print("Número de personas por género:")
    df_gender_count.show()

    # Añade una columna indicando si la persona es mayor de 40 años
    df_with_age_flag = df.withColumn("Is_Over_40", when(col("Age") > 40, "Yes").otherwise("No"))
    print("DataFrame con columna 'Is_Over_40':")
    df_with_age_flag.show()

    # Detiene la sesión de Spark
    spark.stop()

if __name__ == "__main__":
    check_spark_installation()
    test_pyspark()