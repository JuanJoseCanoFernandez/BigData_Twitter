# ¿Qué vamos a hacer? 

### Código para comprobar cual es el trending topic en estos momento y guardar los resultados en un fichero externo.

## Código:

~~~
package juanjo_twitter

import org.apache.spark.streaming.StreamingContextPythonHelper
import org.apache.spark.streaming.Seconds
import org.apache.spark.streaming.StreamingContext
import org.apache.spark.streaming.twitter.TwitterUtils
import java.util.Date

object trendingTopic extends App {
  System.setProperty("twitter4j.oauth.consumerKey", "iaoBdZFCTxgfDaDOapT9xjY0o")
  System.setProperty("twitter4j.oauth.consumerSecret", "jKewh3KvhYEcfm3Xu3dvRq1OwTHHsg1bzBQp1xPxd3xxrNF3Ey")
    System.setProperty("twitter4j.oauth.accessToken", "363892724-upOnovreTdekuMhBnqkPfN2H6gkb7XyWAoRvhdNi")
  System.setProperty("twitter4j.oauth.accessTokenSecret", "AVCnno8ytkjtFP8PWDaO89HJSJ3TlvGvLdS78CRbpflfd")
  
  // el * muestra el numero de hilos y el tiempo de lanzamiento será de 30 segundos
  val ssc = new StreamingContext("local[*]", "TTSpain", Seconds(30))
  // creamos nuestros tweets
  val tweets = TwitterUtils.createStream(ssc,None)
  // hacemos el analisis con una ventana de 90 segundos
  val tweetsWindows = tweets.window(Seconds(90))
  // nos creamos una clase tweet con su fecha y texto 
  case class Tweet(created_at: Date, texto: String)
  // nos quedamos con los tweets en español haciendole un filtro y mapeo con los elementos de mi clase tweet
  val espanol = tweetsWindows.filter(status => status.getLang.equals("es")).map(status => Tweet(status.getCreatedAt(), status.getText()))
  // seleccionamos el texto, lo partimos y nos quedamos con aquellos que tengan la palabra covid19
  val tt = espanol.filter(_.texto.split("_")contains("COVID19"))
  // guardamos los resultados en una ruta y le damos un formato de texto
  tt.saveAsTextFiles("/Users/User/twitter_ficheros/TT", "csv")
  tt.print()
  ssc.start()
  ssc.awaitTermination()
  
}

~~~