# ¿Qué vamos a hacer? 

### Código para sacar los hashtags: Filtramos los tweets en español, nos quedamos con las palabras que empiezan por #, le añado un contador a cada hashtag y contamos cuantas veces se van repitiendo. 

## Código:

~~~
package juanjo_twitter

import org.apache.spark.streaming.StreamingContextPythonHelper
import org.apache.spark.streaming.Seconds
import org.apache.spark.streaming.StreamingContext
import org.apache.spark.streaming.twitter.TwitterUtils

object hashtag extends App {
  System.setProperty("twitter4j.oauth.consumerKey", "iaoBdZFCTxgfDaDOapT9xjY0o")
  System.setProperty("twitter4j.oauth.consumerSecret", "jKewh3KvhYEcfm3Xu3dvRq1OwTHHsg1bzBQp1xPxd3xxrNF3Ey")
    System.setProperty("twitter4j.oauth.accessToken", "363892724-upOnovreTdekuMhBnqkPfN2H6gkb7XyWAoRvhdNi")
  System.setProperty("twitter4j.oauth.accessTokenSecret", "AVCnno8ytkjtFP8PWDaO89HJSJ3TlvGvLdS78CRbpflfd")

  // el * muestra el numero de hilos
  val ssc = new StreamingContext("local[*]", "hastagcount", Seconds(60))
  //ingesta de tweets sin filtros
  val tweets = TwitterUtils.createStream(ssc, None)
  // filtramos los tweets que estan en español
  val tweetsSpain = tweets.filter(status => status.getLang.equals("es"))
  // de los tweets en español nos quedamos con las palabras que empiezan por la # . Aqui con cada tweet nos quedamos con el text, 
  // dividimos por el espacio y seleccionamos todas las palabras que empiecen por #
  val hashtags = tweetsSpain.flatMap(status => status.getText().split(" ").filter(_.startsWith("#")))
  // contamos los hashtags= a cada hashtags le ponemos un 1 y despues agrupamos por el hashtag y sumamos todos los 1 que tenga. 
  //Despues lo ordenamos de mayor a menor, por ello ponemos false, ya que si fuese "ascending" seria de menor a mayor. 
  //_._1 = hashtag y _._2 = la cuenta de las veces que ha salido dicho hashtag
  val hashtagsCount = hashtags.map(h => (h,1)).reduceByKey(_ + _).transform(_.sortBy(_._2, false))
  //pintamos
  hashtagsCount.print()
  ssc.start()
  ssc.awaitTermination()

}

~~~