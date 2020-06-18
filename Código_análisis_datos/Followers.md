# ¿Qué vamos a hacer? 

### Código para recopilar un número de tweets de los usuarios con mas seguidores.

## Código:

~~~
package juanjo_twitter

import org.apache.spark.streaming.StreamingContextPythonHelper
import org.apache.spark.streaming.Seconds
import org.apache.spark.streaming.StreamingContext
import org.apache.spark.streaming.twitter.TwitterUtils
import java.util.Date
import java.io.File

object followers extends App {
  System.setProperty("twitter4j.oauth.consumerKey", "iaoBdZFCTxgfDaDOapT9xjY0o")
  System.setProperty("twitter4j.oauth.consumerSecret", "jKewh3KvhYEcfm3Xu3dvRq1OwTHHsg1bzBQp1xPxd3xxrNF3Ey")
  System.setProperty("twitter4j.oauth.accessToken", "363892724-upOnovreTdekuMhBnqkPfN2H6gkb7XyWAoRvhdNi")
  System.setProperty("twitter4j.oauth.accessTokenSecret", "AVCnno8ytkjtFP8PWDaO89HJSJ3TlvGvLdS78CRbpflfd")
  
  // el * muestra el numero de hilos
  val ssc = new StreamingContext("local[*]", "followers", Seconds(30))
  // creamos nuestros tweets
  val tweets = TwitterUtils.createStream(ssc, None)
  //creamos una ventana de 90 segundos
  val tweetsWindows = tweets.window(Seconds(90))
  //creamos la clase de nuestro tweet
  case class Tweet(created_at: Date, user: String, texto: String, followers: Int)
  // filtramos por el idioma en español y mapeamos en función de la clase creada anteriormente
  val mytweets = tweetsWindows.filter(_.getLang.equals("es")).map(t => Tweet(t.getCreatedAt(), t.getUser.getScreenName, t.getText, t.getUser.getFollowersCount))
  // ordenamos los tweet por el numero de seguidores(ordenando con el sortBy). False porque lo queremos descendente
  val orderFollowers = mytweets.transform(_.sortBy(_.followers, false))
  // Para cada uno de los rdds que conforman el dataset hacemos lo siguiente:
  val ordenTen = mytweets.transform( rdd => {
    // ordenamos por numero de seguidores y se queda con 10 elementos
    val list = rdd.sortBy(_.followers, false).take(10);
    // filtramos los 10 rdd con los que tenemos en toda la lista
    rdd.filter(list.contains)
  }
  )
  //guardamos los resultados en una ruta
  ordenTen.saveAsTextFiles("output/numero")
  ssc.start()
  ssc.awaitTermination()

  ~~~