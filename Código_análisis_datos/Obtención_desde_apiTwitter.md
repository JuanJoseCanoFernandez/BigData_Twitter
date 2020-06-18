# Data Analysis With Twitter
## OBJETIVO.  

**Obtener datos a tiempo real a través de la aplicación de Twitter.**

### ¿Qué necesitamos? 

- Una cuenta Desarrolladora en Twitter que nos brinde la posibilidad de poder acceder a sus datos.
- Aprender a usar SparkStreaming.
- Scala IDE de Eclipse.
- JDK 8 en nuestro entorno de trabajo.
- Hosting para alojar la aplicación de Twitter.
- Diferentes dependencias como Spark-Core, Spark-Sql, Spark-Streaming, etc.

#### Código para lanzar el texto de diferentes tweets en una franja de 10 segundos:


~~~ 
import org.apache.spark.streaming.StreamingContextPythonHelper
import org.apache.spark.streaming.Seconds
import org.apache.spark.streaming.StreamingContext
import org.apache.spark.streaming.twitter.TwitterUtils

object ejemplo extends App {
  System.setProperty("twitter4j.oauth.consumerKey", "iaoBdZFCTxgfDaDOapT9xjY0o")
  System.setProperty("twitter4j.oauth.consumerSecret", "jKewh3KvhYEcfm3Xu3dvRq1OwTHHsg1bzBQp1xPxd3xxrNF3Ey")
  System.setProperty("twitter4j.oauth.accessToken", "363892724-oZeFUDhvfOeryLTOMn3aeMh0huRxMr72lDjUl1UR")
  System.setProperty("twitter4j.oauth.accessTokenSecret", "VKqoG8cYA5vzfyDuWbC9pJynqZutcq6B41fRnxdjlapUy")
  // creamos un streamingContext que recibe que se ejecute aqui y le digo que se ejecute durante 10 segundos, 
  // en el cual el va a procesar, con los datos de esos segundos voy a hacer lo que yo quiera
  val ssc = new StreamingContext("local[*]", "IngestaTweets", Seconds(10))

  // aqui se ingesta todos los tweets en "tweets"
  val tweets = TwitterUtils.createStream(ssc, None)

  // nos quedamos con el texto, le hacemos un mapeo 
  val texto = tweets.map(status => status.getText())
  // pintamos la variable texto pero no se puede ejecutar ya que necesitamos lanzar antes el streaming context
  texto.print()
  // lanzamos el streamingContext 
  ssc.start()
  ssc.awaitTermination()
}
~~~

