from pyspark.sql import SparkSession

# Créer une session Spark
spark = SparkSession.builder \
    .appName("E-commerce Logs Analysis") \
    .getOrCreate()

# Paramètres de connexion à PostgreSQL
database_url = "jdbc:postgresql://localhost/nom_de_votre_base"
properties = {"user": "votre_nom_utilisateur", "password": "votre_mot_de_passe", "driver": "org.postgresql.Driver"}

# Lire les données depuis PostgreSQL
df = spark.read.jdbc(url=database_url, table="e_commerce_logs", properties=properties)

# Afficher les premières lignes pour vérifier
df.show()
